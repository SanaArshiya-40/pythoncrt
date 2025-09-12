###Real time scenerios and iterative statements

# 1 #ATM Withdrawal validation you are designing an ATM system. A customer enters the amount to withdraw-the withdrawal amount must ne less than or equal to the account balance(5k)-the amt must be multiple of 100-if both conditions are true,aloow withdrawal-otherwise display("Insufficient balance")
# amt = int(input("Enter the amount to withdraw:"))
# if(amt<=5000):
#     if(amt%100==0):
#         print("Withdrawal successfull")
#     else:
#         print("Amount should be multiple of 100")
# else:
#     print("Insufficient Balance")


# 2 #signal color as input and print statements according to that color
# color = input("Enter the color:").lower() #.lower
# if(color=="red"):
#    print("Stop Immediately")
# elif(color=="yellow"):
#    print("Get ready to move")
# elif(color=="green"):
#    print("You can go")


# 3 #Movie Ticket Pricing in theater , ticket prices vary depending on customers age-(<12) print 150rs-(>12 and <18) print 200-(>18) print 300rs
# age = int(input("Enter the age:"))
# if(0<age<=12):
#     print("150/-")
# elif(12<age<18):
#     print("200/-")
# elif(age>18):
#     print("300/-")
# else:
#     print("Invalid age")


# 4 #Employee overtime pay standard 8 hrs-if morethan 8 100rs for each extra hour-else no overtime pay
# time = int(input("Enter working hours:"))
# if(time>8):
#     print("100rS for each extra hour")
# else:
#     print("no overtime pay")


# 5 #Restaurant Discount system a restaurent gives discount based on the total bill:-iff > 1000rs--10% discount-if bill > 500rs--5% discount- if bill<=500rs--no discount write program that calculates and displays the final amount after discount
# amt=int(input("Enter the bill amount:"))
# if(amt>1000):
#     dis=amt*0.1
#     amt=amt-dis
#     print(amt)
# elif(amt>500):
#     dis=amt*0.05
#     amt=amt-dis
#     print(amt)
# elif(amt<=500):
#     print("No discount")
#     print(amt)


# 6 #Water reminder app
# hrs = int(input("Enter hours since you drink water"))
# if(hrs>=4):
#     print("You are dehydrated! Drink water now!")
# elif(2<=hrs<=3):
#     print("Drink a glass of water")
# elif(hrs<2):
#     print("you're fine")


# 7 #
# List=[10,20,30,40,50]
# Tupple=(10,20,30,40,50)
# Set={10,20,30,40,50}
# print(List,type(List))
# print(Tupple,type(Tupple))
# print(Set,type(Set))


# 8 ##range(Stop)
# #range(Strt,Stop)
# #range(Strt,stop,Stepsize)
# R1=range(10)
# print(R1)
# print(type(R1))


# for i in range(10):
#     print(i)


# for i in range(10,21):
#     print(i)


# #write a py program to print the natural numbers from 1 to n,where n is the users input
# n=int(input('Enter the integer value:'))
# print(f"Natural Numbers from 1 to {n}:")
# for i in range(1,n+1):
#     print(i)


# #write a py program to print natural numbers from n to 1
# n=int(input('Enter the integer value:'))
# for i in range(n,0,-1):
#     print(i)


# #write a py program to print even numbers from 1 to n
# n=int(input('Enter the integer value :'))
# print(f"Even numbers from 1 to {n}")
# for i in range(2,n+1,2):
#     print(i)


# #write a py program to print even numbers from n to 1
# n=int(input('Enter the integer value :'))
# print(f"Even numbers from n to {1}")
# for i in range(n,0,-1):
#     if(i%2==0):
#         print(i)


# #write a py program to print odd numbers from 1 to n
# n=int(input('Enter the integer value :'))
# print(f"odd numbers from 1 to {n}")
# for i in range(1,n+1,2):
#         print(i)


# #write a py program to print odd numbers from n to 1
# n=int(input('Enter the integer value :'))
# print(f"odd numbers from n to {1}")
# for i in range(n,1,-1):
#     if(i%2!=0):
#         print(i)


#write a py program to print the multiplication table of n
n=int(input("Enter a Integer:"))
print(f"Multiplication table of {n}")
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")