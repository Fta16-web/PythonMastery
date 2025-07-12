import asyncio
from datetime import datetime


def now():
    return datetime.now().strftime("%H:%M:%S")


async def task(name, delay):
    print(f"{now()} - Task {name} started with {delay} seconds delay")
    await asyncio.sleep(delay)
    print(f"{now()} - Task {name} done.")
    return f"Task {name} result"


async def main():
    tasks = [task("A", 3), task("B", 2), task("C", 1)]
    # gather()
    #  “Run all these coroutines at the same time, and wait until all of them are done.”
    #  It schedules the coroutines concurrently (like create_task()) under the hood.
    #  It returns the results in the same order as the coroutines you passed in
    #  — even if they finish out of order.
    # the event loop manages the execution of these coroutine they run concurrently
    # asyncio.gather function is used to await multiple coroutines concurrently
    results = await asyncio.gather(*tasks)
    for result in results:
        print(f"{now()} - {result}")


if __name__ == "__main__":
    asyncio.run(main())
