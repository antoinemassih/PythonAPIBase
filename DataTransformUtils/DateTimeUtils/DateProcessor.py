import datetime


def ExpandDate(date_data):
    data_processed = {}
    data_processed['date'] = date_data
    data_processed['dayOfWeek'] = date_data.weekday()
    data_processed['dayOfMonth'] = date_data.strftime("%d")
    data_processed['dayOfYear'] = date_data.timetuple().tm_yday
    data_processed['weekOfYear'] = date_data.isocalendar()[1]
    data_processed['Month'] = date_data.strftime("%m")
    data_processed['Year'] = date_data.isocalendar()[0]
    data_processed['dayPosition'] = data_processed['dayOfYear'] + 365 * (data_processed['Year'] - 2010)

    return data_processed


def getRange(day_of_year1, day_of_year2):
    if day_of_year1 == day_of_year2:
        the_range = [day_of_year2]
    else:
        temp_range = range(day_of_year1, day_of_year2)
        the_range = list(temp_range)
    return the_range
