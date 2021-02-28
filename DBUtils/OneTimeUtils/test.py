from DataTransformUtils.DateTimeUtils.DateProcessor import ExpandDate
from DataTransformUtils.TradeDataUtils.TradeSymbolParser import ETTradeSymbolParser

#DBConnection = DB('TradeData,['TradeHistory'])
#print(DBConnection.readDB('TradeHistory').fetchmany(50))


print(ExpandDate('19/02/2021',"%d/%m/%Y"))
print(ETTradeSymbolParser("ADBE May 15 '20 $350 Call"))