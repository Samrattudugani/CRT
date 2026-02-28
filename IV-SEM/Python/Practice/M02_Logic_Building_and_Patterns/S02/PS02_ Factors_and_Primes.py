## 1.DISPLAY THE NO.OF FACTORS OF THE GIVEN NUMBER #############
# n = int(input())
# c = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         c+=1
#         print(i , end = " ") ## to know the values
# print()
# print("THE NO.OF FACTORS ARE ",c) ## to know the count 
# n = int(input())
# r = 0
# while(n > 0):
#     r = r*10 + n % 10
#     n//=10
# print(r)
###### 
# n = int(input())
# if n >= 0:
#     print(int(str(n)[::-1]))
# else:
#     n = -1*n 
#     print(-1 * int(str(n)[::-1])) 
###################################
# n = int(input())
# if n < 0:
#     n = -1 * n
# print(-1 * int(str(n)[::-1]))
#### 2. GIVEN NUM IS PRIME OR NOT ###########
n = int(input())
c = 0
for i in range(1,n+1):
    if n % i == 0:
        c += 1
    else:
        c += 0
if c == 2:
    print("PRIME")
else:
    print("NOT PRIME NUM")
