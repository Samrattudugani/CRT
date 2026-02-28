#### SQUARE PATTERN #########3
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*",end = " ")
#     print()
##### RIGHT TRIANGLE ####3
# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*" , end = " ")
#     print()
##### INVERTED TRIANGLE ######
# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print("*" , end = " ")
#     print()
###### 
# n = int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*" , end = " ")
#     print()
###### Triangle with numbers ####
# n = int(input())
# nu = 1
# for i in range(1,n+1):
#     for j in range(i):
#         print(nu, end = " ")
#         nu+=1
#     print()
##### INVERTED TRIANGLE with numbers######
# n = int(input())
# nu = 1
# for i in range(n):
#     for j in range(n-i):
#         print(nu , end = " ")
#         nu += 1
#     print()
# ##### 
# n = int(input())
# nu = 1
# for i in range(n,0,-1):
#     for j in range(i):
#         print(nu , end = " ")
#         nu += 1
#     print()
###### USING ALPHABETS #####
# n = int(input())
# for i in range(1,n+1):
#     s=65
#     for j in range(i):
#         print(chr(s),end = " ")
#         s+=1
#     print() 
# #############
# n = int(input())
# nu = 65
# for i in range(n):
#     for j in range(n-i):
#         print(chr(nu) , end = " ")
#         nu += 1
#     print()
# ****
# *  *
# *  *
# ****
###### HOLLOW SPHERE ######
n = int(input())
for i in range(n):#ROW
    for j in range(n):#col
        if i == j and j == i + 1 or i== j+1:
            print("*",end = " ")
        else:
            print(" ")

