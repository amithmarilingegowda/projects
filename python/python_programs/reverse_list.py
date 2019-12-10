import sys

# Option #1
# ---------
# Using in-built function "reversed()": This would neither reverse a list in-place(modify the original list),
# nor we create any copy of the list. Instead, we get a reverse iterator which we use to cycle through the list.
#
# Option #2
# ---------
# Using in-build function "reverse()": This would reverse the elements/objects of list in-place but no copy will be
# created.
#
# Option #3
# ---------
# Using Slicing technique
#

# Reversing a list using slicing technique 
def Reverse(list): 
    return list[::-1] 
              
list = [10, 11, 12, 13, 14, 15]

# Original List
print "Original List: ", list

# Reversed List
print "Reversed List: ",
print(Reverse(list))

