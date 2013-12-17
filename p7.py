'''
    Given n, determine the nth prime number. 
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

'''
    Determines the nth prime number. 
'''
def primenumber(n):
    cnt = 0
    num = 1
    while (True):
        if isprime(num):
            cnt = cnt + 1
        if cnt == n:
            return num
        num = num + 1


n = input()
print primenumber(n)

        
