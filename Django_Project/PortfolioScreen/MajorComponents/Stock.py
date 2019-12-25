from .Figure import Figure
from .Portfolio import Portfolio
from .Toolbox import Toolbox

class Stock():

    def __init__(self, ticker, price, figures=None):
        self.ticker = ticker
        self.curr_price = price
        if figures is None:
            self.figures = {  # key, #value
                '': '',
            }
        else:
            self.figures = figures

    def calcAllFigures(self):
        for item in self.figures.items():
            print(item)
            print(type(item))

    def addfigure(self, figure: Figure):
        self.figures[figure.figurename()] = figure

    def removefigure(self, figurename):
        del self.figures[figurename]

    def getfigure(self, figurename):
        return ''.format(self.figures[figurename])

    @property
    def ticker(self):
        return '{}'.format(self.ticker)

    @property
    def curr_price(self):
        return '{}'.format(self.curr_price)

    @ticker.setter
    def ChartType(self, ticker):
        self.ticker = type

    @ticker.deleter
    def ChartType(self):
        self.ticker = None

    @curr_price.setter
    def TimeHorizon(self, price):
        self.curr_price = price

    @curr_price.deleter
    def TimeHorizon(self):
        self.curr_price = None
