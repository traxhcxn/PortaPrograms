#setters and getters using decorators
class Student:
	def __init__(self,name,roll_no,age):
		self.__name=name
		self.roll_no=roll_no
		self.__age = age
		
	@property
	def age(self):
		return self.__age
	def name(self):
		return self.__name
	
	
	@age.setter
	def age(self, value):
		self.__age = value
	def name(self,value):
		self.__name = value

student1= Student('','22S11AAAA','')
student1.age = 19
student1.name='xxx'
print(student1.name)
print(student1.roll_no)
print(student1.age)