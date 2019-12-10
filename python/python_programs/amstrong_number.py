# Given any number ABCD of order O, if the sum of pow(A,O) + pow(B,O) + pow(C,O) + pow(D,O) is equal to ABCD.
# Then its an Armstrong number.
#
# For Ex:
#         1234 != 1*1*1*1 + 2*2*2*2 + 3*3*3*3 + 4*4*4*4
#         Hence 1234 is not an Amstrong number
#
#         371 == 3*3*3 + 7*7*7 + 1*1*1
#         Hence 371 is an Amstrong number.



import sys

num = int(sys.argv[1])
num_save = num
sum = 0

def get_order_of_num( num ):
    for x in range( 1, num ):
        num = num / 10
        if( num == 0 ):
            return x
    return num

order_of_num = get_order_of_num( num )
print "order_of_num = %d" %order_of_num

for x in range( 0, order_of_num ):
    digit = num % 10
    num = num / 10
    sum += pow( digit, order_of_num )

if( sum == num_save ):
    print "%d is an Amstrong number" %num_save
else:
    print "%d is *NOT* an Amstrong number" %num_save

