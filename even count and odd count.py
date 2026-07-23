numbers = (10, 20, 30, 40, 45, 50, 60, 70, 75, 80)
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even +=1
else:
    odd+=1

print("even count", even)
print("odd count", odd)            


