class A:
	def do_some(Self):
		print("Method Defined In: A")

class B(A):
	def do_some(Self):
		print("Method Defined In: B")
		super().do_some() # we get A

class C(A):
	def do_some(Self):
		print("Method Defined In: C")

class D(B, C):
	def do_some(Self):
		print("Method Defined In: D")
		super().do_some() # we get B becuase it is inherited before C


# MRO
# print(D.__mro__)
# print(D.mro())
# help(D)

thing = D()
thing.do_some()



# order

#		  A
#	   / \
#	  B   C
#	   \ /
#		  D	


# To confirm the order remove methods in each class and add pass
