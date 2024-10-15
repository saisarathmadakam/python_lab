class animal():
	def action(self):
		print("bow bow")
class dog(animal):
	def happy(self):
		print("huu huu")
class cat(dog):
	def expression(self):
		print("meow meow")
ob = cat()
ob.action()
ob.happy()
ob.expression()


