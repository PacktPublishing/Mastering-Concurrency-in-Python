# ch10/example2.py

import asyncio
import time

async def count_down(name, delay):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        await asyncio.sleep(delay)

        duration = time.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -= 1

async def main():

    await asyncio.gather(*[
        count_down('A', 1),
        count_down('B', 0.8),
        count_down('C', 0.5)
    ])

start = time.perf_counter()
asyncio.run(main())

print('-' * 40)
print('Done.')
