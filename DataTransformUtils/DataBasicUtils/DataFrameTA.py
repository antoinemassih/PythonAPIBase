import pandas as pd
import DataTransformUtils.DateTimeUtils.DateProcessor as dateProcessor
import numpy as np
from time import strptime

pd.options.mode.chained_assignment = None  # default='warn'

class DataFrameTA:
    data = pd.DataFrame()
    data_types = []
    column_names = []

    def __init__(self, data_location, numcols, data_types=[], column_names=[]):
        if len(column_names) == 0:
            df = pd.read_csv(data_location, header=0, usecols=range(numcols))
            column_names = df.columns
        else:
            df = pd.read_csv(data_location, skiprows=1, names=column_names, usecols=range(numcols))

        for index, d_type in enumerate(data_types):
            if d_type == "date":
                df[column_names[index]] = pd.to_datetime(df[column_names[index]])
            else:
                df[column_names[index]] = df[column_names[index]].astype(d_type)

        self.data = df
        self.data_types = data_types
        self.column_names = column_names

    def computeFields(self, compute_instructions):
        for instruction in compute_instructions:
            instruction['']

    def sequenceGroup(self, column, sequenceName):
        df = self.data
        df.reset_index(inplace=True)
        df = df.set_index([column, "index"])
        df.index = pd.MultiIndex.from_arrays(
            [df.index.get_level_values(0), df.groupby(level=0).cumcount()],
            names=[column, sequenceName])
        df = df.reset_index(level=[1, 0])
        self.data = df

    def computeColumn(self, columnName, formula):
        df = self.data
        df[columnName] = pd.eval(formula)
        self.data = df

    def splitColumn(self, source_column, result_columns, delimiter):
        df = self.data
        df[result_columns] = df[source_column].str.split(delimiter, expand=True)
        self.data = df

    def stripColumn(self, column, destinationColumn, stripChars):
        df = self.data
        temp = df[column]
        for char in stripChars:
            temp = temp.str.replace(char, '')
        df[destinationColumn] = temp
        self.data = df

    def expandDate(self, column, dateformat, destinationPrefix="_"):
        destinationPrefix = column + destinationPrefix
        df = self.data

        self.addColumn(destinationPrefix + 'Date')
        self.addColumn(destinationPrefix + 'DayOfWeek')
        self.addColumn(destinationPrefix + 'DayOfMonth')
        self.addColumn(destinationPrefix + 'DayOfYear')
        self.addColumn(destinationPrefix + 'WeekOfYear')
        self.addColumn(destinationPrefix + 'Month')
        self.addColumn(destinationPrefix + 'DayPosition')

        for ind in df.index:
            dateArrayTemp = dateProcessor.ExpandDate(df[column][ind])
            df[destinationPrefix + 'Date'][ind] = dateArrayTemp['date']
            df[destinationPrefix + 'DayOfWeek'][ind] = dateArrayTemp['dayOfWeek']
            df[destinationPrefix + 'DayOfMonth'][ind] = dateArrayTemp['dayOfMonth']
            df[destinationPrefix + 'DayOfYear'][ind] = dateArrayTemp['dayOfYear']
            df[destinationPrefix + 'WeekOfYear'][ind] = dateArrayTemp['weekOfYear']
            df[destinationPrefix + 'Month'][ind] = dateArrayTemp['Month']
            df[destinationPrefix + 'DayPosition'][ind] = dateArrayTemp['dayPosition']
        self.data = df

    def addColumn(self, columnName):
        df = self.data
        df[columnName] = np.nan
        self.data = df

    def createDate(self, monthColumn, dayColumn, yearColumn, columnName,removeColumns=False):
        df = self.data

        Month = df[monthColumn]
        for char in ["'", " ", "-", "_"]:
            Month = Month.str.replace(char, '')
        for ind in Month.index:
            Month[ind] = str(strptime(str(Month[ind]), '%b').tm_mon)

        Year =  df[yearColumn]
        for char in ["'", " ", "-", "_"]:
            Year = Year.str.replace(char, '')

        Day = df[dayColumn]

        df[columnName] = Day+"/"+Month+"/"+Year
        df[columnName] = pd.to_datetime(df[columnName])
        if removeColumns:
            self.removeColumns([monthColumn,dayColumn,yearColumn])
        self.data = df

    def removeColumns(self,columns):
        df = self.data
        df.drop(columns)
        self.data = df
