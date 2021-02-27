import pandas as pd
from datatransform.tradesData import TradesDF
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:monkeyxx@192.168.1.135:5432/postgres')
database = engine.connect()


Session = sessionmaker(bind=engine)
s = Session()


TradeObject = TradesDF('csv', 'OneTimeUtils/RealizedGLDownload.csv')
data = TradeObject.data

df2 = TradeObject.GLperTicker()
df3 = TradeObject.GLperTimeFrame()
df4 = TradeObject.GLperTradeSize()

sql_text = pd.io.sql.get_schema(data.reset_index(), "tradesHistory")
for col in data.columns:
    print(col)

data.to_sql('tradesHistoryNew', con=database, if_exists='replace', index=False)
database.close()

