# #3. Count Even Numbers:
# a = [1, 2, 3, 4, 5, 6]
# # count_even = sum(1 for num in a if num % 2 == 0)
# # print(count_even)
# r = list(filter(lambda x: x % 2 == 0, a))
# print(len(r))
# #4 Sum of digits in a number:
# num = 12345
# r = sum(int(i) for i in str(num))
# print(r)
#5. START WORDS Alphabetically: using sorted function
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words)
print(sorted_words)
print(list(sorted_words))
# index with value using enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")    
#zip function to combine two lists 
# 6. Zip Function:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))
#7. find common elements in two lists using set intersection
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1) & set(list2)
print(common_elements)  
#8. find second largest number in a list
numbers = [5, 2, 9, 1, 5, 6]
unique_numbers = set(numbers)
unique_numbers.remove(max(unique_numbers))
second_largest = max(unique_numbers)
print(second_largest)   