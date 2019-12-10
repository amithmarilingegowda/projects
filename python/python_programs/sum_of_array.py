import sys

# Python inbuilt function sum(array) can also be directly used to find the sum of array.

array = [10, 20, 30, 40, 50]
sum = 0

for x in range( 0, len(array) ):
    sum += array[x]

print "Sum of array is %d\n" %sum
