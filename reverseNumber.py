num = int(input("Enter the Number : "))

rev = 0

while num > 0:
  digit = num % 10 #Get Latest Number
  rev = rev * 10 + digit
  num //= 10 # remove last digit

print("Reverse number = ", rev)
