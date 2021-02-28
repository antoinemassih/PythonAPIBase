import pandas as pd
from DataTransformUtils.tradesData import ET_Transactions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DBUtils.databaseConnect import DBConnect as DB

DBConnection = DB('TradeData',['TradeData_Raw_ET'])

DBdata = DBConnection.readDBasDataFrane('TradeData_Raw_ET')
TransactionsObject = ET_Transactions(sourceType='db', data=DBdata)

DBConnection.writeToDB(TransactionsObject.data,"TransactionData_ET")
DBConnection.closeDB()

