class Bank(object):


	def __init__(self,accountno,balance):
		self.accountno=accountno
		self.balance=balance
	

	def withdraw(self,amount):
		self.balance -= amount
		return self.balance

	def deposit(self,amount):
		self.balance += amount
		return self.balance

	def check_balance(self):
		return self.balance




c=Bank(6415456,2500)
print(c.withdraw(200))
print(c.check_balance())
print(c.deposit(600))
