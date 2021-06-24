class DisplayService:
    def displayAllUsers(self, users):
        for user in users:
            self.displayDebt(user.getAllDebts())


    def displayDebt(self, debts):
        for debt in debts:
            s = str(debt.userId1) + ' owes ' + str(debt.userId2) + ' ' + str(debt.amount)
