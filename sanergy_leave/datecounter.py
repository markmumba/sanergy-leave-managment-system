from datetime import datetime, time

def dateDiffInSeconds(date1, date2):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return days

leaving_date = datetime.strptime('2019-10-16', '%Y-%m-%d')
now = datetime.strptime('2019-10-15', '%Y-%m-%d')

print ("%d days" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, leaving_date)))
