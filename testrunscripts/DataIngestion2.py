import pandas as pd
from DataTransformUtils.DataBasicUtils.DataFrameTA import DataFrameTA as DTF


column_names = ["Symbol","Quantity","OpenDate","OpenPrice","DollarCost","CloseDate","ClosePrice","ClosingAmount","GainLoss"]
data_types = ["str","int64","date","float64","float64","date","float64","float64","float64"]

DTFObject = DTF(data_location='data/RealizedGLDownload.csv',data_types=data_types,column_names=column_names,numcols=9)
DTFObject.computeColumn("Holding","df.CloseDate-df.OpenDate")
DTFObject.sequenceGroup(column='Symbol',sequenceName='AddedTrade')
DTFObject.splitColumn(source_column="Symbol",result_columns=['Ticker','ExpMonth','ExpDay','ExpYear','Strike','OptionType'],delimiter=" ")

#Missing Date Expander / Processor

df = DTFObject.data

dfEquity = df.loc[df['Symbol'].str.len() <= 4]
dfOptions = df.loc[df['Symbol'].str.len() > 4]

df = DTFObject.data

spec_chars = [" ",'$',"'"]


#df[['Ticker','ExpMonth','ExpDay','ExpYear','Strike','OptionType']] = df.Symbol.str.split(" ",expand=True,)
for char in spec_chars:
    df["Symbol"] = df["Symbol"].str.replace(char, '')
print(df)
# gui = show(df)
