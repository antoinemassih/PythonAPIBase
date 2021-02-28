from time import strptime


def ETTradeSymbolParser(symbol):
    symbol = str(symbol)
    symbol_array = symbol.split()
    symbol_data = {'ticker': symbol_array[0], 'securityType': 'Equity'}

    if len(symbol_array) > 2:
        symbol_data['securityType'] = 'Option'
        symbol_data['optionType'] = symbol_array[5]
        symbol_data['optionStrike'] = float(symbol_array[4].replace("$", ""))
        the_month = strptime(symbol_array[1], '%b').tm_mon
        symbol_data['optionExpiry'] = str(symbol_array[2]) + '/' + str(the_month) + '/' + symbol_array[3].replace("'",
                                                                                                                  "20")
        symbol_data['trade_group'] = symbol_data['ticker'] + symbol_data['optionType'] + str(
            symbol_data['optionStrike']) + symbol_data['optionExpiry']
    else:
        return symbol_data

    return symbol_data
