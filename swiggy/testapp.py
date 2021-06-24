from expense import *
from app import *

app = App()
user1 = app.createUser() # 0
user2 = app.createUser() # 1
user3 = app.createUser() # 2

app.createExpense(1, 100, ExpenseType.EQUAL, [1,2,3], splits=[])

app.getAllUsersBalance()