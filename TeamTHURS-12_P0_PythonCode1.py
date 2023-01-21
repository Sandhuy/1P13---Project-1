import sys
sys.path.append('/...')
import time
from Common_Libraries.p0_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim ():
    try:
        my_qbot.ping()
    except Exception as error_update_sim:
        print (error_update_sim)


speed = 0.1 # 1n m/s
my_qbot = qbot(speed)
update_thread=repeating_timer(2, update_sim)

#print("Im up")
#my_qbot.rotate(-90)
#my_qbot.forward(2)
#my_qbot.rotate(360)

start_time=time.time()
#Time-Controlled Code
my_qbot.forward(2.29)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(4.58)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(1.3355)
my_qbot.rotate(-11.05)
my_qbot.rotate(-11.05)
my_qbot.forward(2.29)
stop_time=time.time()
print(stop_time - start_time)   
print("FULL ROTATION YAAAAAAY")
