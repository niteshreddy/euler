'''
This is a solution to solve problem 4 of Project Euler.
P4: Find the largest palindrome formed by multiplying two
3 digit numbers. 
'''

'''
This functions determines weather a given number is
palindrome or not. 
'''
def ispalindrome(n):
    temp= n
    rev = int(str(temp)[::-1])
    if n == rev: return True
    return False

'''
    Brute force. 
'''
def detlargestpalin():
    largestpalin = 0
    for i in range(999,1,-1):
        for x in range(999,1,-1):
            num = i * x
            if ispalindrome(num):
                if num > largestpalin:
                    largestpalin = num
    return largestpalin


print detlargestpalin()


