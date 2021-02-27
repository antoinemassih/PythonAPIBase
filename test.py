import datetime
import time


def getDateRangeFromWeek(p_year,p_week):

    firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)
    return firstdayofweek, lastdayofweek


#Call function to get dates range
firstdate, lastdate =  getDateRangeFromWeek('2019','2')

print('print function ',firstdate.timetuple().tm_yday,' ', lastdate.timetuple().tm_yday)