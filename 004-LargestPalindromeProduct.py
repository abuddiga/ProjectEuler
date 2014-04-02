"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


import timeit
import math

digits = 3
lower = 10 ** (digits - 1)
upper = 10 ** digits

def isPalindrome(num):
    return str(num) == str(num)[::-1]


def main():
    lpp = 0
    x = upper
    while x >= lower:
        y = upper
        while y >= x:
            if (x * y) < lpp:
                break
            if isPalindrome(x * y):
                lpp = x * y

            y -= 1
        x -= 1
    return lpp

    

if __name__ == '__main__':
    start = timeit.default_timer()
    ans = main()
    stop = timeit.default_timer()
    print 'Answer: ',ans
    print 'Time taken: %.3f seconds' % float(stop-start)