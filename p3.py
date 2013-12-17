'''
    Find the largest prime factor of a given number. 
    Problem 3 of Project euler
'''

    


'''
    Function that determins if a given number is prime or not.
'''
def isprime(n):
    if n == 1: return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def return_largest_prime(n):
    i = 2
    while i < int(n**0.5)+1:
        if n%i == 0:
            if (isprime(i)): 
                largest = i
        i = i + 1
    return largest

n = input()
print return_largest_prime(n)

