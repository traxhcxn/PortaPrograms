#setters and getters using decorators
class Student:
	def __init__(self,name,roll_no,age):
		self.name=name
		self.roll_no=roll_no
		self.__age = age
		
	@property
	def age(self):
		return self.__age
	
	@age.setter
	def age(self, value):
		self.__age = value
	
student1= Student("student's_name","22S11AAAA","")
student1.age = 18
print(student1.name)
print(student1.roll_no)
print(student1.age)
