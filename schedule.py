from apscheduler.schedulers.blocking import BlockingScheduler
from parcer import currentWeatherParcer
from datetime import datetime
dateToSTR = datetime.now()
now = str(dateToSTR)

def parsSchedule():
    if __name__ == '__main__':
        currentWeatherParcer.pars()
    print('Cycle done' + now)
scheduler = BlockingScheduler()
scheduler.add_job(parsSchedule, 'cron', month='*', day='*', hour='9')
scheduler.start()
