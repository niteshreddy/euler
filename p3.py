'''
    Find the largest prime factor of a given number. 
    Problem 3 of Project euler
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


def return_largest_prime(n):
    i = 2
    print n**0.5
    while i <= n:
        print i
        if n%i == 0:
            if (isprime(i)): 
                largest = i
        i = i + 1
    return largest

n = input()
print return_largest_prime(n)

