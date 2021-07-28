class HotBeverage:

	def __init__(self, price=0.30, name="hot beverage"):
		self.price = price
		self.name = name

	def description(self):
		return "Just some hot water in a cup."

	def __str__(self):
		return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"


class Coffee(HotBeverage):

	def __init__(self, Price=0.40, Name="coffee"):
		super().__init__(price=Price, name=Name)

	def description(self):
		return "A coffee, to stay awake."


class Tea(HotBeverage):

	def __init__(self, Name="tea"):
		super().__init__(name=Name)


class Chocolate(HotBeverage):

	def __init__(self, Price=0.50, Name="chocolate"):
		super().__init__(price=Price, name=Name)

	def description(self):
		return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):

	def __init__(self, Price=0.45, Name="cappuccino"):
		super().__init__(price=Price, name=Name)

	def description(self):
		return "Un po’ di Italia nella sua tazza!"
