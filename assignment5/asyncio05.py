from random import random
import asyncio

async def task_rice():
    rice = 1 + random()
    print(f'>order done with rice {rice}')
    await asyncio.sleep(rice)
    return rice

async def task_noodle():
    noodle = 1 + random()
    print(f'>order done with noodle {noodle}')
    await asyncio.sleep(noodle)
    return noodle

async def task_curry():
    curry = 1 + random()
    print(f'>order done with curry {curry}')
    await asyncio.sleep(curry)
    return curry

async def main():
    first_dish = [asyncio.create_task(task_rice(),name="rice"), asyncio.create_task(task_curry(),name="curry"), asyncio.create_task(task_noodle(),name="noodle")]
    done,pending = await asyncio.wait(first_dish,return_when=asyncio.FIRST_COMPLETED)
    print("Done")
    first = done.pop()
    print(f'first menu:{first.get_name()} {first.result()}')

asyncio.run(main())
