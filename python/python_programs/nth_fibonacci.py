import sys


# Fibonacci Series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....


# Get Arguments
nth = int(sys.argv[1])
if( nth < 1 ):
    sys.exit("Invalid nth position\n")
save_nth = nth;
option = input("Select option 1 for recurssive and option 2 for dynamic approach to find fibonacci number\n")
if( option != 1 and option != 2 ):
    sys.exit("Invalid input")


def fibonacci( seed1, seed2, nth ):
    nth = nth - 1
    if( nth == 0 ):
        return seed1
    else:
        return fibonacci( seed2, seed1 + seed2, nth )

prev = 0; #Seed 1
cur  = 1; #Seed 2


if( option == 1 ):
    #print "Nth value (%d) of Fibonacci series is %d" %(save_nth, fibonacci( prev, cur, nth ))
    print "%d" %(fibonacci( prev, cur, nth ))
else:
    for x in range( 1, nth ):
        if( x == nth ):
            exit #Exit on nth
        new = cur + prev
        prev = cur
        cur = new
    
    print prev
    
