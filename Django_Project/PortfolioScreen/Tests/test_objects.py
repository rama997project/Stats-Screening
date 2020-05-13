from django.test import TestCase
from ..Portfolio import Portfolio
from ..Figure import Figure
from ..Stock import Stock
from ..Chart import Chart
from ..Toolbox import Toolbox


class TestModels(TestCase):

    allstocks = []

    def setUp(self):
        self.portfolio1 = Portfolio(
            portfolioName='Portfolio',
            inceptionDate='02-02-2015'
        )
        stock1 = Stock(
            ticker='TSLA',
            currprice='725'
        )
        stock1.addfigure(
            Figure(
                figurename='Alpha',
                figurevalue='x/a',
                figureid='12'
            ))
        self.allstocks.append(stock1)
        self.portfolio1.addStock(stock1)

        stock2 = Stock(
            ticker='APC',
            currprice='282'
        )
        stock2.addfigure(
            Figure(
                figurename='Beta',
                figurevalue='x/b',
                figureid='13'
            )
        )
        self.allstocks.append(stock2)
        self.portfolio1.addStock(stock2)


    def test_whether_stock_append_to_portfolio(self):
        self.assertListEqual(self.portfolio1.getStockList,self.allstocks)
