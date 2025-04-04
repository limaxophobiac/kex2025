from os import stat
from pathlib import Path
import numpy as np
import pysocialforce as psf
import random

trainY = 7.2
doorwith = 1.5
boardsplit = 0.5
pedradius = 0.3

#generates random sets of alighting and boarding passengers
def gen_random_leftright(count, boardcount):
    passengers = []
    for i in range(boardcount):
        px = (9.5 - boardsplit - pedradius if (i % 2 == 0) else 10 + boardsplit + pedradius) + random.random()*0.5
        py = trainY - pedradius - i*(pedradius)
        vx = 0
        vy = 1
        gx = px
        gy = py
        passengers.append([px, py, vx, vy, gx, gy])

    for i in range(count - boardcount):
        px = (10 + (i + 1)*pedradius) if (i % 2 == 0) else (10 - (i +1)*pedradius)
        py = trainY + pedradius + random.random()*(10 - pedradius - trainY)
        vx = 1 if (i % 2 == 1) else -1
        vy = 0
        gx = 10
        gy = trainY + pedradius*2
        passengers.append([px, py, vx, vy, gx, gy])

    return passengers

def startAlighting(old, boardcount):
    p = old
    for i in range(boardcount, len(old)):
        p[i][2] = 0
        p[i][3] = -1
        p[i][6] = 1.35
        p[i][5] = 5

    return p

def startBoarding(old, boardcount):
    p = old
    
    for i in range(boardcount):
        p[i][2] = 0
        p[i][3] = 1
        p[i][6] = 1.35
    for i in range(boardcount):
        p[i][4] = 10
        p[i][5] = trainY + pedradius*6

    return p

def get_end_data(state, boardcount, step):
    boardsuccess = 0
    alightsuccess = 0
    for i in range(boardcount):
        if state[i][1] > trainY:
            boardsuccess += 1
    for i in range(boardcount, len(state)):
        if state[i][1] < trainY:
            alightsuccess += 1

    return [boardsuccess, alightsuccess, step]

def get_statistics(dataset, boarding, alighting, maxtime):
    totalboard = 0
    totalalight = 0
    totaltime = 0
    failed = 0
    for i in dataset:
        totalboard += dataset[i][0]
        totalalight += dataset[i][1]
        if dataset[i][2] != maxtime:
            totaltime += dataset[i][2]
        else:
            failed += 1

    avg_time = 0
    if failed != len(dataset):
        avg_time = totaltime/(len(dataset) - failed)

    return [totalboard/(boarding * len(dataset)), totalalight/(alighting*len(dataset)), failed/len(dataset), avg_time]

if __name__ == "__main__":
    # initial states, each entry is the position, velocity and goal of a pedestrian in the form of (px, py, vx, vy, gx, gy)
    boarding = 16
    alighting = 14
    presteps = 15
    midsteps = 20
    poststeps = 50

    passengers2 = gen_random_leftright(boarding + alighting, boarding)
    initial_state = np.array(passengers2)

    # list of linear obstacles given in the form of (x_min, x_max, y_min, y_max)
    # obs = [[-1, -1, -1, 11], [3, 3, -1, 11]]
    obs = [[0, 20, 10, 10], [0, 0, trainY, 10], [20, 20, trainY, 10], [10 + (doorwith/2), 20, trainY, trainY], [0, 10 - (doorwith/2), trainY, trainY]]
    # obs = None
    # initiate the simulator,
    s = psf.Simulator(
        initial_state,
        obstacles=obs,
        config_file=Path(__file__).resolve().parent.joinpath("traintest.toml"),
    )

    s.step(presteps)

    p1 = startAlighting(s.peds.ped_states[-1], boarding)
    s.peds.update(p1, s.peds.groups)
    for i in range(midsteps):
        s.step(1)
        if (i % 3 == 0):
            changed = False
            for j in range (boarding, len(s.peds.ped_states[-1])):
                if s.peds.ped_states[-1][j][1] < 7 and s.peds.ped_states[-1][j][5] == 5:
                    s.peds.ped_states[-1][j][5] = -5
                    changed = True
            if changed:
                s.peds.update(s.peds.ped_states[-1], s.peds.groups)

    p2 = startBoarding(s.peds.ped_states[-1], boarding)
    s.peds.update(p2, s.peds.groups)

    for i in range(poststeps):
        #print(str(s.peds.ped_states[-1][9][0]) + " " +  str(s.peds.ped_states[-1][9][1]))
        s.step(1)
        if (i % 3 == 0):
            changed = False
            for j in range (boarding, len(s.peds.ped_states[-1])):
                if s.peds.ped_states[-1][j][1] < 7 and s.peds.ped_states[-1][j][5] == 5:
                    s.peds.ped_states[-1][j][5] = -5
                    changed = True
            for j in range (boarding):
                if s.peds.ped_states[-1][j][1] > trainY + pedradius and s.peds.ped_states[-1][j][4] == 10:
                    s.peds.ped_states[-1][j][5] = 9
                    s.peds.ped_states[-1][j][4] = (6 if j % 2 == 0 else 14)
                    changed = True
            if changed:
                s.peds.update(s.peds.ped_states[-1], s.peds.groups)

    data = get_end_data(s.peds.ped_states[-1], boarding, (midsteps + poststeps)/2)

    print("Boarded: " + str(data[0]) + " Alighted: " + str(data[1]) + " in " + str(data[2]) + " seconds")
    #with psf.plot.SceneVisualizer(s, "images/traintest" + str(boarding + alighting)) as sv:
     # sv.animate()

