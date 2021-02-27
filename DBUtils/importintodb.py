import pandas as pd
from DataTransformUtils.tradesData import TradesDF
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DBUtils.databaseConnect import DBConnect as DB

#DBConnection = DB()
#database = DBConnection.database

TradeObject = TradesDF('csv', 'RealizedGLDownload.csv')
data = TradeObject.data
TradeObject.DateTradeOverlap()
#DBConnection.writeToDB(data,"TradesFromtheAir")
#DBConnection.closeDB()

