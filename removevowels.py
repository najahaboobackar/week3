n = input("Enter your name: ")
n = n.lower()
a = list(n)  # directly converting string to list of characters

i = 0
while i < len(a):    
    if a[i] in ['a', 'e', 'i', 'o', 'u']:
        del(a[i])
    else:
        i += 1

for m in a:
    print(m, end="")
