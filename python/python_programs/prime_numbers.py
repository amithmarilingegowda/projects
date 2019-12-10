import sys

range_low  = int(sys.argv[1])
range_high = int(sys.argv[2])

def isPrime( num ):
    for x in range( 2, num ):
        if( num % x == 0 ):
            return "FALSE"

for x in range( range_low, range_high + 1):
    if( "FALSE" != isPrime( x )):
        print x

