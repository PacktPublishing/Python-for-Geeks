#asyncio3.py to distribute work via queue
import asyncio
import random
import time

async def executer(name, queue):
    while True:
        exec_time = await queue.get()
        await asyncio.sleep(exec_time)
        queue.task_done()
        print(f'{name} has taken  {exec_time:.2f} seconds')

async def main ():

    myqueue = asyncio.Queue()
    calc_exuection_time = 0
    for _ in range(10):
        sleep_for = random.uniform(0.4, 0.8)
        calc_exuection_time += sleep_for
        myqueue.put_nowait(sleep_for)

    tasks = []
    for id in range(3):
        task = asyncio.create_task(executer(f'Task-{id+1}', myqueue))
        tasks.append(task)

    start_time = time.monotonic()
    await myqueue.join()
    total_exec_time = time.monotonic() - start_time

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)

    print(f"Calculated execution time {calc_exuection_time:0.2f}")
    print(f"Actual execution time {total_exec_time:0.2f}")

asyncio.run(main())