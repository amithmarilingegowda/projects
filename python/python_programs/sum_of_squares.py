import sys

n = input("Enter any natural number i.e. anything from 1 to 4294967296\n")
sum = 0

for x in range( 1, n+1 ):
    sum = sum + pow( x, 2 )

print "Sum of square of first %d natural numbers is %d\n" %(n, sum)
