import sys

num = input("How many Fibonacci numbers to display\n")

prev = 0; #Seed 1
cur  = 1; #Seed 2

for x in range( 0, num ):
    print prev
    new = cur + prev
    prev = cur
    cur = new

