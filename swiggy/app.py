from display import DisplayService
user import User
from swiggy.processor import ExpenseProcessor
from swiggy.expense import Expense
from swiggy.debt import Debt

class App:
    def getInstance():
        app = App()
        return app

    def __init__(self): # singleton
        self.users = {}
        self.userCount = 0
        self.expenseProcessor = ExpenseProcessor()
        self.displayService = DisplayService()

    def createUser(self):
        user = User(self.userCount)
        self.usercount+=1


    def createExpense(self, owner, amount, expenseType, consumers, splits=[]):
        expense1 = Expense()
        expense1.setExpenseType(expenseType) #
        expense1.setOwner(owner)
        expense1.setConsumers(consumers)
        expense1.setAmount(amount)
        expense1.setSplits(splits)
        
        if expense1.amount != sum(splits):
            print("Not a valid expese")
            return

        self.expenseProcessor.process(expense1)
        

    def getAllUsersBalance(self):
        self.displayService.displayAllUsers(self.users.values())

    def getUserBalance(self, userId):
        if userId not in self.users:
            print('User not present')
            return
        self.displayService.displayDebt(self.users[userId].getDebts())