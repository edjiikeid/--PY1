list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_ = list_numbers[0]
i = 0
for max1_ in list_numbers:
    if max1_ > max_:
        max_ = max1_
        p = i
    i +=1
x = list_numbers[p]
list_numbers[p] = list_numbers[-1]
list_numbers[-1] = x
print(list_numbers)
