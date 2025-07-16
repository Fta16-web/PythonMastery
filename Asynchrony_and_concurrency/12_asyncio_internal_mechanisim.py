import asyncio
import time
import heapq


class SimpleTaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, coro, delay):
        exec_time = time.time() + delay
        heapq.heappush(self.tasks, (exec_time, coro))

    async def run(self):
        while self.tasks:
            exec_time, coro = heapq.heappop(self.tasks)
            now = time.time()
            if exec_time > now:
                await asyncio.sleep(exec_time - now)
            try:
                print(f"Running task: {coro.__name__} at {time.time()}")
                await coro()
            except Exception as e:
                print(f"Error in task {coro.__name__}: {e}")


async def example_task():
    print(f"Task completed at {time.time()}")


async def main():
    scheduler = SimpleTaskScheduler()
    scheduler.add_task(example_task, 3)
    scheduler.add_task(example_task, 1)
    await scheduler.run()


if __name__ == "__main__":
    asyncio.run(main())
