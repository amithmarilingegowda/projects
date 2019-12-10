import sys

#Compound Interest = P * ((1 + R/100) ^ T)
#
#Where
#  P: Principle Amount
#  R: Rate of Interest
#  T: Time In Months
#  C: Compounded Amount In Rupees

P = float(sys.argv[1])
T = float(sys.argv[2])
R = float(sys.argv[3])

C = P * (pow( (1 + R / 100), T ))

print "\nPrinciple_Amount = %d\nTime_In_Months = %d\nReturns_In_Percentage = %d\nCompounded_Amount = Rs %f\n" %(P, T, R, C)

