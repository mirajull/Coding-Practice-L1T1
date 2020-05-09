import sys # header file 'sys'

x = input('Input a Integer value: ')
x = int(x) # x = int(input('Input a Integer value: '))

if x> 100 or x < 0:
    print('Invalid Input')
    sys.exit(0) #exit is a butit-in function resides in 'sys' header

if (x >= 80):
    print('You got A+')
elif (x >= 75):
    print('You got A')
elif (x>=70):
    print('You got A-')
elif (x>=65):
    print("You got B+")
elif (x>=60):
    print('You got B')
elif (x>=55):
    print('You got B-')
elif (x>=50):
    print('You got C+')
elif (x >= 45):
    print('You got C')
elif (x>=40):
    print('You got D')
else:
    print('You got F')
    
print('Program terminating...')
