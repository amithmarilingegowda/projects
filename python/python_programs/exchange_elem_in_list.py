# Python "lists" can hold completely heterogeneous, arbitrary data, and they can be
# appended to very efficiently, in amortized constant time. If you need to shrink and grow your list time-efficiently and
# without hassle, they are the way to go. But they use a lot more space than C arrays.

# Python "array" on the other hand, is just a thin wrapper on C arrays. It can hold only homogeneous data,
# all of the same type, and so it uses only sizeof(one object) * length bytes of memory.

# Another difference between a list and an array is the functions that you can perform to them.

# LIST VERSUS ARRAY:
#
# list
#   -> flexible
#   -> can be heterogeneous
# 
# array
#   -> homogeneous
#   -> compact (in size)
#   -> efficient (functionality and speed)

list = [10, 2, 3, 43, 17, 19, 324, 54, 1]

#def swap_first_n_last( list ):
#    list[0], list[-1] = list[-1], list[0]
#    return list

#def swap_first_n_last( list ):
#    list[0], list[len(list)-1] = list[len(list)-1], list[0]
#    return list

def swap_first_n_last( list ):
    temp = list[0]
    list[0] = list[len(list)-1]
    list[len(list)-1] = temp
    return list

# Print Original Array
print "Original Array"
print( list )

print "Modified Array"
print( swap_first_n_last(list) )

