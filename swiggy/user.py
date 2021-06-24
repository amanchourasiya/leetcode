import abc

class UserI(abc.ABC):
    @abc.abstractmethod
    def getUserId(self):
        pass
    
    @abc.abstractmethod
    def addDebt(self, amount, userId):
        pass



class User(UserI):
    def __init__(self, id) -> None:
        self.userId = id
        self.debts = []

    def addDebt(self, debt):
        self.debts.append(debt)

    def getAllDebts(self):
        return self.debts

    def isOwingTo(self, userId):
        if userId in self.debts:
            return True
        return False

    def getDebtFrom(self, userId):
        return self.debts[userId].amount

    def reduceDebtFrom(self, userId, reduce):
        self.debts[userId] = self.debts[userId] - reduce

