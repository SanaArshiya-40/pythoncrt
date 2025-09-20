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
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(f"{j}",end="")
#     print()

#16
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(f"{i}",end=" ")
#     print()  

#17
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(f"{j}",end="")
#     print()    

#18
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(f"{i}",end="")
#     print()    

#19
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(f"{i}",end="")
#     print()    

#20
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(f"{j}",end="")
#     print()   

#21
# n=int(input("Enter the value : "))
# k=1
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(f"{k}",end="")
#     k+=1    
#     print()

#22
# n=int(input("Enter the value of : "))
# for i in range(n,0,-1):
#     for j in range(n,i-1,-1):
#         print(f"{j}",end="")
#     print()

#23
# n=int(input("Enter the value : "))
# for i in range(n):
#     print("  "* i,end= "")
#     for j in range(n,i,-1):
#         print(j,end=" ")
#     print() 

#24
# n=int(input("Enter the value : "))
# for i in range(n):
#     print("  "* i,end= "")
#     for j in range(1,n-i+1):
#         print(f"{j}",end=" ")  
#     print() 

#25
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     print("  "*(n-i),end= "")
#     for j in range(i,0,-1):
#         print(f"{i}",end=" ")  
#     print() 

#26
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(f"{j}",end=" ")  
#     print() 

#27
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(f"{j}",end=" ")  
#     print() 

#28
# n=int(input("Enter the value : "))
# for i in range(1,n):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(f"{j}",end=" ") 
#     print()     
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(f"{j}",end=" ")  
#     print() 

#29
# for ch in range(26):
#     print(chr(ch+65))

#30
# for ch in range(26):
#     print(chr(ch+97),end=" ")

#31
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(i+64),end=" ")
#     print()  

#32
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(chr(i+64),end=" ")
#     print() 

#33
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         print(chr(i+64),end=" ")
#     print()    

#34
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(chr(i+64),end=" ")
#     print()

#35
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         print(chr(j+64),end=" ")
#     print() 

#36
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         print(chr(j+64),end=" ")
#     print() 

#37
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(i+96),end=" ")
#     print() 

#38
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         print(chr(i+96),end=" ")
#     print()

#39
# n=(int(input("Enter the value : ")))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(j+96),end=" ")
#     print() 

#40
# n=(int(input("Enter the value : ")))
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         print(chr(j+96),end=" ")
#     print()    

#41
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(chr(i+64),end=" ")
#     print()

#42
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(chr(j+64),end=" ")
#     print() 

#43
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(chr(j+64),end=" ")
#     print() 

#44
# n=int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i%2==0):
#             print("* ",end="")
#         else:    
#             print(chr(i+64),end=" ")
#     print()  

#45
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(i+64),end=" ")
#     print()

#46
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(i+96),end=" ")
#     print()

#47
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(j+64),end=" ")
#     print()

#48
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(j+96),end=" ")
#     print()

#49
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(chr(i+96),end=" ")
#     print() 

#50
# n=int(input("Enter the value of : "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(chr(j+64),end=" ")
#     print()

#51
# n=int(input("Enter the value of : "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(chr(j+96),end=" ")
#     print()

#52
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(i+64),end="")
#     print()

#53
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(j+64),end="")
#     print()

#54
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(i+96),end="")
#     print()

#55
# n=int(input("Enter the value of : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(j+96),end="")
#     print()

#56
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(i+96),end="")
#     print() 

#57
# n=int(input("Enter the value : "))
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(i+64),end="")
#     print() 

#58
# n=int(input("Enter the value of : "))
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(j+96),end="")
#     print()

#59
# n=int(input("Enter the value of : "))
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(j+64),end="")
#     print()