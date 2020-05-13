from django.test import TestCase
from .. import Portfolio,Figure,Stock,Chart,Toolbox


class TestModels(TestCase):

    def setUp(self):
        self.portfolio1 = Portfolio.objects.create(
            portfolioName='Portfolio',
            inceptionDate='02-02-2015'
        )

    def test_if_stock_list_sticks_into_portfolio(self):
        portfolio1 = Stock.objects.create(
            project=self.project1,
            name='development'
        )
        Expense.objects.create(
            project=self.project1,
            title='expense1',
            amount=1000,
            category=category1
        )
        Expense.objects.create(
            project=self.project1,
            title='expense2',
            amount=2000,
            category=category1
        )


    def test_if_stock_list_sticks_in_portfolio(self):
        portfolio1 = Stock.objects.create(
            project=self.project1,
            name='development'
        )
        Expense.objects.create(
            project=self.project1,
            title='expense1',
            amount=1000,
            category=category1
        )
        Expense.objects.create(
            project=self.project1,
            title='expense2',
            amount=2000,
            category=category1
        )
        self.assertEquals(self.project1.budget_left, 7000)