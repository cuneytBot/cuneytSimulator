from cuneyd_bot import CuneydBot
import time, random

sim_1 = CuneydBot(d=0.1,ID=1)

V= 0.1
W = 0
t_passed = 0
while True:
    sim_1.set_velocities(V=V,W=W)
    V += (random.random() - 0.5)/20
    W += (random.random() - 0.5)/10000
    sim_1.diff_drive_overtime(0.5)
    sim_1.post_position()
    sim_1.post_err_position()
    time.sleep(0.025)
    t_passed += 0.5
    print t_passed

