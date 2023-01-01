class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.size = len(balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.size or account2 > self.size or self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money  
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.size:
            return False
        self.balance[account - 1] += money
        return True
        
    def withdraw(self, account: int, money: int) -> bool:
        if account > self.size or money > self.balance[account - 1]:
            return False
        self.balance[account - 1] -= money
        return True