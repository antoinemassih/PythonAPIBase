from datetime import datetime

import pandas as pd

from DataConnection.StockData import StockDataFrame
from datatransform.tradesData import TradesDF
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:monkeyxx@192.168.1.135:5432/postgres')
database = engine.connect()


Session = sessionmaker(bind=engine)
s = Session()


StockData = StockDataFrame('AAPL')
StockData.get_historical(start=datetime(2016, 1, 1),end=datetime(2021, 1, 1))
print(StockData.data)

#sql_text = pd.io.sql.get_schema(data.reset_index(), "tradesHistory")

#data.to_sql('TradeHistoryNew', con=database, if_exists='replace', index=False)
database.close()

