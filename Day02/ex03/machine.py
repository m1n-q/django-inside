import random
from beverages import *

class CoffeeMachine:


	def __init__(self) -> None:
		self.served = 0

	class EmptyCup(HotBeverage):
		def __init__(self, Price=0.90, Name="empty cup"):
			super().__init__(price=Price, name=Name)

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.served -= 10

	def serve(self, beverage):
		if self.served == 10:
			raise CoffeeMachine.BrokenMachineException()
		if issubclass(beverage, HotBeverage):
			if (random.random() <= 0.8):
				self.served += 1
				return beverage()
			else:
				return self.EmptyCup()
		else:
			return


cm = CoffeeMachine()

for i in range(20):
	try:
		get = cm.serve(CoffeeMachine)
		print(get)
	except CoffeeMachine.BrokenMachineException as e:
		print(e)
	print()

cm.repair()
# for i in range(10):
# 	get = cm.serve(cm.EmptyCup)
# 	print(get)
# try:
# 	cm.serve(cm.EmptyCup)
# except CoffeeMachine.BrokenMachineException as e:
# 	print(e)


# for i in range(10):
# 	print(random.random())

# print(issubclass(CoffeeMachine, HotBeverage))
