y = int(input())

'''
# if -else
if y % 400 ==0 or (y %4==0 and y %100 != 0):
    print('Leap Year')
else:
    print('Not Leap Year')


# Nested if-else

if y % 400 ==0:
    print('Leap Year')
else:
    if (y %4==0 and y %100 != 0):
        print('Leap Year')
    else:
        print('Not Leap Year')
'''

# if-else chain
if y % 400 ==0:
    print('Leap Year')
elif y %4==0 and y %100 != 0:
    print('Leap Year')
else:
    print('Not Leap Year')
