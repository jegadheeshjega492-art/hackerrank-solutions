num = int(input(" Enter the number: "))

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3 
    temp = temp // 10

if total == 0:
    print(" Armstrong number")

else:
    print(" Not a armstrong number")    