from datetime import datetime, time
from .models import Leave
from time import sleep


def dateDiffInSeconds(date1, date2):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

req = datetime.strptime('2019-03-08 10:00:30', '%Y-%m-%d %H:%M:%S')
now = datetime.now()

while req>now:
    print("%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req)))
    sleep(1)
    now = datetime.now()

print("Done")
