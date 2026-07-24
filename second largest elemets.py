numbers = (10, 50, 20, 80, 30)
largest = second = float('-inf')
for num in numbers:
  if num > largest:
    second = largest
    largest = num
  elif num > second and num != largest:
    second = num
print("second element", second)
