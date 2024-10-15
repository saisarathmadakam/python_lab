class student:
	branch="cse"
	def s_details(self,roll,name):
		self.s1=roll
		self.s2=name
	def display(self):
		print(self.s1)
		print(self.s2)
s = student()
s.s_details(123,"sarath")
s.display()
