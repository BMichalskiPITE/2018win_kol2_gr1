#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Good Luck
import uuid

class NotEnoughtCashException(Exception):
	pass
class CannotAddClientAgain(Exception):
	pass
class NegativeCaschValue(Exception):
	pass

class Bank:
	def __init__(self, bank_name):
		self.name = bank_name
		self.clients = []

	def add_client(self,new_client):
		self.check_if_is_client(new_client)
		is_client = filter(lambda client: client.uuid == new_client.uuid, self.clients)
		if len(list(is_client)) > 0:
			raise CannotAddClientAgain
		self.clients.append(new_client)

	def transfer(self, from_client, to_client, amount):
		self.check_if_is_client(from_client)
		self.check_if_is_client(to_client)
		if amount <= 0:
			raise NegativeCaschValue
		from_client.wirthdraw_cash(amount)
		to_client.add_cash(amount)

	def __repr__(self):
		 return "Bank: {}".format(self.name)

	def check_if_is_client(slef, client):
		if not isinstance(client, Client):
			raise AttributeError

class Client:
	def __init__(self, name, lastname, initial_cash):
		self.name = name
		self.lastname = lastname
		self.cash = initial_cash
		self.uuid = uuid.uuid4()

	def add_cash(self,amount):
		self.cash += amount

	def wirthdraw_cash(self, amount):
		if self.cash < amount:
			raise NotEnoughtCashException
		self.cash -=amount
		return self.cash

	def __repr__(self):
		return "{} {} {}".format(self.name, self.lastname, self.cash)

if __name__ == "__main__":
	jan = Client("Jan","Kowalski",214)
	marek = Client("Marek", "koziol",0)

	bank = Bank("somebank")

	print(bank)
	print(jan)
	print(marek)
	marek.add_cash(123)
	print(marek)
	bank.transfer(marek, jan, 20)
	print(jan)
	print(marek)
