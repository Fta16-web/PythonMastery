import asyncio
import time
import logging

# Configure logging format and level
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def simulate_io_task(name, duration):
    """
    Simulate an I/O-bound task that takes a certain duration to complete.

    Args:
        name (str): Name of the task.
        duration (int): Duration in seconds for which the task runs.

    Returns:
        int: The duration the task took to complete.
    """
    logging.info(f"{name} started, will run for {duration} seconds.")
    await asyncio.sleep(duration)
    logging.info(f"{name} completed after {duration} seconds.")
    return duration  # <-- fix: return duration


async def main():
    """
    Main function to run the asyncio event loop and execute tasks concurrently.
    """
    tasks = [
        simulate_io_task("Task 1", 2),
        simulate_io_task("Task 2", 3),
        simulate_io_task("Task 3", 1),
    ]

    start_time = time.perf_counter()
    durations = await asyncio.gather(*tasks)  # Now returns actual durations
    end_time = time.perf_counter()

    total_elapsed = end_time - start_time
    max_duration = max(durations)
    total_sleep = sum(durations)

    logging.info("All tasks completed.")
    logging.info(f"Maximum task duration: {max_duration} seconds")
    logging.info(f"Total elapsed wall time: {total_elapsed:.2f} seconds")
    logging.info(f"Sum of sleep durations (sequential): {total_sleep} seconds")


if __name__ == "__main__":
    asyncio.run(main())
    logging.info("Event loop has been closed.")
