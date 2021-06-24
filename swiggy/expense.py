class ExpenseType:
    EXACT = 1
    EQUAL = 2

class Expense:
    def __init__(self):
        pass

    def setExpenseType(self, expenseType):
        self.expenseType = expenseType
    
    def getExpenseType(self):
        return self.expenseType

    def setOwner(self, userId):
        self.ownerId = userId
    
    def getOwner(self):
        return self.ownerId

    def setConsumer(self, consumers):
        self.consumers = consumers

    def getConsumer(self):
        return self.consumers

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setSplits(self, splits):
        self.splits = splits

    def getSplits(self):
        return self.splits()

    def validate(self):
        pass

    
class Expense1(Expense):

    pass

class Expense2(Expense1):
    pass