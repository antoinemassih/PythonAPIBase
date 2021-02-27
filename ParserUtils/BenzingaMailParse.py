import bs4

from ParserUtils import ParseUtils


class BzMessage:

    def __init__(self, Message):
        self.bzsoup = bs4.BeautifulSoup(Message, features='html.parser')

    def GetTickersFromMail(self):
        tickers = self.bzsoup.find_all("strong", text=ParseUtils.like('Tickers:'))
        tickerArray = []
        if len(tickers)>0:
            if len(tickers[0].parent.find_all('a')) > 0:
                for ticker in tickers[0].parent.find_all('a'):
                    tickerArray.append(ticker.text)

        return tickerArray
