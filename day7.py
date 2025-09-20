#1
# num=[]
# for i in range(1,11):
#     num.append(i)
# print(num)    

#2 List comprehension
# num=[val for val in range(1,11)]
# print(num)

#3 write the py program to print a list of even numbers form 1 to n using list comprehension
# n=int(input("Enter the value :"))
# num=[val for val in range(2,n,2)]
# print(num)
#....
# n=int(input("Enter the value :"))
# num=[val for val in range(1,n) if val%2==0]
# print(num)


#FILTER::: 
  #filter(function_name,iterable)
#REDUCE:::
  #syntax:from functools import reduce(function_name,sequence)
  # Anonnyms Function or Lambda ...A function without a name is called Anonymous Function.It is also called as Lambda Function. Anonymous Function we donot use def to define function but we use lamba keywoed for defining the func.


#4 write a py function to print the square values of n
# def square(n):
#     print(n*n)
# square(10)
# #lambda func
# x=lambda n:print(n*n) 
# x(10)   

#5 write a lambda func to add 10 to a num
# add=lambda n:n+10
# print(add(7))

#6 write a py program to check whether the user entered integer is even using lambda func
# even=lambda n:n%2==0
# print(even(24))
# print(even(27))

#7 write a python program to square numbers in the list using lambda func
# num=[1,2,3,4,5,6,7,8,9,10]
# square=lambda :[val*val for val in num]
# print(square())

#8 Doubling of numbers in list
# num=[1,2,3,4,5,6,7,8,9,10]
# res=lambda :[val+val for val in num]
# print(res())
#....
# num=[1,2,3,4,5,6,7,8,9,10]
# res=[]
# for i in num:
#     val=i+i
#     res.append(val)
# print(res)
#....
# num=[1,2,3,4,5,6,7,8,9,10] 
# res=[i+i for i in num]
# print(res)
#....
# num=[1,2,3,4,5,6,7,8,9,10]
# def double(n):
#     return n+n
# res=list(map(double,num))
# print(res)

#9 write a py program to read the list pf words as input from the user and written the length of each word for the list
# size=int(input("Enter the size of list :"))
# WordList=[]
# for i in range(size):
#     val=input("Enter the word :")
#     WordList.append(val)
# print("User Entered List is :",WordList)
# Len=list(map(lambda w:len(w),WordList))
# print("Length of the words in the list :",Len)

#10 write a py program to read 3 integer values as input in same line and print the summation of it
# num=list(map(int,input("Enter the numbers :").split()))
# print(num)
# print(sum(num))

#11 write a py program to read a list of elements as input from the user & print the square values of list elememts without loops
# li=list(map(int,input("Enter the list of elements :").split()))
# print("The user Entered list: ",li)
# print("List of square of each element:",list(map(lambda x: x*x,li)))

#12 write a py program to read a list of numbers and print the list of even numbers and odd numbers without using loops and conditional statements
# num=list(map(int,input("Enter the numbers :").split()))
# even=list(filter(lambda i:i%2==0,num))
# odd=list(filter(lambda i:i%2!=0,num))
# print(f"User Entered List : {num}")
# print(f"Even List : {even}")
# print(f"Odd List : {odd}")

#13 Sales Data Analysis
# Sales=list(map(int,input("Enter the sales for a week:").split(",")))
# print(max(Sales))
# print(sum(Sales))

#14 Marks Average
# Marks=tuple(map(int,input("Enter 3 subjects marks:").split()))
# avg=sum(Marks)/3
# res=list(map(lambda i:i>=35,Marks))
# res="Failed" if(False in res) else "Passed"
# print(f"Average : {avg}")
# print(res)

#15 Movie ticket booking
age=list(map(int,input("Enter the age of people:").split()))
res=[]
for i in age:
    if i<=12:
        res.append(150)
    elif 13<=i<=59:
        res.append(250) 
    elif i>=60:
        res.append(200)
print(sum(res))             
