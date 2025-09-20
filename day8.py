#####PATTERN SOLVING PROBLEMS#####
## i loop represents num of lines
## j loop represnts numof stars

#1.Enter the value of n : 5 * * * * * * * * * * * * * * * * * * * * * * * * *
# print(N stars in each column and n rows)
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("* ",end="")
#     print()    

#2.Enter the value of n : 5 * * * * * * * * * * * * * * *
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()    

#3
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()   

#4
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)
      
#5
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     print("  "*(n-i)+"* "*i)
      
#6
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     print(" "*(n-i)+" *"*i)
      
#7
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     print(" "*(n-i)+" *"*i)
      
#8
# n=int(input("Enter the value : "))
# for i in range(1,n):
#     print(" "*(n-i)+" *"*i)
# for j in range(n,0,-1):    
#     print(" "*(n-j)+" *"*j)

#9
# n=int(input("Enter the value : "))
# for i in range(1,n+1,2):
#     print(" "*(n-i) +"* "*i)
# print()    

#10
# n=int(input("Enter the value : "))
# for i in range(n,0,-2):
#     print(" "*(n-i) +"* "*i)
# print()    

#11
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{i}",end="")
#     print()    

#12
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     print(f"{i}"*n,end=" ")
#     print()    

#13
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{j}",end="")
#     print()   

#14
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     print(f"{i}"*i,end=" ")
#     print()

#15
n=int(input("Enter the value of : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{j}",end="")
    print()