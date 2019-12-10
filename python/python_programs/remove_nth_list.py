import sys

list = [ "Hello", "1", "My Name is Anthony", "1", "Gonzales", "1", "Tumbad", "10", "1" ]

def search_n_modify_list( nth_occurence ):
    for i in range( 0, len(list) - 1 ):
        if( list[i] == keyword ):
            nth_occurence = nth_occurence - 1
            if( 0 == nth_occurence ):
                del( list[i] ) # Delete the 'Nth' item from the list
                return "TRUE"
    return

keyword = raw_input("Enter keyword to search\n")
nth_occurence = int(raw_input("Enter Nth occurrence\n"))

print "Original List: ",
print list

if( search_n_modify_list( nth_occurence ) == "TRUE" ):
    print "Found Nth keyword in the list"
else:
    print "Nth Keyword NOT found in the list"

# Print list contents
# Print modified list contents
print "Modified List: ",
print list
