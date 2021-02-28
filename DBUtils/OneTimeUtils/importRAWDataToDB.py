import pandas as pd
from DataTransformUtils.tradesData import ET_Transactions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DBUtils.databaseConnect import DBConnect as DB

DBConnection = DB('TradeData',[])


#TradeObject = TradesDF('csv', 'RealizedGLDownload.csv')
#data = TradeObject.data
#TradeObject.DateTradeOverlap()
RawTradeData = pd.read_csv('../RealizedGLDownload.csv', header=0, usecols=range(9))


DBConnection.writeToDB(RawTradeData,"TradeData_Raw_ET")
#DBConnection.closeDB()

