
import json
import matplotlib.pyplot as plt
import seaborn as sns


def team_id_dicts():
    team_name = {
        "1613": "Newcastle United",
        "692": "Celta de Vigo",
        "691": "Espanyol",
        "696": "Deportivo Alav\u00e9s",
        "695": "Levante",
        "3795": "Troyes",
        "698": "Getafe",
        "2454": "Borussia M'gladbach",
        "1673": "Huddersfield Town",
        "678": "Athletic Club",
        "679": "Atl\u00e9tico Madrid",
        "3766": "Olympique Lyonnais",
        "3767": "PSG",
        "674": "Valencia",
        "675": "Real Madrid",
        "676": "Barcelona",
        "714": "Las Palmas",
        "712": "Legan\u00e9s",
        "3204": "SPAL",
        "10531": "Swansea City",
        "3771": "Olympique Marseille",
        "3770": "Nantes",
        "3775": "Nice",
        "3774": "Rennes",
        "3779": "Strasbourg",
        "701": "Eibar",
        "1659": "AFC Bournemouth",
        "1651": "Brighton & Hove Albion",
        "2443": "Werder Bremen",
        "2446": "Bayer Leverkusen",
        "2447": "Borussia Dortmund",
        "2444": "Bayern M\u00fcnchen",
        "2445": "Stuttgart",
        "2449": "Schalke 04",
        "3157": "Milan",
        "3799": "Angers",
        "3159": "Juventus",
        "3158": "Roma",
        "3315": "Sassuolo",
        "1646": "Burnley",
        "3772": "Bordeaux",
        "2455": "Hannover 96",
        "3804": "Dijon",
        "2457": "Hertha BSC",
        "2451": "Wolfsburg",
        "2450": "Hamburger SV",
        "2453": "Freiburg",
        "3166": "Bologna",
        "3777": "Metz",
        "3164": "Sampdoria",
        "3165": "Chievo",
        "3162": "Lazio",
        "3163": "Udinese",
        "3161": "Internazionale",
        "1631": "Leicester City",
        "1633": "West Ham United",
        "1639": "Stoke City",
        "3219": "Benevento",
        "3782": "Saint-\u00c9tienne",
        "756": "Girona",
        "1644": "Watford",
        "2482": "Hoffenheim",
        "3173": "Cagliari",
        "3172": "Atalanta",
        "3176": "Fiorentina",
        "1623": "Everton",
        "1627": "West Bromwich Albion",
        "1625": "Manchester City",
        "1624": "Tottenham Hotspur",
        "2481": "Augsburg",
        "1628": "Crystal Palace",
        "19830": "Monaco",
        "2460": "Mainz 05",
        "3776": "Lille",
        "2462": "Eintracht Frankfurt",
        "1619": "Southampton",
        "2463": "K\u00f6ln",
        "1612": "Liverpool",
        "1610": "Chelsea",
        "1611": "Manchester United",
        "3185": "Torino",
        "3187": "Napoli",
        "677": "Deportivo La Coru\u00f1a",
        "2975": "RB Leipzig",
        "1609": "Arsenal",
        "3783": "Caen",
        "3780": "Toulouse",
        "3787": "Montpellier",
        "3785": "Guingamp",
        "3789": "Amiens SC",
        "3197": "Crotone",
        "3194": "Hellas Verona",
        "3193": "Genoa",
        "684": "Real Betis",
        "687": "Real Sociedad",
        "680": "Sevilla",
        "683": "M\u00e1laga",
        "682": "Villarreal",
        "14855": "Korea Republic",
        "10451": "Hungary",
        "4687": "Turkey",
        "14358": "Russia",
        "7047": "Sweden",
        "16276": "Tunisia",
        "6380": "Brazil",
        "3148": "Germany",
        "8731": "Albania",
        "11944": "Romania",
        "14622": "Ukraine",
        "16216": "Morocco",
        "14496": "Slovakia",
        "12430": "Colombia",
        "17929": "Panama",
        "8493": "Australia",
        "12274": "Argentina",
        "10962": "Northern Ireland",
        "9905": "Portugal",
        "5629": "Belgium",
        "7712": "Denmark",
        "15670": "Uruguay",
        "10682": "Wales",
        "16871": "Costa Rica",
        "2413": "England",
        "16129": "Egypt",
        "12913": "Japan",
        "10840": "Iran",
        "9109": "Austria",
        "7839": "Iceland",
        "9598": "Croatia",
        "15473": "Mexico",
        "8274": "Republic of Ireland",
        "11555": "Czech Republic",
        "19314": "Senegal",
        "3757": "Italy",
        "15594": "Peru",
        "4418": "France",
        "16521": "Saudi Arabia",
        "1598": "Spain",
        "17322": "Serbia",
        "6697": "Switzerland",
        "13869": "Poland",
        "16823": "Nigeria"
    }
    team_id = {
        "1613": "0",
        "692": "1",
        "691": "2",
        "696": "3",
        "695": "4",
        "3795": "5",
        "698": "6",
        "2454": "7",
        "1673": "8",
        "678": "9",
        "679": "10",
        "3766": "11",
        "3767": "12",
        "674": "13",
        "675": "14",
        "676": "15",
        "714": "16",
        "712": "17",
        "3204": "18",
        "10531": "19",
        "3771": "20",
        "3770": "21",
        "3775": "22",
        "3774": "23",
        "3779": "24",
        "701": "25",
        "1659": "26",
        "1651": "27",
        "2443": "28",
        "2446": "29",
        "2447": "30",
        "2444": "31",
        "2445": "32",
        "2449": "33",
        "3157": "34",
        "3799": "35",
        "3159": "36",
        "3158": "37",
        "3315": "38",
        "1646": "39",
        "3772": "40",
        "2455": "41",
        "3804": "42",
        "2457": "43",
        "2451": "44",
        "2450": "45",
        "2453": "46",
        "3166": "47",
        "3777": "48",
        "3164": "49",
        "3165": "50",
        "3162": "51",
        "3163": "52",
        "3161": "53",
        "1631": "54",
        "1633": "55",
        "1639": "56",
        "3219": "57",
        "3782": "58",
        "756": "59",
        "1644": "60",
        "2482": "61",
        "3173": "62",
        "3172": "63",
        "3176": "64",
        "1623": "65",
        "1627": "66",
        "1625": "67",
        "1624": "68",
        "2481": "69",
        "1628": "70",
        "19830": "71",
        "2460": "72",
        "3776": "73",
        "2462": "74",
        "1619": "75",
        "2463": "76",
        "1612": "77",
        "1610": "78",
        "1611": "79",
        "3185": "80",
        "3187": "81",
        "677": "82",
        "2975": "83",
        "1609": "84",
        "3783": "85",
        "3780": "86",
        "3787": "87",
        "3785": "88",
        "3789": "89",
        "3197": "90",
        "3194": "91",
        "3193": "92",
        "684": "93",
        "687": "94",
        "680": "95",
        "683": "96",
        "682": "97",
        "14855": "98",
        "10451": "99",
        "4687": "100",
        "14358": "101",
        "7047": "102",
        "16276": "103",
        "6380": "104",
        "3148": "105",
        "8731": "106",
        "11944": "107",
        "14622": "108",
        "16216": "109",
        "14496": "110",
        "12430": "111",
        "17929": "112",
        "8493": "113",
        "12274": "114",
        "10962": "115",
        "9905": "116",
        "5629": "117",
        "7712": "118",
        "15670": "119",
        "10682": "120",
        "16871": "121",
        "2413": "122",
        "16129": "123",
        "12913": "124",
        "10840": "125",
        "9109": "126",
        "7839": "127",
        "9598": "128",
        "15473": "129",
        "8274": "130",
        "11555": "131",
        "19314": "132",
        "3757": "133",
        "15594": "134",
        "4418": "135",
        "16521": "136",
        "1598": "137",
        "17322": "138",
        "6697": "139",
        "13869": "140",
        "16823": "141"
    }
    return team_name, team_id


def id_eng_dicts():
    wyId_id = {
        '1613': '0',
        '1673': '1',
        '10531': '2',
        '1659': '3',
        '1651': '4',
        '1646': '5',
        '1631': '6',
        '1633': '7',
        '1639': '8',
        '1644': '9',
        '1623': '10',
        '1627': '11',
        '1625': '12',
        '1624': '13',
        '1628': '14',
        '1619': '15',
        '1612': '16',
        '1610': '17',
        '1611': '18',
        '1609': '19'
    }
    wyId_name = {
        '1613': "Newcastle United",
        '1673': "Huddersfield Town",
        '10531': "Swansea City",
        '1659': "AFC Bournemouth",
        '1651': "Brighton & Hove Albion",
        '1646': "Burnley",
        '1631': "Leicester City",
        '1633': "West Ham United",
        '1639': "Stoke City",
        '1644': "Watford",
        '1623': "Everton",
        '1627': "West Bromwich Albion",
        '1625': "Manchester City",
        '1624': "Tottenham Hotspur",
        '1628': "Crystal Palace",
        '1619': "Southampton",
        '1612': "Liverpool",
        '1610': "Chelsea",
        '1611': "Manchester United",
        '1609': "Arsenal"
    }
    return wyId_name, wyId_id


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


def find_subtype(events, event_type, event_subtype):
    events_list = []
    for i in range(len(events)):
        if events[i]['eventName'] == event_type:
            if events[i]['subEventName'] == event_subtype:
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
