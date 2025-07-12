# Tasks -> primary building blocks for executing and managing asynchrouns operations operations in AsyncIO
# AsyncIO Task -> a wrapper around a coroutine that allows it to be scheduled and run concurrently with other tasks.
# tasks are created using `asyncio.create_task()` or `loop.create_task()`.
# Tasks are scheduled to run concurrently with other tasks, allowing for efficient use of resources and improved
# Task states: PENDING, RUNNING, CANCELLED, FINISHED -
#  _state attribute of task object provides current state.
# Task methods: cancel(), done(), result(), exception()
import asyncio


async def compute_square(n):
    await asyncio.sleep(1)  # Simulate a delay
    print(f"square of {n}  is {n * n}")
    return n * n


async def main():
    numbers = [1, 2, 3, 4, 5]
    tasks = [asyncio.create_task(compute_square(n)) for n in numbers]
    print("Task states before running:")
    for task in tasks:
        print(task._state)  # Should print 'PENDING'
    squares = await asyncio.gather(*tasks)
    for task in tasks:
        print(task._state)  # Should print 'FINISHED'
    print(f"Squares: {squares}")


if __name__ == "__main__":
    asyncio.run(main())
