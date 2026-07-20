numbers = [10, 25, 40, 30 ,15]
second = largest = float('-inf')
for num in numbers:
    if num > largest:
        second = largestlargest = num
    elif num > second and num != largest:
        second = num 
print('second largest', second)            