#smallest odd number
print(min(filter(lambda x: x % 2 == 1, map(int, input().split()))))


#whether given sequence contains 0
print(bool(1 - int(all(map(lambda x: int(x) != 0, open('input.txt').read().split())))))


#product of fifth powers of numbers in sequence
from functools import reduce
print(reduce(lambda x, y: x * y ** 5, [1] + list(map(int, input().split()))))


#bitwise XOR
print(*map(lambda x: x[0] ^ x[1], list(map(list, zip(list(map(int, input().split())), list(map(int, input().split())))))))


#sequence of partial sums
from itertools import accumulate
import operator
print(*accumulate(map(int, input().split()), operator.add))


#factorials of numbers from 0 to n
from functools import reduce
print(' '.join(map(str, [1] + list(map(lambda n: reduce(lambda x, y: x * y, range(1, n)), range(2, int(input()) + 2))))))