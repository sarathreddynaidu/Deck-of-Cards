#---------- Iterator vs # Iterable ------------

name = "sarath"

# print(next(name)) # TypeError

it = iter(name)

print(it)

print(next (it)) # s
print(next (it)) # a 
print(next (it)) # r
print(next (it)) # a
print(next (it)) # t
print(next (it)) # h
print(next (it)) # Stop Iteration Erro


# Similar to a for loop, behind the scenes
# for i in "sarath":
# 	print(i)

# -----------------------------------------------

#------------ Custom For Loop -------------------

def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)

def square(x):
	print(x*x)

my_for("sarath", print)
my_for([1, 2, 3, 4, 5], square)

# -------------------------------------------------

# ------------- Custom Iterator (range) ------------------

class Counter:

	def __init__(self, low, high)
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration

for x in Counter(0, 10):
	print(x)

#---------------------------------------------------------
