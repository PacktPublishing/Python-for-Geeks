#asyncio_casestudy.py
import asyncio
import time

import aiofiles, aiohttp
from getfilelistpy import getfilelist

TASK_POOL_SIZE = 10

#update the resource object as per your API key and the gdriver folder id
resource = {
    "api_key": "AIzaSyDYKmm85keqnk41DpYa2bxddKrGns4z0",
    "id": "0B8TxHW2Ci6dbckVweTRlV3RUU",
    "fields": "files(name,id,webContentLink)",
}

async def mydownloader(name, queue):
    while True:
        # Get the file id and name from the queue
        item = await queue.get()
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                async with session.get(item['webContentLink']) as resp:
                    if resp.status == 200:
                        f = await aiofiles.open('./files/{}'.format(
                            item['name']), mode='wb')
                        await f.write(await resp.read())
                        await f.close()
        finally:
            print(f"{name}: Download completed for ",item['name'])
            queue.task_done()

def get_files(resource):
    res = getfilelist.GetFileList(resource)
    files_list = res['fileList'][0]
    return files_list

async def main ():
    files = get_files(resource)
    #add files info into the queue
    myqueue = asyncio.Queue()
    for item in files['files']:
        myqueue.put_nowait(item)

    tasks = []
    for id in range(TASK_POOL_SIZE):
        task = asyncio.create_task(
            mydownloader(f'Task-{id+1}', myqueue))
        tasks.append(task)

    start_time = time.monotonic()
    await myqueue.join()
    total_exec_time = time.monotonic() - start_time

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)

    print(f'Time taken to download: {total_exec_time:.2f} seconds')

asyncio.run(main())
