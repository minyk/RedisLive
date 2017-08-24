#! /usr/bin/env python

from apscheduler.schedulers.blocking import BlockingScheduler
import os

def job():
    """
    5 minutes execute a monitor
    """
    # duration = 60
    # monitor = RedisMonitor()
    # monitor.run(duration)
    os.system("python ./redis-monitor.py --duration=60")

os.system("python ./redis-live.py & ")
scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', minutes=5)
scheduler.start()
