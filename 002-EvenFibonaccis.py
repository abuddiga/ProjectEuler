"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""


import timeit

LIMIT = 4e6
evens = []

start = timeit.default_timer()

first = 1
second = 1
term = 0

while True:
    term = first + second
    if term >= LIMIT: break
    if term % 2 == 0:
        evens.append(term)

    tmp = second
    second = term
    first = tmp


ans = sum(evens)

stop = timeit.default_timer()
print 'Answer: ',ans
print 'Time taken: %.3f seconds' % float(stop-start)