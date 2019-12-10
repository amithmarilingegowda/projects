#Python script for calculator

import sys

operation = input("Select calculator operation: \n1. Add\n2. Subtraction\n3. Mutiplication\n4. Division\n")
operation = int(operation)
if( operation < 1 or operation > 4 ):
    sys.exit( "Select any value between 1 & 4\n\n" )

a = int(sys.argv[1])
b = float(sys.argv[2])

def add(a , b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    return (a / b)

print "add = ", add(a, b)
print "sub = ", sub(a, b)
print "mul = ", mul(a, b)
print "div = ", div(a, b)

