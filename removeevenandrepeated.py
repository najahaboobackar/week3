a = []
for _ in range(6):
    num = int(input("Enter the value: "))
    a.append(num)

# Remove duplicates
a = list(set(a))

# Remove even numbers
a = [x for x in a if x % 2 != 0]

for i in a:
    print(i)
      
    