import datetime
import time
from DBUtils.databaseConnect import DBConnect as DB

DBConnection = DB(['TradeHistory'])
print(DBConnection.readDB('TradeHistory').fetchmany(50))

