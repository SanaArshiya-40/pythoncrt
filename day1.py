# 1 #program to read 2 numbers as input and find summation
# num1=int(input('Enter the first number :'))
# num2=int(input('Enter the second number :'))
# print(f"Summation : {num1+num2}")


# 2 #write a python program to read an integer value and check whether it is a digit or number 
# num=int(input('Enter the integer :'))
# #if-else
# if (num>=-9 and num<=9):
#     print("Digit")
# else :
#     print('Number')
#ternary operator :::
# res = "Digit" if(num>=-9 and num<=9) else "Number"
# print(res)


# 3 #write a python program to read an integer as input from user and check whether it is a 2 digit number or not a 2 digit number
# dig = int(input('Enter a number :'))
# res = "2 Digit number" if ((dig >=-99 and dig <=-10) or (dig >= 10 and dig <= 99)) else "Number"
# print(res)


# 4 #write a python program to read an integer as input from user and check whether it is a 3 digit number or not a 3 digit number
# dig = int(input('Enter a number :'))
# res = "3 Digit number" if ((dig >=-999 and dig <-99) or (dig > 99 and dig <= 999)) else "Number"
# print(res)


# 5 #write a python program to read an integer as input from user and check whether it is a 4 digit number or not a 4 digit number
# dig = int(input('Enter a number :'))
# res = "4 Digit number" if ((dig >=-9999 and dig <=-1000) or (dig >= 1000 and dig <= 9999)) else "not a 4 digit number"
# print(res)


# 6 #write a python program to read 2 integer values as input and find largest using if-else and ternary
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# #if-else
# if (a>b):
#     print(f"{a} is the largest")
# else:
#     print(f"{b} is the largest")
# #ternary operator:::
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# res = "a is the largest" if (a>b) else "b is the largest"
# print(res)


# 7 #write a python program to read 2 integer values as input user and find smallest number
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# res = a if (a>b) else b 
# print(res)


# 8 #write a python program to read 3 integer values as input user and find largest number
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# c = int(input('Enter third number:'))
#  #if-else
# if (a>b and a>c):
#   print(f"{a} is the largest")
# elif (b>a and b>c):
#   print(f"{b} is the largest")
# else:
#   print(f"{c} is largest")
#ternary operator:::
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# c = int(input('Enter third number:'))
# big = a if(a>b and a>c) else b
# res = c if (c>big) else big
# print(res)


# 9 #write a python program to read 3 integer values as input user and find smallest number using both if-else and ternary operator
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# c = int(input('Enter third number:'))
# #if-else
# if (a<b and a<c):
#   print(f"{a} is the smallest")
# elif (b<a and b<c):
#   print(f"{b} is the smallest")
# else:
#    print(f"{c} is smallest")
# #ternary operator:::
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# c = int(input('Enter third number:'))
# small = a if(a<b and a<c) else b
# res = c if (c<small) else small
# print(res)


# 10 #write a python program to read 3 integer values as input user and find middle number using both if-else and ternary operator
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# c = int(input('Enter third number:'))
# #if-else
# if (a>b and a<c):
#   print(f"{a} is the middle numbert")
# elif (b>a and b<c):
#   print(f"{b} is the middle number")
# else:
#    print(f"{c} is middle number")
# #ternary operator:::
# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# c = int(input('Enter third number:'))
# middle = a if(a>b and a<c) else b
# res = c if (c<middle) else middle
# print(res)


# 11 # write a python program to read the month number as input from the user and check whether it is a valid month number or not
# mon = int(input('Enter month number:'))
# res = "Valid month" if (mon>0 and mon<=12) else "Invalid month number"
# print(res)


# 12 # write a python program to read month number as input frpm the user and print the respective number of days present in that particular month
# mon = int(input('Enter month number: '))
# if(mon==1 or mon==3 or mon==5 or mon==7 or mon==8 or mon==10 or mon==12):
#     print("31 Days")
# elif(mon==2):
#     print("28 or 29 Days")
# elif(mon==4 or mon==6 or mon==9 or mon==11):
#     print("30 Days")
# else:
#     print("Invalid month number")


# 13 #write a python program to check whether the user entered age is eligible to vote or not
# age = int(input("Enter your age:"))
# if (age>=18):
#     print("Eligible to vote")
# elif(age<18 and age>0):
#     print("Not eligible to vote")
# else:
#     print("Invalid input")


# 14 #write a py program to read an integer value as integer from user and check whether it is even or odd
# a = int(input('Enter a number:'))
# if(a % 2 == 0 and a!= 0):
#     print("Even")
# elif(a==0):
#     print("Not even or odd")
# else:
#     print("odd")


# 15 # write a py program to read an integer values input from user and check whether it is multiple of 3 and 5 or not
# a = int(input('Enter a number:'))
# if(a%3==0 and a%5==0):
#     print("Divisible by 3 and 5")
# else:
#     print("Not Divisible by 3 and 5 ")


# 16 # write a py program to read an integer value as input and print fizzbuzz if divisible by 3&5, fizz  if by 3 and buzz if by 5
# a = int(input('Enter a number:'))
# if(a%3==0 and a%5==0):
#     print("FizzBuzz")
# elif(a%3==0):
#     print("Fizz")
# elif(a%5==0):
#     print("Buzz")


# 17 #write a python program to read amount as input from user and print no' of notes required in indian currency dimension
# amt = int(input('Enter amount:'))
# print("No of 500 notes:" , amt//500)
# amt = amt%500
# print("No of 200 notes:" , amt//200)
# amt = amt%200
# print("No of 100 notes:" , amt//100)
# amt = amt%100
# print("No of 50 notes:" , amt//50)
# amt = amt%50
# print("No of 20 notes:" , amt//20)
# amt = amt%20
# print("No of 10 notes:" , amt//10)
# amt = amt%10
# print("No of 5 notes:" , amt//5)
# amt = amt%5
# print("No of 2 notes:" , amt//2)
# amt = amt%2
# print("No of 1 notes:" , amt//1)