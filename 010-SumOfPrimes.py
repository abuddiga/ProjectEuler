"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


import timeit
import math

NUM = 2000000

def main():
    arr = [0] * NUM
    sum_of_primes = 2
    candidate = 3

    while candidate < NUM:
        if arr[candidate] == 0:
            sum_of_primes += candidate
            i = candidate

            while i < NUM:
                arr[i] = 1
                i += candidate #mark all multiples of candidate

        candidate += 2

    return sum_of_primes


if __name__ == '__main__':
    start = timeit.default_timer()
    ans = main()
    stop = timeit.default_timer()
    print 'Answer: ',ans
    print 'Time taken: %.3f seconds' % float(stop-start)