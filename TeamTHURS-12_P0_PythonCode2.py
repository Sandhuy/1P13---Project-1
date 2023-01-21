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

start_time=time.time()
#Distance-Controlled

my_qbot.travel_forward(0.5)
my_qbot.rotate(-45.05)
my_qbot.travel_forward(0.5)
my_qbot.rotate(-40.05)
my_qbot.travel_forward(0.35)
my_qbot.rotate(-60.05)
my_qbot.travel_forward(0.35)
my_qbot.rotate(-30.05)
my_qbot.travel_forward(0.45)
my_qbot.rotate(-30.05)
my_qbot.travel_forward(0.55)
my_qbot.rotate(-45.05)
my_qbot.travel_forward(0.35)
my_qbot.rotate(-60.05)
my_qbot.travel_forward(0.25)
my_qbot.rotate(-45.05)
my_qbot.travel_forward(0.4)
my_qbot.rotate(-30.05)
my_qbot.travel_forward(0.85)
stop_time=time.time()
print(stop_time - start_time) 
