x=int(input())
sum=0
for i in range(1,x+1):
    #import math
    
#    sum=sum+i*((i+1)**2)
#print(sum)
    #sum=sum+i*(math.factorial(i))
#print(sum)
#    y=(3*i+1)/((i+1)*(i+2)*(i+3))
 ##   sum=sum+y
#print(sum)
    p=0
    for j in range (i):
        p=2*j+p
    sum=sum+p
print(sum)

