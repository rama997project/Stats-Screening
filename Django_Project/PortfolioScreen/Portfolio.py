from builtins import property, type

#subclass of Stock

class Portfolio():

    def __init__(self, portfolioName, inceptionDate, stockList = None, figureList = None):
        self.portfolioName = portfolioName
        self.inceptionDate = inceptionDate
        self.stockList = stockList
        self.figureList = figureList

        #set up dict
        if self.stockList is None:
            self.stockList = {  # key, #value
                '': '',
            }
        else:
            self.stockList = stockList

        if self.figureList is None:
            self.figureList = {  # key, #value
                '': '',
            }
        else:
            self.figureList = figureList
    # nur Stock-Objekt rein
    def addStock(self, stock):
        self.stockList[stock.ticker] = stock
    # nur Stock-Objekt rein
    def removeStock(self, stock):
        #create for each which finds the specified Stock and then removes it
        del self.stockList[stock.ticker]

    def getStock(self, ticker):
        ##enter name and then find Stock and return it's object
        return self.StockList[ticker]

    def getStockList(self):
        return self.StockList

    # hier darf nur das object Figure eingefügt werden
    def addfigure(self, figure):
        self.stockList[figure.figurename()] = figure
    # hier darf nur das object Figure eingefügt werden
    def removefigure(self, figure):
        #create for each which finds the specified Stock and then removes it
        del self.stockList[figure.figurename()]

    def getfigure(self, figureid = None, figurename = None):
        if figureid is None and figurename is not None:

            return '{}'.format(self.figureList[figurename])
        elif figurename is None and figureid is not None:
            # hier ist noch was zu tun
            return "noch nicht fertig"
        elif figurename is None and figureid is None:
            return None

    @property
    def portfolioName(self):
        return '{}'.format(self.portfolioName)

    @property
    def inceptionDate(self):
        return '{}'.format(self.inceptionDate)

    @portfolioName.setter
    def ChartType(self, portfolioName):
        self.portfolioName = type

    @portfolioName.deleter
    def ChartType(self):
        self.portfolioName = None

    @inceptionDate.setter
    def TimeHorizon(self, inceptionDate):
        self.inceptionDate = inceptionDate

    @inceptionDate.deleter
    def TimeHorizon(self):
        self.inceptionDate = None

