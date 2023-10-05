a = []
for i in range(8):
    n = int(input("enter the values"))
    a.append(n)
a.sort()

differences = []

for i in range(3):  # Adjusted range to avoid out-of-bounds errors
    min2 = a[i] - a[4+i]
    min1 = a[1+i] - a[5+i]
    b = min(min2, min1)
    differences.append(b)

print(min(differences))
