# # import math 
# # # functions of math module:
# # print(dir(math))
# # print(math.factorial(5))
# # print(math.sqrt(16))
# # print(math.sin(math.pi/2))
# # print(math.cos(0))
# # print(math.ceil(3.7))
# # print(math.floor(3.7))  
# # print(math.log(100, 10))    
# # print(math.exp(1))  
# # print(math.gcd(48, 18))
# # print(math.lcm(12, 15))
# # print(math.isqrt(16))
# # print(math.degrees(math.pi/2))
# # print(math.radians(90))         
# # print(math.hypot(3, 4))
# # print(math.comb(5, 2))
# # print(math.perm(5, 2))
# # print(math.prod([1, 2, 3, 4]))
# # # # 1. Calculate the area of a circle with a radius of 5 units.
# # # radius = 5
# # # area = math.pi * radius ** 2
# # # print(f"The area of the circle with radius {radius} is: {area}")
# # gcd traditional way:
# # def gcd(a, b):
# #     while min(a, b) != 0:        
# #         a, b = b, a % b
# #     return a
# # print(gcd(4, 16))
# # a = int(input())
# # b = int(input())
# # while min(a, b) != 0:        
# #     a, b = b, a % b
# # lcm  = (a * b) // a
# # print(a)
# # print(lcm)
# # # PERFECT NUMBER: A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself). For example, 6 is a perfect number because its divisors are 1, 2, and 3, and their sum is 6. Another example is 28, which has divisors 1, 2, 4, 7, and 14, and their sum is also 28. Perfect numbers are relatively rare and have been studied in number theory for centuries.
# # def perfect_number(n):
# #     if n < 2:
# #         return False
# #     divisors_sum = sum(i for i in range(1, n) if n % i == 0)
# #     return divisors_sum == n
# # print(perfect_number(6))  
# # print(perfect_number(29)) 
# n = int(input())
# s = 0
# for i in range(1, n):
#     if n < 2:
#         print("False")
#     elif n % i == 0:
#         s = s.append(i)
#         if sum(s) == n:
#             print("True")
## leet code question no 1071, 1979, 914
#gcd of two strings:
def gcdOfStrings(str1, str2):    
    if str1 + str2 != str2 + str1:
        return ""
    else:
        from math import gcd
        length = gcd(len(str1), len(str2))
        return str1[:length]
print(gcdOfStrings("ABCABC", "ABC"))
Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"
gcd traditional way:
# # def gcd(a, b):
# #     while min(a, b) != 0:        
# #         a, b = b, a % b
# #     return a
# # print(gcd(4, 16))
# # a = int(input())
# # b = int(input())
# # while min(a, b) != 0:        
# #     a, b = b, a % b
# # lcm  = (a * b) // a
# # print(a)
# # print(lcm)
