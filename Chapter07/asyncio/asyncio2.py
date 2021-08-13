#asyncio2.py to build and run coroutines in parallel
import asyncio
import time

async def say(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main ():
    task1 = asyncio.create_task( say(1, 'Good'))
    task2 = asyncio.create_task( say(1, 'Morning'))
    print("Started at ", time.strftime("%X"))
    await task1
    await task2
    print("Stopped at ", time.strftime("%X"))

asyncio.run(main())