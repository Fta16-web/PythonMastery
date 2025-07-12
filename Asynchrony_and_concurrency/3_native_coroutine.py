# Native coroutine is more efficient than the traditional generator-based coroutine used in earlier version
# Native coroutines use a dedicated await opcode, resulting in better performance and reduced overhead
# The async/await syntax remains the same, but the underlying implementation is more optimized
# introduced in Python3.8
import asyncio


# A native coroutine that simulates an asynchronous task
async def download_file(filename, delay):
    print(f"Starting download: {filename}")
    await asyncio.sleep(delay)  # Simulate I/O-bound operation
    print(f"Finished downloading: {filename}")
    return f"{filename} downloaded"


# Another coroutine that gathers results from multiple tasks
async def main():
    # Create multiple coroutine objects (not yet running)
    task1 = download_file("file1.txt", 2)
    task2 = download_file("file2.txt", 3)
    task3 = download_file("file3.txt", 1)

    # Run all tasks concurrently and wait for all to complete
    results = await asyncio.gather(task1, task2, task3)

    print("\nAll downloads complete:")
    for result in results:
        print(result)


# Run the main coroutine using asyncio's event loop
if __name__ == "__main__":
    asyncio.run(main())
