class Bank:
    
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.nb_accounts = len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1<=self.nb_accounts and account1>0 and account2<=self.nb_accounts and account2>0:
            if self.balance[account1-1] >= money:
                self.withdraw(account1,money)
                self.deposit(account2,money)
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account<=self.nb_accounts and account>0:
            self.balance[account-1]+=money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account<=self.nb_accounts and account>0:
            if self.balance[account-1]>= money:
                self.balance[account-1]-=money
                return True
            else:
                return False
        else:
            return False



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

