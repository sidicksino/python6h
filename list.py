# # Write a programme to get the largest number in the list 
# numbers = [5, 3, 9, 8, 12, 10, 37]
# max = numbers[0]

# for number in numbers:
#     if number > max:
#         max = number

# print(max)


# # Write a programme to remove the duplicate number
# numbers = [2, 2, 4, 5, 5, 3, 6, 7]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)




numbers1 = [2, 4, 5, 3, 6, 7]
# to add new number to the list 
numbers1.append(20)
# to insert number in any place you need
numbers1.insert(0,10)
# to remove the number 4
numbers1.remove(4)
# to remove all the number in the list
numbers1.clear()
# to remove le last item in the list 
numbers1.pop()
# to get the item of a number in the list
print(numbers1.index(5))
# to check if a number exist or not
print(50 in numbers1)
# to count the total number of a number in the list
print(numbers1.count(5))
# to sort a list 
numbers1.sort()
# to reverse the sorted list to dsc
numbers1.reverse()
# to copy the list of number to a new list 
numbers2 = numbers1.copy()

print(numbers1)
