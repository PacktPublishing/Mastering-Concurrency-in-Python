# ch1/example1.py

from math import sqrt
import concurrent.futures
from timeit import default_timer as timer

def is_prime(x):
    if x < 2:
        return False

    if x == 2:
        return x

    if x % 2 == 0:
        return False

    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False

    return x


input = [i for i in range(10 ** 13, 10 ** 13 + 500)]


# sequential
# comment out to only run concurrent
start = timer()
result = []
for i in input:
    if is_prime(i):
        result.append(i)
print('Result 1:', result)
print('Took: %.2f seconds.' % (timer() - start))


# concurrent
# comment out to only run sequential
start = timer()
result = []
with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(is_prime, i) for i in input]

    for i, future in enumerate(concurrent.futures.as_completed(futures)):
        if future.result():
            result.append(future.result())

print('Result 2:', result)
print('Took: %.2f seconds.' % (timer() - start))
