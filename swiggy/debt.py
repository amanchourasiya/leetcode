class Debt:
    def __init__(self, userId1, userId2, amount):
        self.userId1 = userId1  # consumer
        self.userId2 = userId2  # producer
        self.amount = amount