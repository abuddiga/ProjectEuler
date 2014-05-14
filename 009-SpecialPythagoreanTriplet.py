"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""


import timeit
import math

N = 1000

def main():
    a = 0

    for b in range(N/2): #b can be at maximum 499 to satisfy conditions (a=0, c=501 or a=1, c= 500)
        while a < b:
            if a + b + math.sqrt(a**2 + b**2) == N:
                return a*b*math.sqrt(a**2 + b**2)
            a += 1
        a = 0
    

if __name__ == '__main__':
    start = timeit.default_timer()
    ans = main()
    stop = timeit.default_timer()
    print 'Answer: ',ans
    print 'Time taken: %.3f seconds' % float(stop-start)