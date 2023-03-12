#setters and getters using get and set functions 

class Student:
	def __init__(self,name,roll_no,age):
		self.name=name
		self.roll_no=roll_no
		self._age=age	
	
	def get_age(self):
		#self._age=18
		return self._age
	
	def set_age(self, value):
		self._age=value
		
student1=Student("student's_name","22S11AAAA","")
student1.set_age(18)
print(student1.name)
print(student1.roll_no)
#print(student1.get_age())
print(student1._age)