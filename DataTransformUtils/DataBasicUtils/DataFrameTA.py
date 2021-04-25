import pandas as pd


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
    def splitColumn(self,source_column,result_columns,delimiter):
        df = self.data
        df[result_columns] = df[source_column].str.split(delimiter,expand=True )
        self.data = df
