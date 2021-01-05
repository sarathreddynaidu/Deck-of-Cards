class Human:

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self, value):
		self._age = value

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@full_name.setter
	def full_name(self, name):
		self.first, self.last = name.split(" ")
	

sai = Human("Sai", "Reddy", 23)
print(sai.full_name)
print(sai.age)
sai.age = 24
sai.full_name = "Sarath Reddy"
print(sai.age)
print(sai.full_name)
