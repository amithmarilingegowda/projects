list = [2, 7, 5, 64, 14]

odd = 0
even = 0

for i in range( 0, len(list) ):
    if( list[i] % 2 == 0 ):
        even += 1
    else:
        odd += 1

print "Even_Counter = %d, Odd_Counter = %d" %(even, odd)

