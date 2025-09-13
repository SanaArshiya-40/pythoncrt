# #write a py program to print the sum of natural numbers from 1 to n
# n = int(input("Enter the n value :"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"Summation is {sum}")


# #write a py program to find factorial of n
# n = int(input("Enter the n value:"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(f"Factorial of {n} is {fact}")


# #write a py program and print the count of digits present in the user entered number
# n = int(input('Enter the digit value:'))
# digit_count = 0
# while(n!=0):
#     n = n//10
#     digit_count += 1
# print(f"Digit count is {digit_count}")


# #Write a py program to print the count of even digits and odd digits present in the user entered number
# n = int(input("Enter the number:"))
# even, odd = 0,0
# while(n!=0):
#     rem = n%10
#     if rem % 2 == 0:
#         even += 1
#     else :
#         odd += 1
#     n = n//10
# print(f"Even digits = {even}")
# print(f"Odd digits = {odd}")    


# #write a py program to read an integer value as input from the user and print reverse of it
# n = int(input("Enter the digit :"))
# rem,rev = 0, 0
# print(f"User enter number {n}")
# while(n!=0):
#     rem = n %  10
#     rev = rev * 10 + rem
#     n=n//10
# print(f"Reversed Number is {rev}")    


# #write a py program to check the user entered integer is a palindrome number or not
# n = int(input("Enter the number:"))
# pn, rem, rev = 0,0,0
# pn = n
# print(f"User defined number {n}")
# while(pn!=0):
#     rem = pn % 10
#     rev = rev * 10 + rem
#     pn = pn // 10
# print(f"Reverse = {rev}")
# if(n==rev):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# #      -5  -4 -3 -2 -1
# num = [10,20,30,40,50]
# #       0  1  2  3  4
# print(num, type(num))
# print("accessing the list elements using +ve indexing :")
# print(num[0],num[1],num[2],num[3],num[4])
# print("accessing the list elements using +ve indexing :")
# print(num[-5],num[-4],num[-3],num[-2],num[-1])


# ##LIST SLICING
# '''
# [stop]
# [start:stop]
# [start:stop:stepsize]
# '''
# lang = ['Python','Java','Ruby','Golang','HTML','JS','SOL','C','C++']

# print(lang[:4])
# print(lang[3:-1])
# print(lang[4:8])
# print(lang[::-1])


# #acessing list using for and while loop
# lis = ['REd','Green','YEllow','Blue','Orange','Pink','White','Purple']
# for i in lis:
#     print(i)
#     # print(i, enr =" ") # for output in same line
# n = 0
# print()
# while(n<len(lis)):
#     print(lis[n])
#     n += 1


# #Deleting operation in a list
# br = ['CSE','ECE','EEE','CE','MECH','CSD','CSC','CAI']
# print(br)
# print(f"after deleting: {br[6]}")
# del br[6]
# print(br)
# del br #list will be deleted


# #Built in Function
# li = [50,40,30,20,10]
# print(f"Original list: {li}")
# print(f"length of list: {len(li)}")
# print(f"max of list: {max(li)}")
# print(f"min of list: {min(li)}")

# print(f"Sorted list : {sorted(li)}")
# print(any(li))
# print(all(li))


#USING BUILT IN METHODS

# #Append()
# li=[10,20,30]
# print(li)
# li.append(50)
# print(li)
# li.append(70)
# print(li)


# #insert()
# li = [10,20,30]
# print(li)
# li.insert(0,5)
# print(li)


# #pop() - based on idex
# li = [10,20,30,40,50]
# print(li)
# li.pop()
# print(li)
# li.pop(-4)
# print(li)


# #remove() - based on value
# li = [50,40,30,20,10,10]
# print(li)
# li.remove(10)
# print(li)
# li.remove(10)
# print(li)


# #reverse()
# li = [50,40,30,20,10]
# print(li)
# li.reverse()
# print(li)


# #sort()
# li = [5,4,3,2,1]
# print(li)
# li.sort()
# print(li)
# print("Descending Order")
# li.reverse()
# print(li)


# #extend() - add 2 lists
# a = [12,24,36]
# b = [48,60,72]
# b.extend(a)
# print(b)


# a = [12,24,36]
# print(a+a+a+a)#concatination
# print(a*10)#repetition


# #write a py program to print the square values of 1 to n using for & while loop
# n = int(input())
# for i in range(1,n+1):
#     print(i*i)

#while loop
n = int(input())
i = 1
while(i<=n):
    print(i*i)
    i += 1