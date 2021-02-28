import datetime


def ExpandDate(date_input, format):
    date_string = str(date_input)
    data_processed = {}
    date_data = datetime.datetime.strptime(date_string, format)
    data_processed['dayOfWeek'] = date_data.weekday()
    data_processed['dayofMonth'] = date_data.strftime("%d")
    data_processed['dayofYear'] = date_data.timetuple().tm_yday
    data_processed['weekofYear'] = date_data.isocalendar()[1]
    data_processed['Month'] = date_data.strftime("%m")
    data_processed['Year'] = date_data.isocalendar()[0]
    data_processed['dayPosition'] = data_processed['dayofYear'] + 365*(data_processed['Year']-2010)

    return(data_processed)

