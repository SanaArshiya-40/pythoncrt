#1 def display():
#     print('Python')
#     print('Java')
#     print('SQL')
#     print('c++')
# display()

#2
# def arithmetic_operations(a,b):
#     print(f"Addition = {a+b}")
#     print(f"Substraction = {a-b}")
#     print(f"Multiplication = {a*b}")
#     print(f"Division = {a/b}")
#     print(f"Division = {a//b}")
#     print(f"Division = {a%b}")
# arithmetic_operations(5,10)

#3
# def add(a,b):
#     return a+b
# print(add(10,20))
# res = add(30,40)
# print(res)

#4 write a python program to print(multiplication table of n)
# def mul_table(a):
#     print(f"Multiplication table of {a}:")
#     for i in range(1,11):
#         print(f"{a} X {i} = {a*i}")
#     print()
# mul_table(45)
# mul_table(7)

#5 
# def mul(a):
#     i=1
#     while(i<11):
#         print(f"{a} X {i} = {a*i}")
#         i+=1
# mul(25)

#6 write a python program to calculate the simple interest by using a parameterised function
# def cal_si(p,t,r):
#     interest =  (p*t*r)/100
#     print(f"Simple Interest : {interest}")

# cal_si(12345,2,32)


###Complexities

  #1.Time Complexity : Time complexity is used to measure the amount of time required to execute the code
  #2.Space complexity : Space complexity means the amount of space required to execute successfully the functionalities of the code
#Notations:

  #1.Big - O notation: worst case scenario
  #2.Omega Notation : Best - Case scenario
  #3.Theta Notation : the avarage complexity of an algorithm

#7 Write a python program to read the size of the list as input from the user and read the list elements as a input from the user and print the user entered list
# n = int(input("Enter the size of the list"))
# List = []
# for i in range(n):
#     val=int(input(f"Enter the element for {i} index :"))
#     List.append(val)
# print(f"User Defined list : ")
# print(List)

#8 Write a python program to read a list as input from the user and read the list elements as alphabetic characters and print the user entered list and the sorted version of the user entered list.
n = int(input("Enter the size of the list"))
List = []
for i in range(n):
    val=input(f"Enter the element at {i} index : ")
    List.append(val)
print(f"User Entered List is : a{List}")
List.sort()
print()
print(List)