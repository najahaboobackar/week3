a=[]
for i in range(4):
    n= int(input("enter the values"))
    a.append(n)
a=list(a)    
maxSub=a[0]
currSum=0  
for i in range(0,3):
    if currSum <0:
        currSum=0
    currSum=currSum+a[i] 
    maxSub=max(maxSub,currSum) 
    
print(maxSub)        