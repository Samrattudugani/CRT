# 1Q)Amstrong number ?

# n = 123 

# 1 ** 3 + 2 **3 + 3 ** 3 
# 1 + 8 + 27 
# 36 
# 36 != n ==> False
# 153 = True 
# 1634 = True 


n = int(input())
r = 0 
l = len(str(n))
for i in str(n) :
    r += int(i) ** l
print(n == r)


# 2Q) Perfect number ? 

# n = 6 
# 1 + 2 + 3 = 6 


n = int(input()) 
res = 0 
i = 1 
while i < n :
    if n % i == 0 :   
        res += i 
    i += 1
print(n == res)


# 3Q)Strong number ?
