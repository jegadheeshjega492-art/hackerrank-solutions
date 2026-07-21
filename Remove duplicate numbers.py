numbers = [10, 20, 30, 20, 40, 30, 50, 60]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)        