"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


import timeit
import math

NUM = 100

def squareOfSum(n):
    sum_of_n = n * (1 + n) / 2 #sum of first n terms is n * the mean of the sequence: (n + 1)/2
    return sum_of_n ** 2

def sumOfSquares(n):
    s = n * (n + 1) * (2*n + 1) / 6 #sum of squares of first n numbers
    return s

def main():
    # sum_of_squares = sumOfSquares(NUM)
    # square_of_sum = squareOfSum(NUM)
    return squareOfSum(NUM) - sumOfSquares(NUM)


if __name__ == '__main__':
    start = timeit.default_timer()
    ans = main()
    stop = timeit.default_timer()
    print 'Answer: ',ans
    print 'Time taken: %.3f seconds' % float(stop-start)