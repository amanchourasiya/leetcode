import abc

from swiggy.expense import ExpenseType
from swiggy.debt import Debt

class ProcessorI(abc.ABC):
    @abc.abstractmethod
    def process(self, expense, usersDb):
        pass


class ExpenseProcessor(ProcessorI):
    def __init__(self):
        pass

    def process(self, expense, usersDb):
        owner = usersDb[expense.getOwner()]

        if expense.getExpenseType() == ExpenseType.EQUAL:
            if owner in expense.consumers:
                expense.amount = expense.amount - (expense.amount/ len(expense.consumers))
            splitAmount = expense.amount/ (len(expense.consumers)-1)
            for consumer in expense.consumers:
                if consumer != owner:
                    
                    debt = Debt(consumer, owner, splitAmount)
                    if usersDb[owner].isOwingTo(consumer):
                        usersDb[consumer].reduceDebt(owner, usersDb[owner].getDebtFrom(consumer))
                    else:
                        usersDb[consumer].addDebt(debt)

        else:
            for consumer, amount in map(expense.consumers, expense.splits):
                if consumer == owner:
                    continue
                debt = Debt(consumer, owner, amount)
                if usersDb[owner].isOwingTo(consumer):
                    usersDb[consumer].reduceDebt(owner, usersDb[owner].getDebtFrom(consumer))
                else:
                    usersDb[consumer].addDebt(debt)


                


