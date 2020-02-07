import asyncio
from time import perf_counter 

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
start = perf_counter() 
asyncio.run(main())
stop = perf_counter() 
print("asyncio time:" + str(stop - start))