class Student:
    college="IIITG"  #same for all
    name="all anonymous"  # object attribute>class atribute
    def __init__(self): #default constructor
        pass
    def __init__(self,name,marks):  # parameterised constructor
        self.name=name  # self for individual
        self.marks=marks  # self for individual
        print("adding student to database....")
    def say_hello(self):
        print("hello",self.name)
    @staticmethod  # decorator-->takes func as parameter and give op as func
    def say_good_morning_all(): # if we use @staticmethod then we don't have to use self
        print("good morning to all")
    # name="Abhishek Kumar"
s1=Student("Abhishek Kumar", 98)
s2=Student("Ashish Kumar", 100)
print(s1.name,s1.marks)
print(s1.college)
s1.say_hello()  # if we print this line then it will also give a none
print(s2.name,s2.marks)
print(s2.college)
s1.say_good_morning_all()