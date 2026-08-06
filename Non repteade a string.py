text = input("Enter a string: ")

frequency = {}

# Count frequency of each character
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Find first non-repeated character
for char in text:
    if frequency[char] == 1:
        print("First non-repeated character:", char)
        break
else:
    print("No non-repeated character found.")