
squares_sum = 0
sumsquare = 0

for x in range(1,101):
    squares_sum = squares_sum + x * x
   # print x * x
    sumsquare = sumsquare + x

sumsquare = sumsquare**2;


#print squares_sum
#print sumsquare

print abs(sumsquare-squares_sum)
