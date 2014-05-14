

import timeit
import math

list_one = [1, 5, 13, 14, 16, 21]
list_two = [2, 5, 8, 12, 17, 25, 29, 34]

def main():
    new = []
    if len(list_one) < len(list_two):
		short, longer = list_one, list_two
    else:
		short, longer = list_two, list_one

    idx, idx_2 = 0, 0

    while idx < len(short):
        if short[idx] < longer[idx_2]:
            new.append(short[idx])
            idx += 1
        else:
            new.append(longer[idx_2])
            idx_2 += 1

    new.extend(longer[len(short):])

    return new

    

if __name__ == '__main__':
    start = timeit.default_timer()
    ans = main()
    stop = timeit.default_timer()
    print 'Answer: ',ans
    print 'Time taken: %.3f seconds' % float(stop-start)