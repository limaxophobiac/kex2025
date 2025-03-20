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
        px = (9.5 - boardsplit - pedradius if (i % 2 == 0) else 10 + boardsplit + pedradius) + random()*0.5
    return passengers

def changeGoals(old, boardcount):
    p = old
    
    for i in range(boardcount):
        p[i][6] = 0.5
    for i in range(boardcount):
        p[i][4] = 10
        p[i][5] = 9.8


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
    passengers =         [
            [7.5, 6.5, 0.5, 0.5, 7.5, 6.5],
             [12.5, 6.5, 0.5, 0.5, 12.5, 6.5],
            [6.0, 5.0, 0.5, 0.5, 7.5, 6.5],
             [14.0, 5.0, 0.5, 0.5, 12.5, 6.5],
             [6.0, 6.5, 0.5, 0.5, 7.5, 6.5],
            [13.0, 6.5, 0.5, 0.5, 12.5, 6.5],
            [11.0, 9.0, 0.5, 0.5, 10.0, 0.0],
             [9.0, 8.0, 0.5, 0.5, 10.0, 0.0],
            [11.0, 8.0, 0.5, 0.5, 10.0, 0.0],
             [10.0, 9.0, 0.5, 0.5, 10.0, 0.0],
             [8.0, 8.0, 0.5, 0.5, 10.0, 0.0]
        ]
    initial_state = np.array(passengers)

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
    # update 80 steps
    s.step(20)

    

    for i in range(20):
        print(str(s.peds.ped_states[-1][9][0]) + " " +  str(s.peds.ped_states[-1][9][1]))
        s.step(1)

    print("changing------------------")
    p = changeGoals(s.peds.ped_states[-1], 6)
    s.peds.update(p, s.peds.groups)

    for i in range(80):
        print(str(s.peds.ped_states[-1][9][0]) + " " +  str(s.peds.ped_states[-1][9][1]))
        s.step(1)

    data = get_end_data(s.peds.ped_states[-1], 6, 110)

    print("Boarded: " + str(data[0]) + " Alighted: " + str(data[1]) + " in " + str(data[2]) + " steps")
    #with psf.plot.SceneVisualizer(s, "images/traintest" + str(5)) as sv:
     #   sv.animate()

