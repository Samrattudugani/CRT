# l = [1,2,3,4,5]
# output : [1,4,9,16,25]
# li = []
# for i in (l):
#     li.append(i**2)
# print(li)
# ################
# res = [i**2 for i in l if i % 2==0 ]
# print(res)
# #############
# r = []
# for i in l:
#     if i % 2 == 0:
#         r.append(i**2)
# print(r)
# #########################
# concate strings####################3
# li = ['a','b','c']
# output : 'a b c'
# r = ""
# for c in li:
#     r = r + c +" "
# print(r)
# # JOIN METHOD ##
# print("#".join(li))
# ########################################
# 1.PYRAMID
# N = 4
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"* " * i)
# ######## INVERTED PYRAMID ##########
# n = int(input("Enter number of rows: "))
# for i in range(n):
#     print(" " * i + "* " * (n - i))
# ####### Daimond ##############
# n = int(input())
# for i in range(1, n+1):
#     print(" "*(n-i) + "* " * i)
# for i in range(1, n):
#     print(" " * i + "* " * (n - i))
### num pyramid ############
# n = int(input())
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print() 
###### CONTINOUS NUM PYRAMID ######
# n = int(input())
# c = 1
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(i):
#         print(c, end=" ")
#         c += 1
#     print()
#### BUTTERFLY ###############
n = int(input("Enter rows: "))

for i in range(1, n+1):
    print("*" * i + " " * (2*(n-i)) + "*" * i)

for i in range(n-1, 0, -1):
    print("*" * i + " " * (2*(n-i)) + "*" * i)





















