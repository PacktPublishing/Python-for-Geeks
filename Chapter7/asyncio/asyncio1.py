#asyncio1.py to build a basic coroutine
import asyncio
import time


async def say(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

print("Started at ", time.strftime("%X"))
asyncio.run(say(1,"Good"))
asyncio.run(say(2, "Morning"))
print("Stopped at ", time.strftime("%X"))
