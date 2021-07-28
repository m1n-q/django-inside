class Intern:

	def __init__(self, name="My name? I’m nobody, an intern, I have no name.") -> None:
		self.Name = name


	def __str__(self) -> str:
		return self.Name


	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")


	class Coffee:
		def __str__(self) -> str:
			return "This is the worst coffee you ever tasted."


	def make_coffee(self):
		return self.Coffee()


