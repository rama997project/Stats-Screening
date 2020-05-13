from Django_Project.PortfolioScreen.MajorComponents.Toolbox import Toolbox

class Figure():

    def __init__(self, figurename, figurevalue, figureid):
        self.figurename = figurename
        self.figurevalue = figurevalue
        self.figureid = figureid

    def figurename(self):
        return '{}'.format(self.figurename)

    def figurevalue(self):
        return '{}'.format(self.figurevalue)

    # figureid
    def figureid(self):
        return '{}'.format(self.figureid)

    @figurename.setter
    def figurename(self, name):
        self.figurename = name

    @figurename.deleter
    def figurename(self):
        self.figurename = None

    @figurevalue.setter
    def figurevalue(self, value):
        self.figurevalue = value

    @figurevalue.deleter
    def figurevalue(self):
        self.figurevalue = None

    @figureid.setter
    def figureid(self, figureid):
        self.figureid = figureid

    @figureid.deleter
    def figureid(self):
        self.figureid = None