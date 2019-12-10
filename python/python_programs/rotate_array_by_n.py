import sys

array = [1, 60, 7, 20, 15, 50, 40, 3, 30]
n = input("Enter an integer to rotate the array by that number\n")

def rotate_left( n ):
    print "\nRotate Array by %d times to left" %n
    for x in range( n ):
        temp = array[0]
        for y in range( length-1 ):
            array[y] = array[y+1]
        array[length-1] = temp

def rotate_right( n ):
    print "\nRotate Array by %d times to right" %n
    for x in range( n ):
        curr = array[length-1]
        for y in range( length ):
            prev = curr
            curr = array[y]
            array[y] = prev

# Check for Argument
if n > len(array) or n < 0:
    sys.exit("Invalid rotation argument")

# Get Array length
length = len(array)
print "\nArray Length: %d" %length

# Print Original Array
print "\nOriginal Array"
for x in range( 0, length ):
    print array[x],
print ""

# Check if 'n' is greater than half the size of array length.
# If true/so, then instead of rotate right, it would be better
# to do a rotate left. Just an efficient way.
if n > (len(array) / 2):
    print "\nRotate argument %d is greater than half the length of array\n" %n
    n = len(array) - n
    rotate_left( n )
else:
    # Rotate Array right by 'N' times
    rotate_right( n )

# Print Rotated Array
for x in range( 0, length ):
    print array[x],
print ""


print (*array)
