from DataTransformUtils.TradeDataUtils.ETTradeProcessor import ETTradeprocessor
from DBUtils.databaseConnect import DBConnect as DB

DBConnection = DB('TradeData',['TradeData_Raw_ET'])

DBdata = DBConnection.readDBasDataFrane('TradeData_Raw_ET')
TransactionsObject = ETTradeprocessor(sourceType='db', data=DBdata)

option_transactions = TransactionsObject.option_data
equity_transactions = TransactionsObject.equity_data

DBConnection.writeToDB(option_transactions,"TransactionData_Option_ET")
DBConnection.writeToDB(equity_transactions,"TransactionData_Equity_ET")
DBConnection.closeDB()

