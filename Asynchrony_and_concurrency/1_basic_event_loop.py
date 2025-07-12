# imports Python’s built-in asynchronous I/O library

import asyncio
from datetime import datetime


# asynchronous function defines asynchronous coroutine
# can be  paused and resumed using await.
# delay -> number inseconds This pauses this coroutine for delay seconds without blocking other tasks (if there were any).
# what -> message to print
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(f"delay:{delay} second(s) ,", what)


def now():
    return datetime.now().strftime("%H:%M:%S")


# Runs the main() coroutine
async def main():
    # sequental
    start_time = asyncio.get_running_loop().time()
    print("Started at:", start_time, now())
    await say_after(1, "Hello AsyncIO")
    await say_after(2, "AsyncIO is powerful")
    end_time = asyncio.get_running_loop().time()
    print("Finished at:", end_time, now())
    print(f"sequential time elapsed: {end_time - start_time}")

    print("#" * 10)
    # run coroutine in parallel
    start_time = asyncio.get_running_loop().time()
    task1 = asyncio.create_task(say_after(1, "Hello AsyncIO"))
    task2 = asyncio.create_task(say_after(2, "AsyncIO is powerful"))
    await task1
    await task2
    end_time = asyncio.get_running_loop().time()
    print(f"Parallel time elapsed: {end_time - start_time}")


# Runs the main() coroutine
if __name__ == "__main__":
    asyncio.run(main())
