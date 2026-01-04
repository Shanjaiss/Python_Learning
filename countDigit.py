num = int(input("Enter the Number: "))

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Number of Digit Count:", count)
