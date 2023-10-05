a=[]
for i in range(5):
    n=int(input("enter the number"))
    a.append(n)    
a=list(a) 
for i in range(len(a)-1,-1,-1):
    print(a[i])   