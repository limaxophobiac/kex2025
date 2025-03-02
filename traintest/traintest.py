from pathlib import Path
import numpy as np
import pysocialforce as psf


if __name__ == "__main__":
    # initial states, each entry is the position, velocity and goal of a pedestrian in the form of (px, py, vx, vy, gx, gy)
    initial_state = np.array(
        [
            [7.5, 6.5, 0.5, 0.5, 7.5, 6.5],
             [12.5, 6.5, 0.5, 0.5, 12.5, 6.5],
            [6.0, 5.0, 0.5, 0.5, 7.5, 6.5],
             [14.0, 5.0, 0.5, 0.5, 12.5, 6.5],
             [6.0, 6.5, 0.5, 0.5, 7.5, 6.5],
            [14.0, 6.5, 0.5, 0.5, 12.5, 6.5],
            [14.0, 9.0, 0.5, 0.5, 10.0, 7.0],
             [16.0, 8.0, 0.5, 0.5, 10.0, 7.0],
            [11.0, 8.0, 0.5, 0.5, 10.0, 7.0],
             [7.0, 9.0, 0.5, 0.5, 10.0, 7.0],
             [3.0, 8.0, 0.5, 0.5, 10.0, 7.0]
        ]
    )
    # social groups informoation is represented as lists of indices of the state array
    # list of linear obstacles given in the form of (x_min, x_max, y_min, y_max)
    # obs = [[-1, -1, -1, 11], [3, 3, -1, 11]]
    obs = [[0, 20, 10, 10], [0, 0, 7, 10], [20, 20, 7, 10], [11, 20, 7, 7], [0, 9, 7, 7]]
    # obs = None
    # initiate the simulator,
    s = psf.Simulator(
        initial_state,
        obstacles=obs,
        config_file=Path(__file__).resolve().parent.joinpath("traintest.toml"),
    )
    # update 80 steps
    
    s.step(30)
    print(s.peds.ped_states[-1])
    p = s.peds.ped_states[-1]

    p[6][5] = 0.0
    p[7][5] = 0.0
    p[8][5] = 0.0
    p[9][5] = 0.0
    p[10][5] = 0.0


    p[6][3] = -0.5
    p[7][3] = -0.5
    p[8][3] = -0.5
    p[9][3] = -0.5
    p[10][3] = -0.5

    p[0][3] = 0.5
    p[1][3] = 0.5
    p[2][3] = 0.5
    p[3][3] = 0.5
    p[4][3] = 0.5
    p[5][3] = 0.5

    p[0][4] = 10.0
    p[1][4] = 10.0
    p[2][4] = 10.0
    p[3][4] = 10.0
    p[4][4] = 10.0
    p[5][4] = 10.0

    p[0][5] = 10.0
    p[1][5] = 10.0
    p[2][5] = 10.0
    p[3][5] = 10.0
    p[4][5] = 10.0
    p[5][5] = 10.0




    s2 = psf.Simulator(
        p,
        obstacles=obs,
        config_file=Path(__file__).resolve().parent.joinpath("traintest.toml"),
    )
    with psf.plot.SceneVisualizer(s, "images/traintest1") as sv:
        sv.animate()

    s2.step(100)

    with psf.plot.SceneVisualizer(s2, "images/traintest2") as sv:
        sv.animate()
        #sv.plot()

