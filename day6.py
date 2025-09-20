# OBJECT ORIENTED PROGRAMMING

# ENTITY : anything which has existence or anything which exists.
# CLASS : it is a logical entity or blue print or a plan to create multiple objects. multiple objects created using the same class are known as identical objects or similar objects.
# SYNTAX class classname: constructor + object creation

# OBJECT : it is a real world entity. object consists of states & behaviours. object is also known as instance. SYNTAX : ObjRef = classname()

# Classname Rules:

# the class name can be any valid identifier. it can't be python reserved word. a valid class name starts with aletter, followed by any number of letter, numbers or underscores. a class name generally starts with capital letter.

# HOW TO CREATE A CLASS to define a class, we use the class keyword. this was an empty class. class Mobile:

#                                             object
#                                 1.states              2.behaviour
# states : represents the properties or attributes of an entity (data member) behaviour : functionality of the object (methods/funtions)

#                                            student
#                                states                    behaviours

#                               studentname                bunking classes 
#                               age                         studying
#                               regnum                       exams
# Datamembers : it is a container or data holder which holds or stores the data.

#                                            datamembers
#                               > variable                   > constant   
# 1.variable : it is a datamember which holds or stores the data and whose value is not fixed. 2.constant : it is a datamemeber which holds or stores th data and the value is fixed. is

# CONSTRUCTOR A class constructor, if defined is called whenever a program creates an object of that class. A constructor is called only onc at the time of creating an instance.

# TWO TYPES OF CONSTRUCTORS

# Parameterized.
# Non-parameterized.
# The__init__() Method This is a magic method(dunder method) which we can use to inintialize variables for classes (objects). Every class has init and this is executed when we instantiate the class.

# SELF KEYWORD self is a default variable that contains the memory address of the current object.


# #1.
# class Student:
#     def __init__(self):
#         print('Student Object is Created')
# S1=Student()
# S2=Student()
# S3=Student()
# S4=Student()
# S5=Student()


#                                                    Variables
#                                 Global variable                Local variable
# Global variable : it is a variable which is declared within the class but outside of a method,constructor or block. it has global scope.
# Local variable : it is a variable which is declared within the class but inside of a constructor,method or block. it has limited/local slope.


#2.
# class Student:
#     def __init__(self,name,age,branch):
#         self.Stdname=name
#         self.Age=age
#         self.Branch=branch
# S1=Student("Scott",20,"CSE")
# print(f"Student Name is : {S1.Stdname}")  
# print(f"Student Age is : {S1.Age}")
# print(f"Student Branch is : {S1.Branch}")      

#3. 
# class Student:
#     def __init__(self,id,num,per):
#         self.Stdid=id
#         self.Stunum=num
#         self.Stuper=per
# S1=Student("22f21a3240",90909090,75)
# print(f"Student Id is : {S1.Stdid}")  
# print(f"Student Num is : {S1.Stunum}")
# print(f"Student Per is : {S1.Stuper}")      

#4. 
# class Student:
#     def __init__(self,name,age,branch):
#         self.Stdname=name
#         self.Age=age
#         self.Branch=branch
#     def display(self):
#         print(f"Student Name is : {self.Stdname}")  
#         print(f"Student Age is : {self.Age}")
#         print(f"Student Branch is : {self.Branch}")   
# S1=Student("Scott",20,"CSE")
# S1.display()  
# S2=Student("Adams",21,"ECE")
# S2.display()

#5. Employeenum,emplynum,designation,salry,deptnum create 5 objects and access the details of 5 employee objects using functions
# class Employee:
#     def __init__(self,EmpName,EmpNum,Designation,Salary,DeptNo):
#         self.EmpName=EmpName
#         self.EmpNum=EmpNum
#         self.Designation=Designation
#         self.Salary=Salary
#         self.DeptNo=DeptNo
#     def display(self):
#         print(f"Employee Name is : {self.EmpName}")  
#         print(f"Employee Num is : {self.EmpNum}")
#         print(f"Designation is : {self.Designation}")  
#         print(f"Salary is : {self.Salary}") 
#         print(f"DeptNo is : {self.DeptNo}")
# E1=Employee("Scott",20,"software designer",20000,1)
# E1.display()  
# E2=Employee("Sandy",10,"visual designer",10000,2)
# E2.display()


# TYPES OF METHODS
     #1. Instance Methods --Accesssor Methods --Mutator Methods
     #2. Class Methods
     #3. Static Methods
# Accessor Method This method is used to access or read data of the variables. This method do not modify the data in the variable. This is also called as getter method. ex : def get_value(self): def get_result(self): def get_name(self): def get_id(self):

# Mutator method This method is used to access or read and modify data of variable. This method modify the data in the variable. This is also called as setter method. ex : def set_value(self): def set_result(self): def set_name(self): def set_id(self):


#6.
# class Student:
#     def __init__(self):
#         print()
#         print("Student Object is Created....!")
#         print()
#     #mutator or setter methods
#     def set_name(self,name):
#         self.name=name
#     def set_age(self,age):
#         self.age=age
#     def set_branch(self,branch):
#         self.branch=branch
#     #accessor or getter methods
#     def get_name(self):
#         print(f"Student Name is : {self.name}")
#     def get_age(self):
#         print(f"Student Age is : {self.age}")
#     def get_branch(self):
#         print(f"Student branch is : {self.branch}")   
# S1=Student()
# S1.set_name("Scott")
# S1.set_age(21)
# S1.set_branch("CSE")
# S1.get_name()
# S1.get_age()
# S1.get_branch() 


###Class Methods:::
      #Class methods are the methods which act upon the class variables or static variable of the class. Decorator @classmethod need to write above the class method. By default, the frist parameter of class method is cls which refers to the class itself.


#7. 
#Class Method w/o Parameter
# class Mobile:
#     @classmethod                     #Decorator
#     def show_model(cls):             #Class Method 
#         print("RealMe X")
# realme = Mobile()
# realme.show_model()        


##Static Methods::::
    #Static Methods are used when some processing is related to the class but does not need the class or it's instances to perform any work. We use static method when we want to pass some values from outside and perform some action in the method. Decorator @staticmethod need to write above the static method.


#8.
#Static Method w/o Parameter
# class Mobile:
#     @staticmethod
#     def show_model():
#         print("Realme X")
# realme = Mobile()
# realme.show_model()   


##INHERITANCE ::
    #The mechanism of deriving a new class from an old one(existing class) such that the new class inherit all the members(variables and methods) of old class is called inheritance or derivation.

##Super Class and Sub Class:: 
    #The old class is referred to as the Super class and the new one is called the sub class. Parent Class -- Base Class or Super Class Child Class -- derived class or sub class


#9.
class Person:
    def __init__(self,Name,Age,Gender):
        print("Person Class Object is Created")
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
class Student(Person):
    def __init__(self,Name,Age,Gender,Id,Branch):
        super().__init__(Name,Age,Gender)
        self.Id=Id
        self.Branch=Branch
        print("Student class object is created")
s1=Student(1,2,3,4,5)                



