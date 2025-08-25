pre = 1
next = 1
a = int(input("Enter no of terms: "))
print(pre)
print(next)
for i in range(2, a):
    new = pre + next
    print(new)
    pre = next
    next = new
print("\nApproximate Golden Ratio:", next / pre)
