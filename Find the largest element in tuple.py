numbers = (10, 25, 45, 89, 12)
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("largest elements", largest)        
