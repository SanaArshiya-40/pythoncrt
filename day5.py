#1.
# string = input("Enter the String : ")
# print(string)
# print(string.upper())
# print(string.swapcase())

#2. Write a python program to read name of the user and print the length of the name and check if it is more than 5 characters
# name = input('Enter Your Name')
# print("Length of Name : ",len(name))
# res = "More than 5 characters" if (len(name)>5) else "Not More than 5 characters"
# print(res)

#3. Write a python program to check if the user entered name has the charcter a or not
# String = input("Enter the String : ")
# print(String)
# if "a" or "A" in String:
#         print("String has A character")
# else:
#         print("Dont have A character")

#4. Write a python program to check how many alphabets, how many digits and how many special characters are present in the user entered string
# String= input("Enter the String : ")
# print(String)
# alpha,digit,spclchar = 0,0,0
# for i in String:
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         digit +=1
#     else:
#         spclchar+=1
# print(f"Count of Alphabetic Characters is {alpha}")
# print(f"Count of Digit is {digit}")
# print(f"Count of Special Character is {spclchar}")

#5. write a python program to check the count of Vowels and consonents present in the user entered string
# String = input("Enter the String : ")
# vowel,consonent= 0,0
# for ch in String:
#     if ch.isalpha():
#         if ch in "aeiou":
#             vowel+=1
#         else:
#             consonent+=1
# print(f"Vowel Count is {vowel}")
# print(f"Consonent Count is {consonent}")

#6.
# Str = "PythonProgramming"
# print(Str)
# print(Str[0:6:])
# print(Str[2:6:])
# print(Str[0::+2])
# print(Str[1::+2])
# print(Str[6:13:])

#7. Write a python number to read your 12 digit aadhar number as input from the user and print the 12 digit number where the first 8 digits are hidden the last four digits visible
# adno = input("Enter Your Aadhar Number")
# print(f"Encrypted Aadhaar Number : {adno.replace(adno[0:9:],'XXXX XXXX')}")

#8. Tuple packing - when we create tuple with out brackets
# num = 10,20,30,40,50,60
# print(num)
# print(type(num))

#9. Tuple unpacking
# a,b,c,d,e,f=num
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

#10. write a python program to to read 2 integer vales as input from the user and swap the values of the two integers
           #1.using arithmetic operators
           #2.using third variable
           #3.without using any variable
# a = int(input("Enter the value of 1st integer"))
# b = int(input("Enter the value of 2nd integer"))
# print(f"Before Swapping : a = {a} , b = {b}")
# a = a + b
# b = a - b
# a = a - b
# print(f"After Swapping : a = {a} , b = {b}")

#
# a = int(input("Enter the value of 1st integer"))
# b = int(input("Enter the value of 2nd integer"))
# print(f"Before Swapping : a = {a} , b = {b}")
# temp = a
# a = b
# b = temp
# print(f"After Swapping : a = {a} , b = {b}")

#11. Write a python program to check weather the user entered integer is a prime number or not
# num = int(input("Enter the Integer Value : "))
# factor = 0
# for i in range(1, num+1):
#     if(num % i == 0):
#         factor += 1
# res = "Prime Number" if(factor == 2) else "Not a Prime Number"
# print(f"{num} is {res}")

#12. Write a python program to read an integer value as input from user and check whether it is a Prime Palindrome or not.
# num = int(input("Enter a Number"))
# pn, rem, rev = 0,0,0
# factor = 0
# pn = num
# while(pn!=0):
#     rem = pn % 10
#     rev = rev * 10 + rem
#     pn = pn // 10
# if(num==rev):
#     for i in range(1, num + 1):
#         if(num %i == 0):
#             factor+=1
# res = "Prime Palindrom" if (factor == 2 and num == rev) else "Not a Prime Palindrome"
# print(res)

#13. Write a python program to read 2 integer values as input from the user and perform addition without using addition and without using built in function.
# a = int(input("Enter the first digit : "))
# b = int(input("Enter the second digit : "))
# sum = a - (-b)
# print(f"Summation : {sum}")

#14. Write a python program to print all 3 digit palindrome numbers
for i in range(1,10):
    for j in range(0,10):
        print(f"{i}{j}{i}", end = ",")