#! /usr/bin/env python

import os
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    """
    5 minutes execute a monitor
    """
    os.system("python ./redis-monitor.py --duration=60")
    #os.system("python ./redis-ping.py &")

os.system("python ./redis-live.py & ")
scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', minutes=5)
scheduler.start()
