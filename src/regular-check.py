from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    """
    5 minutes execute a monitor
    """
    # duration = 60
    # monitor = RedisMonitor()
    # monitor.run(duration)
    execfile("python ./redis-monitor.py --duration=60")


scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', minutes=5)
scheduler.start()
