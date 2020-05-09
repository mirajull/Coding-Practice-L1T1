x = float(input('Input x value of a Point: '))
y = float(input('Input y value of a Point: '))
a = float(input('Input a value of a Circle: '))
b = float(input('Input b value of a Circle: '))
c = float(input('Input c value of a Circle: '))

r = x**2 + y**2 + 2*x*a+ 2*y*b+c

if r == 0:
    print('Point P ( '+ str(x) +','+ str(y)+') is on the Circle')
elif r >0:
    print('Point P ( '+ str(x)+','+str(y)+') is outside the Circle')
else:
    print('Point P ( '+ str(x) +','+str(y)+') is in the Circle')
