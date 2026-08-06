text = input("Enter a string: ")

frequency = {}

# Count frequency of each character
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Sort characters by frequency (highest to lowest)
sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# Print second most frequent character
if len(sorted_freq) >= 2:
    print("Second most frequent character:", sorted_freq[1][0])
    print("Frequency:", sorted_freq[1][1])
else:
    print("No second most frequent character.")