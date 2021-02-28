import pandas as pd

from DataTransformUtils.DateTimeUtils.DateProcessor import ExpandDate
from DataTransformUtils.TradeDataUtils.TradeSymbolParser import ETTradeSymbolParser


class ETTradeprocessor:
    equity_data = pd.DataFrame()
    option_data = pd.DataFrame()
    raw_Data = pd.DataFrame()

    def __init__(self, sourceType, data):
        if sourceType == 'csv':
            self.raw_Data = pd.read_csv(data, header=0, usecols=range(9))
        else:
            self.raw_Data = data

        equity_transaction_data = []
        option_transaction_data = []

        for i, j in self.raw_Data.iterrows():
            open_transaction = {}
            close_transaction = {}

            symbol_array = ETTradeSymbolParser(j['Symbol'])

            if symbol_array['securityType'] == 'Equity':
                # add Symbols for Equity
                open_transaction['ticker'] = symbol_array['ticker']
                close_transaction['ticker'] = symbol_array['ticker']

                open_transaction['securityType'] = symbol_array['securityType']
                close_transaction['securityType'] = symbol_array['securityType']
            else:
                # add symbols for Options
                open_transaction['ticker'] = symbol_array['ticker']
                open_transaction['securityType'] = symbol_array['securityType']
                open_transaction['optionType'] = symbol_array['optionType']
                open_transaction['optionStrike'] = symbol_array['optionStrike']
                open_transaction['optionExpiry'] = symbol_array['optionExpiry']
                open_transaction['trade_group'] = symbol_array['trade_group']
                # -- close transactions
                close_transaction['ticker'] = symbol_array['ticker']
                close_transaction['securityType'] = symbol_array['securityType']
                close_transaction['optionType'] = symbol_array['optionType']
                close_transaction['optionStrike'] = symbol_array['optionStrike']
                close_transaction['optionExpiry'] = symbol_array['optionExpiry']
                close_transaction['trade_group'] = symbol_array['trade_group']

                # Process Options Expiry Dates
                expiry_date_array = ExpandDate(open_transaction['optionExpiry'], "%d/%m/%Y")
                open_transaction['expiryDate'] = expiry_date_array['date']
                open_transaction['expiryDayOfWeek'] = expiry_date_array['dayOfWeek']
                open_transaction['expiryDayOfMonth'] = expiry_date_array['dayOfMonth']
                open_transaction['expiryDayOfYear'] = expiry_date_array['dayOfYear']
                open_transaction['expiryWeekOfYear'] = expiry_date_array['weekOfYear']
                open_transaction['expiryMonth'] = expiry_date_array['Month']
                open_transaction['expiryDayPosition'] = expiry_date_array['dayPosition']

                close_transaction['expiryDate'] = expiry_date_array['date']
                close_transaction['expiryDayOfWeek'] = expiry_date_array['dayOfWeek']
                close_transaction['expiryDayOfMonth'] = expiry_date_array['dayOfMonth']
                close_transaction['expiryDayOfYear'] = expiry_date_array['dayOfYear']
                close_transaction['expiryWeekOfYear'] = expiry_date_array['weekOfYear']
                close_transaction['expiryMonth'] = expiry_date_array['Month']
                close_transaction['expiryDayPosition'] = expiry_date_array['dayPosition']

            # Process Dates

            open_date_array = ExpandDate(j['OpenDate'], "%m/%d/%Y")
            close_date_array = ExpandDate(j['CloseDate'], "%m/%d/%Y")

            # Opening Transaction dates
            open_transaction['date'] = open_date_array['date']
            open_transaction['dayOfWeek'] = open_date_array['dayOfWeek']
            open_transaction['dayOfMonth'] = open_date_array['dayOfMonth']
            open_transaction['dayOfYear'] = open_date_array['dayOfYear']
            open_transaction['weekOfYear'] = open_date_array['weekOfYear']
            open_transaction['Month'] = open_date_array['Month']
            open_transaction['dayPosition'] = open_date_array['dayPosition']

            # Closing Transaction dates
            close_transaction['date'] = close_date_array['date']
            close_transaction['dayOfWeek'] = close_date_array['dayOfWeek']
            close_transaction['dayOfMonth'] = close_date_array['dayOfMonth']
            close_transaction['dayOfYear'] = close_date_array['dayOfYear']
            close_transaction['weekOfYear'] = close_date_array['weekOfYear']
            close_transaction['Month'] = close_date_array['Month']
            close_transaction['dayPosition'] = close_date_array['dayPosition']

            # add Actions
            if j['ClosingAmount'] > 0:
                close_transaction['action'] = 'SELL'
            else:
                close_transaction['action'] = 'EXPIRED'

            open_transaction['action'] = 'BUY'

            # Dollar Amount
            open_transaction['dollarAmount'] = j['DollarCost']
            close_transaction['dollarAmount'] = j['ClosingAmount']

            # Quantity
            open_transaction['quantity'] = j['Quantity']
            close_transaction['quantity'] = j['Quantity']

            if open_transaction['securityType'] == 'Equity':
                equity_transaction_data.append(open_transaction)
                equity_transaction_data.append(close_transaction)
            else:
                option_transaction_data.append(open_transaction)
                option_transaction_data.append(close_transaction)

        self.equity_data = pd.DataFrame(equity_transaction_data)
        self.option_data = pd.DataFrame(option_transaction_data)
