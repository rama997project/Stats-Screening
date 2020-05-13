

import unittest

from PortfolioScreen.Figure import Figure


class TestHelloWorld(unittest.TestCase):
	
	def test_equals(self):
		fig = Figure
		fig.figurename = "name1"
		self.assertEquals(fig.figurename,"name1")