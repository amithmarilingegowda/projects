n = int(input("Enter number of elements intended in the array: \n"))

print("Enter elements one by one")
array = []
for i in range( 0, n ):
    array.append( int(input()) )

#print("Enter all the elements in a line separated by space")
#array = map(int,raw_input().split(' '))


print "Array contents: "
print (array)

ascending = 0
descending = 0

for i in range( 0, len(array) - 1 ):
    if( array[i] > array [i+1] ):
        descending += 1
    else:
        ascending += 1

if( ascending and descending ):
    print "Array is NOT monotonous\n"
else:
    print "Array is monotonous\n"

