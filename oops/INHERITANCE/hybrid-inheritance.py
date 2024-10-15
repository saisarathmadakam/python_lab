class parent:
	def greet(self):
		print("hi parent")
class child1(parent):
	def show1(self):
		print("hi child1")
class child2(parent):
	def show2(self):
		print("hi child2")
class grandchild(child1, child2):
	def display(self):
		print("hello grandchild")
		
g = grandchild()
g.greet()
g.show1()
g.show2()
g.display()
