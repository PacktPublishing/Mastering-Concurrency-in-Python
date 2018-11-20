import asyncio
import time
from datetime import datetime

async def custom_factorial(name, n):
    f = 1

    for i in range(2, n + 1):
        print(f'Task {name}: Compute factorial({i}).')
        await asyncio.sleep(1)
        f *= i

    print(f'Task {name}: factorial({n}) is {f}.')

async def main():
    tasks = [custom_factorial('A', 3), custom_factorial('B', 4)]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print(f'Total time: {end - start : .4f}.')
