developer = "Devin"
print(type(developer))  # <class 'str'>

account_balance = 12
print(isinstance(account_balance, int))          # True
print(isinstance(account_balance, (int, float))) # True
