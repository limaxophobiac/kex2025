from os import stat
from pathlib import Path
import numpy as np
import pysocialforce as psf
import random
import math

trainY = 7.0
doorwith = 1.5
boardsplit = 0.5
pedradius = 0.25

#generates random sets of alighting and boarding passengers

def gen_random_rightside(count, boardcount, frontcount, remaining_passengers):
    passengers = []
    for i in range(frontcount):
        placed = False
        while (not placed):
            px = 9.5 - pedradius + random.random()
            py = trainY - pedradius*3 - random.random()*pedradius*i
            placed = True
            for j in passengers:
                if ((j[0] - px)**2 + (j[1] - py)**2 < pedradius**2):
                    placed = False
                    break
        passengers.append([px, py, 0, 0.1, px, py, 1.35])

    
    for i in range(boardcount-frontcount):
        px = 10.5 + (random.random()*pedradius if (i % 2 == 0) else pedradius*2 + random.random()*pedradius*0.5)
        py = trainY - pedradius*2 - i*pedradius - (pedradius if i % 2 == 1 else 0)
        vx = 0
        vy = 0.1
        gx = px
        gy = py

        passengers.append([px, py, vx, vy, gx, gy, 1.35])

    for i in range(count - boardcount):
        px = (10 + (i + 1)*pedradius) if (i % 2 == 0) else (10 - (i +1)*pedradius)
        py = trainY + 0.5 + random.random()*(10 - 1 - trainY)
        vx = 0.1 if (i % 2 == 1) else -0.1
        vy = 0
        gx = 10
        gy = trainY + pedradius*2
        passengers.append([px, py, vx, vy, gx, gy, 1.35])

    for i in range(remaining_passengers):
        placed = False
        while (not placed):
            px = 3 + random.random()*15
            py = trainY + 0.5 + (10 - trainY - 1)*random.random()
            placed = True
            for j in passengers:
                if ((j[0] - px)**2 + (j[1] - py)**2 < pedradius**2):
                    placed = False
                    break
        passengers.append([px, py, 0, 0, px, py, 0.5])


    return passengers 

def gen_random_leftright(count, boardcount, frontcount, remaining_passengers):
    passengers = []
    for i in range(frontcount):
        placed = False
        while (not placed):
            px = 9.5 - pedradius + random.random()
            py = trainY - pedradius*3 - random.random()*pedradius*i
            placed = True
            for j in passengers:
                if ((j[0] - px)**2 + (j[1] - py)**2 < pedradius**2):
                    placed = False
                    break
        passengers.append([px, py, 0, 0.1, px, py, 1.35])

    for i in range(boardcount-frontcount):
        px = (9.5 - boardsplit - pedradius if (i % 2 == 0) else 10 + boardsplit + pedradius) + random.random()*0.5
        py = trainY - pedradius - i*(pedradius)
        vx = 0
        vy = 0.1
        gx = px
        gy = py
        passengers.append([px, py, vx, vy, gx, gy, 1.35])

    for i in range(count - boardcount):
        px = (10 + (i + 1)*pedradius) if (i % 2 == 0) else (10 - (i +1)*pedradius)
        py = trainY + 0.5 + random.random()*(10 - 1 - trainY)
        vx = 0.1 if (i % 2 == 1) else -0.1
        vy = 0
        gx = 10
        gy = trainY + pedradius*2
        passengers.append([px, py, vx, vy, gx, gy, 1.35])

    for i in range(remaining_passengers):
        placed = False
        while (not placed):
            px = 3 + random.random()*15
            py = trainY + 0.5 + (10 - trainY - 1)*random.random()
            placed = True
            for j in passengers:
                if ((j[0] - px)**2 + (j[1] - py)**2 < pedradius**2):
                    placed = False
                    break
        passengers.append([px, py, 0, 0, px, py, 0.5])


    return passengers

def startAlighting(old, boardcount, rulebreaking):
    p = old
    for i in range(boardcount, len(old)):
        p[i][2] = 0
        p[i][3] = 0.1
        p[i][6] = 1.35
        p[i][5] = 5.5
        p[i][4] = 10

    for i in range(rulebreaking):
        p[i][2] = 0
        p[i][3] = 0.1
        p[i][6] = 1.35
    for i in range(rulebreaking):
        p[i][4] = 10
        p[i][5] = trainY + pedradius*6

    return p

def startBoarding(old, boardcount, rulebreaking):
    p = old
    
    for i in range(rulebreaking, boardcount):
        p[i][2] = 0
        p[i][3] = 0.1
        p[i][6] = 1.35
    for i in range(rulebreaking, boardcount):
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
    times = []
    if (boarding == 0):
        boarding = 1
    totalboard = 0
    totalalight = 0
    totaltime = 0
    failed = 0
    for i in range(len(dataset)):
        times.append(dataset[i][2])
        totalboard += dataset[i][0]
        totalalight += dataset[i][1]
        if (dataset[i][0] == boarding and dataset[i][1] == alighting):
            totaltime += dataset[i][2]
        else:
            failed += 1

    avg_time = 0
    if failed != len(dataset):
        avg_time = totaltime/(len(dataset) - failed)

    average_adjusted = 0
    times.sort()
    median = times[round(len(times)/2)]

    return [totalboard/(boarding * len(dataset)), totalalight/(alighting*len(dataset)), failed/len(dataset), avg_time, median]

if __name__ == "__main__":
    # initial states, each entry is the position, velocity and goal of a pedestrian in the form of (px, py, vx, vy, gx, gy)
    boarding = 10
    alighting = 10
    presteps = 20
    midsteps = 40
    poststeps = 300
    rulebreaking = 0
    max_passengers = 80
    waitpercent = 1.0
    rulebreaking = 0
    
    

    # list of linear obstacles given in the form of (x_min, x_max, y_min, y_max)
    # obs = [[-1, -1, -1, 11], [3, 3, -1, 11]]
    obs = [[0, 20, 10, 10], [0, 0, trainY, 10], [20, 20, trainY, 10], [10 + (doorwith/2), 20, trainY, trainY], [0, 10 - (doorwith/2), trainY, trainY],
           [10 + (doorwith/2), 10 + (doorwith/2), trainY, trainY + 0.5], [10 + (doorwith/2), 20, trainY + 0.5, trainY + 0.5],
           [20, 20, trainY, trainY + 0.5], [10 - (doorwith/2), 10 - (doorwith/2), trainY, trainY + 0.5], [0, 10 - (doorwith/2), trainY + 0.5, trainY + 0.5],
           [0, 0, trainY, trainY + 0.5], [20, 20, 10, 9.5], [10 - (doorwith/2), 10 - (doorwith/2), 10, 9.5], [0, 10 - (doorwith/2), 9.5, 9.5],
           [10 + (doorwith/2), 20, 9.5, 9.5], [10 + (doorwith/2), 10 + (doorwith/2), 10.0, 9.5]]
    # obs = None
    # initiate the simulator,
    for p in range(5):
        remaining_passengers = round(max_passengers*0.2*p)
        arrDeadlock = []
        arrTime = []
        waitpercent = 1.0
        
        for sim in range(6):
            stats = []
            
            for i in range(150):
                passengers2 = gen_random_leftright(boarding + alighting, boarding, rulebreaking, remaining_passengers)
                initial_state = np.array(passengers2)
                groups = []
                for i in range(boarding + alighting):
                    groups.append([i])

                s = psf.Simulator(
                    initial_state,
                    groups = groups,
                    obstacles=obs,
                    config_file=Path(__file__).resolve().parent.joinpath("traintest.toml"),
                )

                collisioncount = 0
                for i in range(presteps):
                    s.step(1)

                actualSteps = 0
                alighted = 0
                boarded = 0
                p1 = startAlighting(s.peds.ped_states[-1], boarding, rulebreaking)
                
                s.peds.update(p1, s.peds.groups)
                while(alighted < alighting*waitpercent and actualSteps < 150):
                    actualSteps += 1
                    s.step(1)
                    changed = False
                    for j in range (boarding, len(s.peds.ped_states[-1])):
                        if s.peds.ped_states[-1][j][1] < trainY and s.peds.ped_states[-1][j][5] == 5.5:
                            s.peds.ped_states[-1][j][5] = -5
                            s.peds.ped_states[-1][j][6] = 1.35
                            changed = True
                            alighted += 1
                    for j in range (rulebreaking):
                        if s.peds.ped_states[-1][j][1] > trainY + pedradius and s.peds.ped_states[-1][j][4] == 10:
                            s.peds.ped_states[-1][j][5] = 9
                            s.peds.ped_states[-1][j][4] = (7 if j % 2 == 0 else 13)
                            changed = True
                            boarded += 1
                    if changed:
                        s.peds.update(s.peds.ped_states[-1], s.peds.groups)

                p2 = startBoarding(s.peds.ped_states[-1], boarding, rulebreaking)
                s.peds.update(p2, s.peds.groups)
                
                for i in range(poststeps):
                    actualSteps += 1
                    #print(str(s.peds.ped_states[-1][9][0]) + " " +  str(s.peds.ped_states[-1][9][1]))
                    s.step(1)
                    changed = False
                    for j in range (boarding, len(s.peds.ped_states[-1])):
                        if s.peds.ped_states[-1][j][1] < trainY and s.peds.ped_states[-1][j][5] == 5.5:
                            s.peds.ped_states[-1][j][5] = -5
                            changed = True
                            alighted += 1
                    for j in range (boarding):
                        if s.peds.ped_states[-1][j][1] > trainY + pedradius and s.peds.ped_states[-1][j][4] == 10:
                            s.peds.ped_states[-1][j][5] = 9
                            s.peds.ped_states[-1][j][4] = (7 if j % 2 == 0 else 13)
                            changed = True
                            boarded += 1
                    if changed:
                        s.peds.update(s.peds.ped_states[-1], s.peds.groups)

            #        for j in range(0, len(s.peds.ped_states[-1])):
            #            for k in range(len(s.peds.ped_states[-1])):
            #               if (j == k):
        #                     continue
        #                  if (((s.peds.ped_states[-1][j][0] - s.peds.ped_states[-1][k][0])**2 + (s.peds.ped_states[-1][j][1] - s.peds.ped_states[-1][k][1])**2) < 0.2**2):
        #                       collisioncount += 1

                    if (boarded == boarding and alighted == alighting):
                        break
        #      print("collisions " + str(collisioncount))

                data = get_end_data(s.peds.ped_states[-1], boarding, actualSteps/5)

                print("Boarded: " + str(data[0]) + " Alighted: " + str(data[1]) + " in " + str(data[2]) + " seconds")
                stats.append(data)
                with psf.plot.SceneVisualizer(s, "images/traintest" + str(boarding + alighting) + "right side") as sv:
                   sv.animate()

            statistics = get_statistics(stats, boarding, alighting, 60)
            print("boarding: " + str(boarding) + " alighting: " + str(alighting) + " Percentage Boarded: " + str(round(statistics[0]*100, 2)) + " Percentage alighted: " + str(round(statistics[1]*100,2)) + " average time: " + str(round(statistics[3], 2)) + " seconds" + " failed: " + str(round(statistics[2], 2)) + " waiting for " + str(round(waitpercent*100, 2)) + " of passengers before board, remaining in cart: " + str(remaining_passengers) +" median time: " + str(round(statistics[4],2)) + " rulebreakers: " + str(rulebreaking))
            arrDeadlock.append(round(statistics[2], 2))
            arrTime.append(round(statistics[4],2))
            waitpercent -= 0.2

        print("deadlockarray: " + str(arrDeadlock))
        print("timearray: " + str(arrTime))
            

        


