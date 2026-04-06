# # n = [1,2,3,4,4,5,6,6,7]
# n= [1, 2, 3, 4, 5, 6, 7]
# def check_duplicates(nums):
#     for i in range(len(nums)):    TIME COMPLEXITY O(n^2)
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# print(check_duplicates(n))
# REDUCING TIME COMLEXITY TO O(n)
# n=[1,2,3,3,4,5,5,6,5,4,3,21,345]
n = [1,2,3,4]
def c_d(nums):
    s = set()
    for i in nums:
        if i in s:
            return True 
        s.add(i)
    return False
print(c_d(n))












# def check_duplicates(nums):
#     s = set()  # Create an empty set to store seen numbers
#     for num in nums:  # Iterate through each number in the list
#         if num in s:  # Check if the number is already in the set
#             return True  # If it is, we have a duplicate
#         s.add(num)  # Add the number to the set
#     return False  # If we finish the loop without finding duplicates, return False