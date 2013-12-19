'''
	Smallest positive number evenly 
	divisible by all numbers from 1 - 20
'''

def gcd(a , b):
	while (b > 0):
		temp = b;
		b = a % b;
		a = temp;
	return a
def lcm(a,b):
	return a * (b/gcd(a, b))

def lcmset(input):
	result = input[0]
	for i in range(1,len(input)):
			result = lcm(result,input[i])
	return result;

input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print lcmset(input)


