import sys

def factorial( num ):
    if( num == 1 or num == 0 ):
        return (1);
    return (num * factorial(num - 1))

#Get argument
num = int(sys.argv[1])

method = input("Choose:\n1 for recursive method\n2 for regular method\n")
if( int(method < 1) or int(method) > 2 ):
    sys.exit ("Choose either 1 or 2\n")

if( num < 0 ):
    sys.exit ("\nArgument should be an integer greater than 0\n")

if (int(method) == 1):
    print "Factorial of the number = %d" %(factorial(num))
else:
    if (int(num) == 0):
        print "Factorial of the number = 1"
    else:
        temp = num
        for x in range( 1, num ):
            temp = (temp * x)
        print "Factorial of the number = %d" %(temp)

