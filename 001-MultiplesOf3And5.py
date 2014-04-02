"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""


import timeit

LIMIT = 1000

multiples = []

start = timeit.default_timer()
for x in range(0, LIMIT):
    if x % 3 == 0 or x % 5 == 0:
        multiples.append(x)

ans = sum(multiples)

stop = timeit.default_timer()
print 'Answer: ',ans
print 'Time taken: %.3f seconds' % float(stop-start)