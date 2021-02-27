import pandas as pd
from datatransform.tradesData import TradesDF

TradeObject = TradesDF('csv', 'RealizedGLDownload.csv')
data = TradeObject.data

df2 = TradeObject.GLperTicker()
df3 = TradeObject.GLperTimeFrame()
df4 = TradeObject.GLperTradeSize()

sql_text = pd.io.sql.get_schema(df2.reset_index(), "GLperticker")
print(sql_text)

sql_text2 = pd.io.sql.get_schema(df3.reset_index(), "GLperHoldingTime")
print(sql_text2)
