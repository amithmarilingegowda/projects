tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()] 

# Method #1:
#    Using function "filter()"
#

# Method #2:
#     Parsing through every element and checking if the element is NULL
#


#Method #1:

new_tuples = []

def func( tuples ):
    length = len(tuples)
    for i in range( 0, length ):
        if( tuples[i] ):
            new_tuples.append( tuples[i] )

    print "Original Tuple:", tuples, "\nNew Tuple:", new_tuples


def filter_func( tuples ):
    print "Original Tuple:", tuples
    tuples = filter( None, tuples )
    print "New Tuple:", tuples

#func(tuples)
filter_func( tuples )
