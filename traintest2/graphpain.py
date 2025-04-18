import matplotlib.pyplot as plt
import numpy as np
import math

X = np.arange(0, math.pi*2, 0.05)

y = np.sin(X)
z = np.cos(X)



all_wait_b15_a15_r0_t = [17.0, 15.0, 15.2, 16.0, 16.2, 16.2]
all_wait_b15_a15_r16_t = [21.2, 18.6, 18.2, 19.0, 18.8, 18.8]
all_wait_b15_a15_r32_t = [26.6, 23.0, 22.6, 22.4, 22.8, 23.2]
all_wait_b15_a15_r48_t = [35.2, 30.4, 28.2, 29.8, 30.6, 30.6]
all_wait_b15_a15_r64_t = [48.6, 45.0, 42.4, 43.2, 44.4, 44.4]

all_wait_b15_a15_r0_d = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
all_wait_b15_a15_r16_d = [0.0, 0.0, 0.01, 0.01, 0.01, 0.01]
all_wait_b15_a15_r32_d = [0.0, 0.04, 0.05, 0.06, 0.11, 0.09]
all_wait_b15_a15_r48_d = [0.15, 0.15, 0.21, 0.37, 0.44, 0.49]
all_wait_b15_a15_r64_d = [0.43, 0.48, 0.58, 0.71, 0.81, 0.87]

all_wait_b5_a5_r0_t = []
all_wait_b5_a5_r16_t = []
all_wait_b5_a5_r32_t = []
all_wait_b5_a5_r48_t = []
all_wait_b15_a15_r64_t = []

all_wait_b5_a5_r0_d = []
all_wait_b5_a5_r16_d = []
all_wait_b5_a5_r32_d = []
all_wait_b5_a5_r48_d = []
all_wait_b15_a15_r64_d = []

all_wait_b10_a10_r0 = []
all_wait_b10_a10_r16 = []
all_wait_b10_a10_r32 = []
all_wait_b10_a10_r48 = []
all_wait_b10_a10_r64 = []

plt.plot(X, y, color='r', label='sin')
plt.plot(X, z, color='g', label='cos')

plt.xlabel("Angle")
plt.ylabel("Magnitude")
plt.title("sine and cosine")

plt.legend()
plt.show()