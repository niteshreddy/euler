'''
	Sum of all primes below 2 million.
'''



'''
    Function that determins if a given number is prime or not.
'''
def isprime(n):

    n = abs(int(n));
    if n < 2: return False
    if n == 2: return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


'''
Brute Force

Now, find solutions which are better than this.
'''
def return_sum_primes():
	sum = 0
	for i in range(1,2000001):
		print i
		if(isprime(i)):
			sum = sum + i;
	return sum

print return_sum_primes();