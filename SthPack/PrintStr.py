class PrintStr:
    def __init__(self):
        self.MaxStrLength = 105
        self.FillChar = '='
        self.dummyString = ''.center(self.MaxStrLength, self.FillChar)


    def Start(self, string):
        print(self.dummyString)
        print(('   {}   '.format(string)).center(self.MaxStrLength, self.FillChar))


    def End(self, string):
        print(('   {}   '.format(string)).center(self.MaxStrLength, self.FillChar))
        print(self.dummyString)


    def OneLine(self, string):
        print(('   {}   '.format(string)).center(self.MaxStrLength, self.FillChar))


    def ThreeLine(self, string):
        print(self.dummyString)
        print(('   {}   '.format(string)).center(self.MaxStrLength, self.FillChar))
        print(self.dummyString)


    # def Box(self, string):
    #     print('|' + (''.center(self.MaxStrLength - 2)) + '|')
    #     print('|' + (('   {}   '.format(string)).center(self.MaxStrLength-2)) + '|')
    #     print('|' + (''.center(self.MaxStrLength - 2)) + '|')
