
import data_handling as dh
import numpy as np
import math
import matplotlib.pyplot as plt


def generate_xg_loc():
    matches, events, players, teams = dh.import_all()
    # matches, events, players, teams = dh.import_data("England")

    shots = dh.find_all(events, "Shot")
    print(shots)

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
            scored_count += 1

    for i in range(104):
        for j in range(68):
            xg[i][j] = shots_count[i][j] / scored_count[i][j]

    # print("Saving xg table...")
    np.save("models/xg_pos_allcomps.npy", xg, allow_pickle=True)

    return xg


def plot_xg(xg):
    fig, ax = plt.subplots(figsize=(10.4, 6.8))
    fig, ax = dh.create_pitch(fig, ax)

    ax.imshow(np.transpose(xg), cmap='Reds')
    ax.set_xlim(0, 104)
    ax.set_ylim(0, 68)
    ax.set_title('xG by Shot Location')
    plt.show()


if __name__ == "__main__":
    xg = np.load("models/xg_pos_allcomps.npy")
