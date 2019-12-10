import sys

array = [60, 20, 50, 40, 30]
largest = 0  # To start with

for x in range( 0, len(array) ):
    if( array[x] > largest ):
        largest = array[x]

print "Largest number of the array is %d\n" %largest
