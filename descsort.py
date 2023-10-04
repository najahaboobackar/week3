n=int(input("enter the value"))
a=[]
for i in range(n):
    num=int(input("enter the numbers"))
    a.append(num)
k=0

for i in range(0,len(a)-1,1):
    for j in range(0,len(a)-1-i,1):
        if a[j]<a[j+1]:
            temp =a[j]
            a[j]=a[j+1]
            a[j+1]=temp  
for s in a:
    print(s)                      