
import data_handling as dh
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import seaborn as sns


def generate_id_dicts(teams):
    for i in range(len(teams)):
        """if teams[i]['area']['name'] == "England":
            print(str(teams[i]['wyId']) + ": \"" + teams[i]['name'] +"\",")
        if teams[i]['area']['name'] == "Wales":
            print(str(teams[i]['wyId']) + ": \"" + teams[i]['name'] +"\",")"""
    for i in range(len(teams)):
        # print("\"" + str(teams[i]['wyId']) + "\": \"" + teams[i]['name'] + "\",")
        print("\"" + str(teams[i]['wyId']) + "\": \"" + str(i) + "\",")


def generate_xg_pos(shots):
    # matches, events, players, teams = dh.import_all()
    # matches, events, players, teams = dh.import_data("England")

    # shots = dh.find_all(events, "Shot")
    # print(shots)

    shots_count = np.zeros((104, 68), dtype=int)
    scored_count = np.zeros((104, 68), dtype=int)

    xg = np.zeros((104, 68))

    print("Processing shots...")
    for i in range(len(shots)):
        x_temp = shots[i]['positions'][0]['x'] * 1.04
        y_temp = shots[i]['positions'][0]['y'] * 0.68

        x, y = math.floor(x_temp) - 1, math.floor(y_temp) - 1

        shots_count[x][y] += 1
        if shots[i]['tags'][0]['id'] == 101:
            scored_count[x][y] += 1

    for i in range(104):
        for j in range(68):
            if shots_count[i][j] == 0:
                xg[i][j] = 0
            else:
                xg[i][j] = scored_count[i][j]/shots_count[i][j]
                # outlier removal
                if xg[i][j] == 1 and i < 99:
                    xg[i][j] = 0

    # print("Saving xg table...")
    np.save("models/xg_pos.npy", xg, allow_pickle=True)

    return xg


def plot_xg(xg):
    fig, ax = plt.subplots(figsize=(10.4, 6.8))
    fig, ax = dh.create_pitch(fig, ax)

    ax.imshow(np.transpose(xg), cmap='Reds')
    ax.set_xlim(0, 104)
    ax.set_ylim(0, 68)
    ax.set_title('xG by Shot Location')
    plt.show()


def count_scored(events):
    num_events = len(events)
    events_scored = 0
    for i in range(num_events):
        if events[i]['tags'][0]['id'] == 101:
            events_scored += 1
    return num_events, events_scored, events_scored/num_events


def save_pens_dfks(xGpen, xGdfk):
    xGfk = np.array([xGpen, xGdfk])
    np.save("models/xGfk.npy", xGfk, allow_pickle=True)


def reshape_xG(xG):
    xG_x, xG_y = [], []
    for i in range(104):
        for j in range(68):
            for k in range(math.floor(100*xG[i][j])):
                xG_x.append(i+0.5)
                xG_y.append(j+0.5)
    return xG_x, xG_y


def generate_xG_values(shots, pens, DFKs):
    xG = generate_xg_pos(shots)

    num_pens, pens_scored, xGpen = count_scored(pens)
    num_DFKs, DFKs_scored, xGdfk = count_scored(DFKs)
    save_pens_dfks(xGpen, xGdfk)

    return xG, xGpen, xGdfk


def get_shots(events):
    shots = dh.find_all(events, 'Shot')
    pens = dh.find_subtype(events, 'Free Kick', 'Penalty')
    DFKs = dh.find_subtype(events, 'Free Kick', 'Free kick shot')
    return shots, pens, DFKs


def create_xG_cont(xG, upper_bound=1):
    xG_x, xG_y = reshape_xG(xG)

    xG_kern = gaussian_kde([xG_x, xG_y])
    xG_cont = np.zeros((104, 68))

    for i in range(104):
        for j in range(68):
            xG_cont[i][j] = xG_kern([i, j])
    xG_cont = (upper_bound / np.amax(xG_cont)) * xG_cont

    np.save("models/xG_cont.npy", xG_cont)

    return xG_cont


def plot_xG_G(x_plot, y_plot):
    fig, ax = plt.subplots()
    ax.scatter(x_plot, y_plot)

    x_str = np.linspace(0, 110, 110)
    y_str = np.linspace(0, 110, 110)

    ax.plot(x_str, y_str, 'r')

    ax.set_title('xG vs Goals Scored')

    ax.set_xlabel('Goals')
    ax.set_ylabel('xG')

    return fig, ax


def evaluate_xG_metric(shots, team_name_dict, team_id_dict, xG_scale=1.0):
    teams_goals = np.zeros(len(team_name_dict))
    teams_xg = np.zeros(len(team_name_dict))
    teams_names = np.zeros(len(team_name_dict), dtype=object)

    for i in range(len(shots)):
        wyId = str(shots[i]['teamId'])
        temp_id = int(team_id_dict[wyId])
        teams_names[temp_id] = team_name_dict[wyId]

        x_temp = shots[i]['positions'][0]['x'] * 1.04
        y_temp = shots[i]['positions'][0]['y'] * 0.68

        x, y = math.floor(x_temp) - 1, math.floor(y_temp) - 1

        teams_xg[temp_id] += xG_scale * xG[x][y]
        if shots[i]['tags'][0]['id'] == 101:
            teams_goals[temp_id] += 1

    error = 0
    oe_total = 0
    print()

    x_plot, y_plot = [], []
    for i in range(len(team_name_dict)):
        if teams_xg[i] != 0:
            temp_est = teams_goals[i] / teams_xg[i]
        else:
            temp_est = 0
        oe_total += temp_est

        x_plot.append(teams_goals[i])
        y_plot.append(teams_xg[i])

        print(teams_names[i] + " - xG: " + str(teams_xg[i]) + ", G: " + str(teams_goals[i]) + ", O/E: " +
              str(temp_est))
        error += abs(teams_xg[i] - teams_goals[i])

    print("\nError: " + str(error))
    oe_average = oe_total / len(team_name_dict)
    print("Overestimate avg: " + str(oe_average))

    fig, ax = plot_xG_G(x_plot, y_plot)
    plt.show()
    return error


if __name__ == "__main__":

    xG = np.load("models/xg_cont.npy")
    xGfk = np.load("models/xGfk.npy")

    # JUST EPL DATA
    matches, events, players, teams = dh.import_data("England")
    team_name_dict, team_id_dict = dh.id_eng_dicts()

    # ALL COMPETITIONS DATA
    # matches, events, players, teams = dh.import_all()
    # team_name_dict, team_id_dict = dh.team_id_dicts()

    # GENERATE XG MATRICES
    # xG, xGpen, xGdfk = generate_xG_values(shots, pens DFKs)
    # xG_cont = create_xG_cont(xG)

    shots, pens, DFKs = get_shots(events)

    evaluate_xG_metric(shots, team_name_dict, team_id_dict, 0.6)
