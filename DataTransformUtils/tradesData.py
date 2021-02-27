import pandas as pd
import datetime
from time import strptime


def GLperType():
    return True


class TradesDF:
    data = pd.DataFrame()
    tickerlist = []
    optionsTickerList = []

    def __init__(self, sourceType, source):
        if sourceType == 'csv':
            df = pd.read_csv(source, header=0, usecols=range(9))
            tickers = []
            EquityType = []
            OptionType = []
            OptionExpiry = []
            OptionStrike = []
            HoldingTime = []
            OpenWeekday = []
            OpenWeek = []
            OpenMonth = []
            CloseWeekday = []
            CloseWeek = []
            CloseMonth = []
            AddTo = []

            for i, j in df.iterrows():
                j["GainLoss"] = float(j["GainLoss"])
                j["OpenDate"] = datetime.datetime.strptime(j["OpenDate"], "%m/%d/%Y")
                OpenWeekday.append(j["OpenDate"].weekday())
                OpenWeek.append(j["OpenDate"].isocalendar()[1])
                OpenMonth.append(j["OpenDate"].month)
                j["CloseDate"] = datetime.datetime.strptime(j["CloseDate"], "%m/%d/%Y")
                CloseWeekday.append(j["CloseDate"].weekday())
                CloseWeek.append(j["CloseDate"].isocalendar()[1])
                CloseMonth.append(j["CloseDate"].month)
                Hold = j["CloseDate"] - j["OpenDate"]
                HoldingTime.append(abs(Hold.days))
                wholeTicker = j['Symbol'].split()
                tickers.append(wholeTicker[0])
                alreadyhere = False
                alreadyhereOption = False

                for ticker in self.tickerlist:

                    if ticker == wholeTicker[0]:
                        alreadyhere = True
                if not alreadyhere:
                    self.tickerlist.append(wholeTicker[0])

                for Optionticker in self.optionsTickerList:

                    if Optionticker[0] == j['Symbol']:
                        alreadyhereOption = True
                        Optionticker[1] = Optionticker[1] + 1
                        AddTo.append(Optionticker[1])

                if not alreadyhereOption:
                    self.optionsTickerList.append([j['Symbol'], 0])
                    AddTo.append(0)

                if len(wholeTicker) > 2:
                    OptionType.append(wholeTicker[5])
                    EquityType.append("option")
                    OptionStrike.append(float(wholeTicker[4].replace("$", "")))
                    date = datetime.datetime(int(wholeTicker[3].replace("'", "20")),
                                             strptime(wholeTicker[1], '%b').tm_mon, int(wholeTicker[2]))
                    OptionExpiry.append(date)
                else:
                    OptionType.append("equity")
                    EquityType.append("equity")
                    OptionStrike.append(0.0)
                    OptionExpiry.append(0)

            print(self.optionsTickerList)
            df['Ticker'] = tickers
            df['OptionType'] = OptionType
            df['EquityType'] = EquityType
            df['OptionStrike'] = OptionStrike
            df['OptionExpiry'] = OptionExpiry
            df['HoldingTime'] = HoldingTime
            df['OpenWeekday'] = OpenWeekday
            df['CloseWeekday'] = CloseWeekday
            df['OpenWeek'] = OpenWeek
            df['CloseWeek'] = CloseWeek
            df['OpenMonth'] = OpenMonth
            df['CloseMonth'] = CloseMonth
            df['AddTo'] = AddTo

            self.data = df

    def GLperTicker(self):
        GLArray = {i: 0.0 for i in self.tickerlist}

        for i, j in self.data.iterrows():
            GLArray[j["Ticker"]] += j["GainLoss"]

        return pd.DataFrame(list(GLArray.items()), columns=['Ticker', 'Amount'])

    def GLperTimeFrame(self):
        GLArray = [0] * max(self.data["HoldingTime"] + 1)

        for i, j in self.data.iterrows():
            GLArray[j["HoldingTime"]] += j["GainLoss"]
        GLDF = pd.DataFrame(GLArray, columns=['Amount'])
        GLDF.index.name = "Days"
        GLDF.reset_index(inplace=True)

        return GLDF

    def GLperTradeSize(self):
        GLArray = [[5, 0], [10, 0], [20, 0], [30, 0], [50, 0], [100, 0], [200, 0], [500, 0]]

        for i, j in self.data.iterrows():
            if j['Quantity'] < GLArray[0][0]:
                GLArray[0][1] += j['GainLoss']
            else:
                for k, g in enumerate(GLArray[1:]):
                    if GLArray[k - 1][0] < j['Quantity'] < GLArray[k][0]:
                        GLArray[k][1] += j['GainLoss']
        GLDF = pd.DataFrame(GLArray, columns=['Size', 'Amount'])
        return GLDF

    def DateTradeOverlap(self):
        Data = [[]]

        for i in range(365):
            Data.append([])

        for k, trade in self.data.iterrows():
            opendate = datetime.datetime.strptime(trade["OpenDate"], '%m/%d/%Y')
            closedate = datetime.datetime.strptime(trade["CloseDate"], '%m/%d/%Y')
            opendayofyear = opendate.timetuple().tm_yday
            closedayoftheyear = closedate.timetuple().tm_yday
            if opendayofyear == closedayoftheyear:
                therange = []
                therange.append(closedayoftheyear)
            else:
                interange = range(opendayofyear, closedayoftheyear)
                therange = list(interange)
            print(therange)

            for thedate in therange:
                # print("Added"+trade['Symbol']+" to day : "+str(thedate))
                Data[thedate].append(k)
        print(Data)
        #DF = pd.DataFrame(Data, columns=['Day', 'Symbol'])
        return Data
