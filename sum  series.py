x=int(input())
sum=0
max2=0
max3=0
for i in range(x):
    y=int(input())
    sum=sum+y
    max2=max2+y
    if (y<0):
        max3=max(max2-y,max3)
        
        max2=0
if max3==0:
    max3=max2
ans=max(sum,max3)
print(ans)
    
    
        
        
    
    
        
    
    
