class parent:
	def greet(self):
		print("hi parent")
class child1(parent):
	def show1(self):
		print("hi child1")
class child2(parent):
	def show2(self):
		print("hi child2")
		
s1 = child1()
s2 = child2()
s1.greet()
s1.show1()
s2.greet()
s2.show2()
