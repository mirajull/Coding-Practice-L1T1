a= float(input())
b= float(input())
c= float(input())
x= float(input())
y= float(input())

k=x**2+y**2+2*a*x+2*b*y+c
if(k==0):
   print('Point P('+str(x)+','+ str(y)+')is on the circle')
elif (k>0):
    print('Point P('+str(x)+','+str(y)+')is outside the circle')
else:
    print('is inside the circle')
