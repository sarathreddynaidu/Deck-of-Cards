class Aquatic:
	def __init__(self, name):
		print("AQUATIC INIT")
		self.name = name

	def swim(self):
		return f"{self.name} is swimming"

	def greet(self):
		return f"I am {self.name}  of the sea"

class Ambulatory:
	def __init__(self, name):
		print("AMBULATORY INIT")
		self.name = name

	def walk(self):
		return f"{self.name} is walking"

	def greet(self):
		return f"I am {self.name}  of the land"

class Penguin(Ambulatory, Aquatic):
	def __init__(self, name):
		print("PENGUIN INIT")
			#If we use super() the first inherited class will be in action. So the Ambulatory.
			#If we want aquatic in action then we need to class Penguin(Aquatic, Ambulatory)
		# super().__init__(name=name)
			#Not recommended to use super() for multiple inheritance
			#If we need the both inherited classes to be in action then we need specity both inits
		Ambulatory.__init__(self, name=name)
		Aquatic.__init__(self, name=name)

captian_cook = Penguin("Captain Cook")





########## Method Resolution Order (MRO) ##########
# Penguin.__mro__
# Penguin.mro()
# help(Penguin)
