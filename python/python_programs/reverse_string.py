#string = "malayalam"
#string = "amith"
#string = "amitha"
#string = "am"
string = "pullup"

def isPalindrome( string ):
    half_length = len(string) / 2
    for i in range( 0, half_length ):
        if( string[i] != string[len(string) - 1 - i] ):
            return "FALSE"
    return "TRUE"

if( isPalindrome(string) == "TRUE" ):
    print "String is a palindrome"
else:
    print "String is *NOT* a palindrome"

