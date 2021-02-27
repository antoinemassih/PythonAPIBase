from sqlalchemy import Table

from models.modeldb import db



class TradeHistory(db.Model):
    __tablename__ = 'tradesHistory'

    index = db.Column(db.Integer, primary_key=True, unique=True)
    Symbol = db.Column(db.Text)
    Quantity = db.Column(db.Integer)
    OpenDate = db.Column(db.Text)
    OpenPrice = db.Column(db.Float(53))
    DollarCost = db.Column(db.Float)
    CloseDate = db.Column(db.Text)
    ClosePrice = db.Column(db.Float(53))
    ClosingAmount = db.Column(db.Float(53))
    GainLoss = db.Column(db.Float(53))
    Ticker = db.Column(db.Text)
    OptionType = db.Column(db.Text)
    EquityType = db.Column(db.Text)
    OptionStrike = db.Column(db.Float(53))
    OptionExpiry = db.Column(db.Text)
    HoldingTime = db.Column(db.Integer)

    def __repr__(self):
        return "<TradeHistory(Symbol='{}', Quantity='{}', OpenDate='{}', OpenPrice={}, DollarCost={}, CloseDate='{}', " \
               "ClosePrice={}, ClosingAmount={}, GainLoss={}, Ticker='{}', OptionType='{}', ClosingAmount={}, " \
               "EquityType='{}', OptionStrike={}, OptionExpiry='{}', HoldingTime={}) >" \
            .format(self.symbol, self.quantity, self.openDate, self.openPrice, self.dollaCost, self.closeDate,
                    self.closePrice, self.closingAmount, self.gainLoss, self.ticker, self.optionType,
                    self.closingAmount, self.equityType, self.optionStrike, self.optionExpiry, self.holdingTime)


class TradeGLByHoldingTime(db.Model):
    __tablename__ = 'TradesByHoldingTime'

    id = db.Column(db.Integer, primary_key=True)
    holdingtime = db.Column(db.Integer)
    gainloss = db.Column(db.Float)

    def __repr__(self):
        return "<TradesByHoldingTime( id={},holdingtime={},gainloss={}) >" \
            .format(self.id,self.holdingtime, self.gainloss)
