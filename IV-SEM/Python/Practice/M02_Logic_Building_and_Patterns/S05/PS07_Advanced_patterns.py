
# 1. Pascal Triangle
# n=5
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# n = int(input())
# for i in range(n):
#     num = 1
#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j+1)
#     print()
# 2. Butterfly Pattern
# n=4
# Output:
# *      *
# **    **
# ***  ***
# ********
# ********
# ***  ***
# **    **
# *      *
# n = int(input())
# for i in range(1, n + 1):
#     print("*" * i + " " * (2 * (n - i)) + "*" * i)
# for i in range(n, 0, -1):
#     print("*" * i + " " * (2 * (n - i)) + "*" * i)
# 3. Hourglass Pattern
# n=4
# Output:
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
n = int(input())

# Upper half
for i in range(n, 0, -1):
    print("* " * i)

# Lower half
for i in range(2, n + 1):
    print("* " * i)
# 4. Concentric Square
# n=3
# Output:
# 3 3 3 3 3
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3
# 3 3 3 3 3
n = int(input())
size = 2 * n - 1

for i in range(size):
    for j in range(size):
        value = n - min(i, j, size - i - 1, size - j - 1)
        print(value, end=" ")
    print()
# 5. Snake Pattern
# n=4
# Output:
# 1 2 3 4
# 8 7 6 5
# 9 10 11 12
# 16 15 14 13
n = int(input())
num = 1

for i in range(n):
    row = []
    for j in range(n):
        row.append(num)
        num += 1
    
    if i % 2 != 0:
        row.reverse()
    
    print(*row)

# 6. Spiral Matrix
# n=3
# Output:
# [1, 2, 3]
# [8, 9, 4]
# [7, 6, 5]
n = int(input())
matrix = [[0]*n for _ in range(n)]

top, bottom = 0, n-1
left, right = 0, n-1
num = 1

while top <= bottom and left <= right:
    
    for i in range(left, right+1):
        matrix[top][i] = num
        num += 1
    top += 1
    
    for i in range(top, bottom+1):
        matrix[i][right] = num
        num += 1
    right -= 1
    
    for i in range(right, left-1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    
    for i in range(bottom, top-1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(row)

# 7. Number Spiral
# n=5
# Output:
# [1, 2, 3, 4, 5]
# [16,17,18,19,6]
# [15,24,25,20,7]
# [14,23,22,21,8]
# [13,12,11,10,9]
n = int(input())
matrix = [[0]*n for _ in range(n)]

top, bottom = 0, n-1
left, right = 0, n-1
num = 1

while top <= bottom and left <= right:
    
    for i in range(left, right+1):
        matrix[top][i] = num
        num += 1
    top += 1
    
    for i in range(top, bottom+1):
        matrix[i][right] = num
        num += 1
    right -= 1
    
    for i in range(right, left-1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    
    for i in range(bottom, top-1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(row)

# 8. X Pattern Numbers
# n=5
# Output:
# 1       1
#  2   2
#    3
#  4   4
# 5       5
n = int(input())

for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print(i + 1, end="")
        else:
            print(" ", end="")
    print()

# 9. Hollow Butterfly
# n=4
# Output:
# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *     
n = int(input())

# Upper half
for i in range(1, n+1):
    print("*" * i + " " * (2*(n-i)) + "*" * i)

# Lower half
for i in range(n-1, 0, -1):
    print("*" * i + " " * (2*(n-i)) + "*" * i)