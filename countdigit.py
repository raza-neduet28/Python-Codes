num = int(input("Enter a number: "))
count = 0
n = abs(num)
while n > 0:
    count += 1
    n //= 10
if num == 0:
    count = 1

print("Number of digits:", count)
