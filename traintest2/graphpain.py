import matplotlib.pyplot as plt
import numpy as np
import math

X = np.arange(0, math.pi*2, 0.05)

y = np.sin(X)
z = np.cos(X)

waited_for = [100, 80, 60, 40, 20, 0]

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

all_wait_b5_a5_r0_t = [6.6, 6.6, 6.4, 6.4, 6.0, 6.0]
all_wait_b5_a5_r16_t = [7.2, 7.0, 7.0, 6.8, 7.0, 6.6]
all_wait_b5_a5_r32_t = [8.2, 8.0, 8.0, 7.8, 7.6, 7.4]
all_wait_b5_a5_r48_t = [10.8, 9.6, 9.6, 9.4, 9.2, 9.2]
all_wait_b5_a5_r64_t = [13.8, 11.6, 11.4, 11.2, 11.6, 11.6]

all_wait_b5_a5_r0_d = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
all_wait_b5_a5_r16_d = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
all_wait_b5_a5_r32_d = [0.0, 0.01, 0.0, 0.01, 0.01, 0.0]
all_wait_b5_a5_r48_d = [0.03, 0.03, 0.03, 0.03, 0.03, 0.02]
all_wait_b5_a5_r64_d = [0.07, 0.14, 0.13, 0.11, 0.13, 0.19]

all_wait_b10_a10_r0_t = [11.2, 10.0, 9.8, 9.6, 9.8, 9.6]
all_wait_b10_a10_r16_t = [13.4, 11.6, 11.2, 10.8, 10.8, 11.0]
all_wait_b10_a10_r32_t = [17.2, 13.8, 13.4, 13.2, 13.6, 13.2]
all_wait_b10_a10_r48_t = [22.6, 19.8, 18.2, 17.2, 18.0, 17.6]
all_wait_b10_a10_r64_t = [35.4, 25.2, 25.8, 24.0, 26.2, 26.6]

all_wait_b10_a10_r0_d = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
all_wait_b10_a10_r16_d = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
all_wait_b10_a10_r32_d = [0.01, 0.01, 0.03, 0.03, 0.03, 0.03]
all_wait_b10_a10_r48_d = [0.04, 0.15, 0.15, 0.15, 0.15, 0.19]
all_wait_b10_a10_r64_d = [0.3, 0.35, 0.38, 0.45, 0.45, 0.49]

all_wait_b15_a15_r0_t = [17.0, 15.0, 15.2, 16.0, 16.2, 16.2]
all_wait_b15_a15_r16_t = [21.2, 18.6, 18.2, 19.0, 18.8, 18.8]
all_wait_b15_a15_r32_t = [26.6, 23.0, 22.6, 22.4, 22.8, 23.2]
all_wait_b15_a15_r48_t = [35.2, 30.4, 28.2, 29.8, 30.6, 30.6]
all_wait_b15_a15_r64_t = [48.6, 45.0, 42.4, 43.2, 44.4, 44.4]

rulebreaking = [0, 2, 4, 6, 8, 10]

b15_a15_r0_rb0_t = [15.0, 15.8, 15.6, 15.6, 15.4, 15.0]
b15_a15_r0_rb0_d = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

b15_a15_r16_0rb_t = [18.6, 18.6, 18.8, 18.8, 18.2, 18.6]
b15_a15_r16_0rb_d = [0.01, 0.01, 0.01, 0.01, 0.02, 0.03]

b15_a15_r32_rb0_t = [22.6, 23.0, 24.2, 23.2, 23.8, 23.2]
b15_a15_r32_rb0_d = [0.06, 0.04, 0.07, 0.09, 0.13, 0.23]

b15_a15_r48_rb0_t = [28.6, 29.6, 30.8, 31.4, 31.6, 31.8]
b15_a15_r48_rb0_d = [0.26, 0.21, 0.27, 0.32, 0.51, 0.63]

b15_a15_r64_rb0_t = [40.4, 45.6, 46.4, 42.8, 48.4, 50.6]
b15_a15_r64_rb0_d = [0.6, 0.58, 0.69, 0.73, 0.86, 0.91]

b10_a10_r0_rb_t = [9.8, 9.4, 9.2, 9.2, 8.8, 8.6]
b10_a10_r0_rb_d = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

b10_a10_r16_rb_t = [11.2, 10.6, 10.8, 10.4, 10.6, 11.0]
b10_a10_r16_rb_d = [0.0, 0.0, 0.0, 0.01, 0.01, 0.01]

b10_a10_r32_rb_t = [13.6, 14.0, 14.2, 13.2, 13.8, 13.4]
b10_a10_r32_rb_d = [0.01, 0.01, 0.01, 0.04, 0.02, 0.05]

b10_a10_r48_rb_t = [17.6, 18.8, 19.4, 17.8, 17.8, 20.6]
b10_a10_r48_rb_d = [0.16, 0.18, 0.19, 0.21, 0.17, 0.21]

b10_a10_r64_rb_t = [25.6, 26.6, 27.8, 26.6, 27.8, 29.4]
b10_a10_r64_rb_d = [0.31, 0.42, 0.53, 0.51, 0.53, 0.58]

#plt.plot(rulebreaking, b10_a10_r0_rb_d, '.', label= '0r')
#plt.plot(rulebreaking, b10_a10_r16_rb_d, '.', label= '16r')
#plt.plot(rulebreaking, b10_a10_r32_rb_d, '.', label= '32r')
#plt.plot(rulebreaking, b10_a10_r48_rb_d, '.', label= '48r')
#plt.plot(rulebreaking, b10_a10_r64_rb_d, '.', label= '64r')

xval = np.linspace(rulebreaking[0], rulebreaking[-1], num=100)

lin0 = np.polyfit(rulebreaking, b10_a10_r0_rb_d, 3)
poly0 = np.polyval(lin0, xval)

lin16 = np.polyfit(rulebreaking, b10_a10_r16_rb_d, 3)
poly16 = np.polyval(lin16, xval)

lin32 = np.polyfit(rulebreaking, b10_a10_r32_rb_d, 3)
poly32 = np.polyval(lin32, xval)

lin48 = np.polyfit(rulebreaking, b10_a10_r48_rb_d, 3)
poly48 = np.polyval(lin48, xval)

lin64 = np.polyfit(rulebreaking, b10_a10_r64_rb_d, 3)
poly64 = np.polyval(lin64, xval)

plt.plot(xval, poly0, '-', label='0rPoly')
plt.plot(xval, poly16, '-', label='16rPoly')
plt.plot(xval, poly32, '-', label='32rPoly')
plt.plot(xval, poly48, '-', label='48rPoly')
plt.plot(xval, poly64, '-', label='64rPoly')

plt.xlabel("rule breakers")
plt.ylabel("chance of deadlock")

plt.legend()
plt.show()