#!/bin/python3

import os

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def get_primes(q):
    primes = []
    cur = 2
    while q > len(primes):
        while not all(cur % prime for prime in primes):
            cur += 1
        primes.append(cur)
        cur += 1
    return primes


def waiter(arr, q):
    nxt, answers = arr[:], []
    for prime in get_primes(q):
        temp, curr = [], []
        for num in reversed(nxt):
            if num % prime:
                temp.append(num)
            else:
                curr.append(num)
        answers += reversed(curr)
        nxt = temp
    answers += reversed(temp)
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    number = list(map(int, input().rstrip().split()))
    result = waiter(number, q)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
