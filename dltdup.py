n = input("enter the value")
result = ""

for char in n:
    if char not in result:
        result += char

print(result)
