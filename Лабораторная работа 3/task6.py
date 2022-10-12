list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# finds max number from the list of numbers
max_num = max(list_numbers)
# finds the index of max number
for i, num in enumerate(list_numbers):
    if num == max_num:
        idx_max = i
# adjusts positions of two elements from the list
list_numbers[-1], list_numbers[idx_max] = list_numbers[idx_max], list_numbers[-1]
# print new list of numbers
print(list_numbers)
