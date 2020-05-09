'''
x= int(input('write down thw year: '))

if (x%400 == 0 ) or (x%4==0 and x%100 != 0 ) :
    print('the year is leapyear')
else :
    print('the year is not leap year' )



# nested if else:

if x% 400==0 :
   print('the year is leap year')
else:
    if (x%4==0 and x%100 !=100 ):
        print('leap year ' )
    else:
        print('not leap year')


# if _ else chain

if x%400 ==0 :
    print('leap year')
elif x%4==0 and x%100 !=0 :
    print('leap year')
else:
    print('not leap year')

              
'''

a=float(input('a=: '))
b=float(input('b=: '))
c=float(input('c=: '))


if( a**2 + b**2 - c >=0) :
    print('the point is :')
    x1 = float(input('x1=: '))
    y1 =float(input('y1=: '))

    if (x1**2 + y1**2 + 2*a*x1 +2*y1*b +c ==0):
     print('the point p(' +  str(x1) +',' + str(y1)+ ') is on the border')
    elif (x1**2 + y1**2 + 2*a*x1 +2*y1*b +c < 0 ):
     print('the point p(' + str(x1)+',' + str(y1) + ') is in the circle')
    else :
     print('the point p(' +str(x1) +',' + str(y1)+ ') is out side the circle')
else :
    print('the circle is unreal')

input()    
    






