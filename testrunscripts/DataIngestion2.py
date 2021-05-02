import pandas as pd
from DataTransformUtils.DataBasicUtils.DataFrameTA import DataFrameTA as DTF


column_names = ["Symbol","Quantity","OpenDate","OpenPrice","DollarCost","CloseDate","ClosePrice","ClosingAmount","GainLoss"]
data_types = ["str","int64","date","float64","float64","date","float64","float64","float64"]

DTFObject = DTF(data_location='data/RealizedGLDownload.csv',data_types=data_types,column_names=column_names,numcols=9)
DTFObject.computeColumn("Holding","df.CloseDate-df.OpenDate")
DTFObject.sequenceGroup(column='Symbol',sequenceName='AddedTrade')
DTFObject.splitColumn(source_column="Symbol",result_columns=['Ticker','ExpMonth','ExpDay','ExpYear','Strike','OptionType'],delimiter=" ")

DTFObject.expandDate(column="OpenDate",dateformat="%Y-%m-%d")
DTFObject.expandDate(column="CloseDate",dateformat="%Y-%m-%d")
DTFObject.stripColumn(column="Symbol",destinationColumn="Symbol_Identifier",stripChars=[" ",'$',"'"])


df = DTFObject.data

dfEquity = df.loc[df['Symbol'].str.len() <= 4]

DTFObject.data = df.loc[df['Symbol'].str.len() > 4]
DTFObject.createDate(monthColumn="ExpMonth",dayColumn="ExpDay",yearColumn="ExpYear",columnName="ExpDate")

dfOptions = df.loc[df['Symbol'].str.len() > 4]



df = DTFObject.data





print(df)
# gui = show(df)
