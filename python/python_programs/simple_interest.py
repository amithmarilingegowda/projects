import sys

# Simple Interest Formula
#
# Where
#   P: Principle Amount
#   R: Rate of Interest
#   T: Time In Months
#   S: Simple Interest Amount In Rupees


P = float( sys.argv[1] )
T = float( sys.argv[2] )
R = float( sys.argv[3] )

S = float((P * T * R) / 100)

print "\nPrinciple_Amount = %d\nTime_In_Months = %d\nReturns_In_Percentage = %d\nSimple_Interest_Amount = Rs %f\n" %(P, T, R, S)

