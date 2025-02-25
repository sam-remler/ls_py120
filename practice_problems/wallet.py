
class Wallet():
    def __init__(self, amount = 0):
        self.amount = amount
    
    def __add__(self, other):
        if not isinstance(other, Wallet):
            NotImplemented
        return Wallet(amount=self.amount + other.amount)
    
    def __str__(self):
        return f"Wallet with ${self.amount}"

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True
print(merged_wallet)