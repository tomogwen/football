
import json
import matplotlib.pyplot as plt
import seaborn as sns


def create_pitch(fig, ax):
    # code from http://petermckeever.com/2019/01/plotting-pitches-in-python/

    # n.b. alpha=0 in pitch creation
    pitch = 'white'

    # fig, ax = plt.subplots(figsize=(10.4, 6.8))
    ax.axis('off')  # this hides the x and y ticks

    # side and goal lines #

    ly1 = [0, 0, 68, 68, 0]

    lx1 = [0, 104, 104, 0, 0]

    ax.plot(lx1, ly1, color="black", zorder=5)

    # boxes, 6 yard box and goals

    # outer boxes#

    ly2 = [13.84, 13.84, 54.16, 54.16]
    lx2 = [104, 87.5, 87.5, 104]
    ax.plot(lx2, ly2, color="black", zorder=5)

    ly3 = [13.84, 13.84, 54.16, 54.16]
    lx3 = [0, 16.5, 16.5, 0]
    ax.plot(lx3, ly3, color="black", zorder=5)

    # goals
    ly4 = [30.34, 30.34, 37.66, 37.66]
    lx4 = [104, 104.2, 104.2, 104]
    ax.plot(lx4, ly4, color="black", zorder=5)

    ly5 = [30.34, 30.34, 37.66, 37.66]
    lx5 = [0, -0.2, -0.2, 0]
    ax.plot(lx5, ly5, color="black", zorder=5)

    # 6 yard boxes#
    ly6 = [24.84, 24.84, 43.16, 43.16]
    lx6 = [104, 99.5, 99.5, 104]
    ax.plot(lx6, ly6, color="black", zorder=5)

    ly7 = [24.84, 24.84, 43.16, 43.16]
    lx7 = [0, 4.5, 4.5, 0]
    ax.plot(lx7, ly7, color="black", zorder=5)

    # Halfway line, penalty spots, and kickoff spot

    vcy5 = [0, 68]
    vcx5 = [52, 52]
    ax.plot(vcx5, vcy5, color="black", zorder=5)

    ax.scatter(93, 34, color="black", zorder=5)
    ax.scatter(11, 34, color="black", zorder=5)
    ax.scatter(52, 34, color="black", zorder=5)

    circle1 = plt.Circle((93.5, 34), 9.15, ls='solid', lw=1.5, color="black", fill=False, zorder=1, alpha=0)
    circle2 = plt.Circle((10.5, 34), 9.15, ls='solid', lw=1.5, color="black", fill=False, zorder=1, alpha=0)
    circle3 = plt.Circle((52, 34), 9.15, ls='solid', lw=1.5, color="black", fill=False, zorder=2, alpha=1)

    circle1 = plt.Circle((93.5, 34), 9.15, ls='solid', lw=1.5, color="black", fill=False, zorder=1, alpha=0)
    circle2 = plt.Circle((10.5, 34), 9.15, ls='solid', lw=1.5, color="black", fill=False, zorder=1, alpha=0)
    circle3 = plt.Circle((52, 34), 9.15, ls='solid', lw=1.5, color="black", fill=False, zorder=2, alpha=1)

    ## Rectangles in boxes
    rec1 = plt.Rectangle((87.5, 20), 16, 30, ls='-', color="white", zorder=1, alpha=0)
    rec2 = plt.Rectangle((0, 20), 16.5, 30, ls='-', color="white", zorder=1, alpha=0)

    ## Pitch rectangle

    rec3 = plt.Rectangle((-1, -1), 106, 70, color=pitch, zorder=1, alpha=0)

    ax.add_artist(rec3)
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(rec1)
    ax.add_artist(rec2)
    ax.add_artist(circle3)

    return fig, ax


def load_file(file_name):
    with open(file_name) as f:
        return json.load(f)


def import_data(country):
    print("Importing data...")
    matches = load_file("data/matches/matches_" + country + ".json")
    events = load_file("data/events/events_" + country + ".json")
    players = load_file("data/players.json")
    teams = load_file("data/teams.json")
    print("Done")
    return matches, events, players, teams


def import_all():
    players = load_file("data/players.json")
    teams = load_file("data/teams.json")

    competitions = ["England",
                    "European_Championship",
                    "France",
                    "Germany",
                    "Italy",
                    "Spain",
                    "World_Cup"]

    matches_temp, events_temp = [], []
    for i in range(len(competitions)):
        print("Importing matches from " + competitions[i])
        matches_temp.append(load_file("data/matches/matches_" + competitions[i] + ".json"))
        events_temp.append(load_file("data/events/events_" + competitions[i] + ".json"))

    matches = [item for sublist in matches_temp for item in sublist]
    events = [item for sublist in events_temp for item in sublist]

    return matches, events, players, teams


def find_team_name(id, teams):
    for i in range(len(teams)):
        # print(teams[i]['wyId'])
        if int(teams[i]['wyId']) == int(id):
            return teams[i]['officialName']
    return 'Invalid Team ID'


def team_names(teamsData, teams):
    team_ids = []
    for key in teamsData.keys():
        team_ids.append(key)

    return team_ids[0], find_team_name(team_ids[0], teams), team_ids[1], find_team_name(team_ids[1], teams)


def identify_events(events, match_id):
    print("Processing events...")
    match_events = []
    num_events = len(events)
    for i in range(num_events):
        if int(events[i]['matchId']) == int(match_id):
            match_events.append(events[i])
        # if i % math.floor(num_events/5) == 0:
        #     print('Processed: ' + str(i) + '/' + str(num_events))

    print("Done")
    return match_events


def find_pass(match_events, team_id):
    passes = []
    for i in range(len(match_events)):
        if match_events[i]['eventName'] == 'Pass' and int(match_events[i]['teamId']) == int(team_id):
            passes.append(match_events[i])

    return passes


def find_all(events, event_type):
    events_list = []
    for i in range(len(events)):
        if events[i]['eventName'] == event_type:
            events_list.append(events[i])
    return events_list


def get_coords(events):
    x, y = [], []
    for i in range(len(events)):
        x.append(events[i]['positions'][0]['x'])
        y.append(events[i]['positions'][0]['y'])
    return x, y


def scale_to_pitch(x, y):
    new_x = []
    new_y = []
    for i in range(len(x)):
        new_x.append(int(float(x[i])*1.04))
        new_y.append(int(float(y[i])*0.68))
    return new_x, new_y


def find_match(matches, home_id, away_id):
    for i in range(len(matches)):
        if list(matches[i]['teamsData'].keys()) == [str(home_id), str(away_id)]:
            return i, matches[i]['wyId']