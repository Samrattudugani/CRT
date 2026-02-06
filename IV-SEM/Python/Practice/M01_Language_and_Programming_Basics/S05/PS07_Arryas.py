import numpy as np
#a = np.array([10,20,30])
# print(a)
# print(np.max(a))
# print(np.min(a))
# print(np.sum(a))
# print(np.mean(a))
# print("Even numbers are :" ,np.arange(2,10,2))
# print("Odd num are :",np.arange(1,10,2))
##############################################################################################################
#################---SUM OF TWO ARRAYS---##############
# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# print(np.array(a))
# print(np.array(b))
# print([x + y for x, y in zip(a, b)]) #ZIP   
#### 1.THIRD MAXIMUM NUMBER #######################################################################
# a = list(set(map(int, input().split())))
# a.sort()
# if len(a) >= 3:
#     print(a[-3])
# else:
#     print(max(a))
#### 2.MONOTONIC OF ARRAY #########################################################################
n = list(map(int, input().split()))
inc = True
de = True
for i in range(1, len(n)):
    if n[i] > n[i - 1]:
        de = False
    if n[i] < n[i - 1]:
        inc = False
if inc or de:
    print("YES")
else:
    print("NO")
