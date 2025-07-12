"""
Mixing Synchronous and Asynchronous Tasks using asyncio

This script demonstrates how to:
1. Use asyncio for concurrent execution of I/O-bound tasks
2. Run blocking (synchronous) code in a thread pool using asyncio's run_in_executor
3. Fetch content from URLs both synchronously (via requests) and asynchronously (via aiohttp)

Useful when:
- You're working with a mix of async and sync libraries (e.g., aiohttp + requests)
- You want to learn how asyncio schedules concurrent tasks
"""

import asyncio
import requests  # Synchronous HTTP library (blocking)
import aiohttp  # Asynchronous HTTP library (non-blocking)
import time


# -------------------------------
# 🛑 Simulate Blocking Operation
# -------------------------------
def blocking_operation():
    """
    Simulates a CPU-bound or blocking I/O operation that should not block the event loop.
    This function will be run in a thread pool using run_in_executor.
    """
    print("[Blocking] Starting blocking operation (3 seconds)...")
    time.sleep(3)
    print("[Blocking] Blocking operation completed.")


# ------------------------------------------
# ✅ Wrap blocking operation in thread pool
# ------------------------------------------
async def run_in_thread_pool():
    """
    Runs a blocking operation in a separate thread to avoid blocking the event loop.
    """
    print("[Async] Offloading blocking operation to thread pool...")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, blocking_operation)
    print("[Async] Thread pool operation completed.")


# -------------------------------------------------
# 🔁 Fetch URL using synchronous requests (blocking)
# -------------------------------------------------
async def fetch_with_requests(url):
    """
    Fetches a URL using synchronous `requests.get()` but runs it in a thread pool.
    """
    print(f"[Requests] Fetching {url}")
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, url)
    print(f"[Requests] Got response from {url}: {response.status_code}")
    return response.text


# ------------------------------------------------
# ⚡ Fetch URL using aiohttp (non-blocking & async)
# ------------------------------------------------
async def fetch_with_aiohttp(url):
    """
    Fetches a URL using aiohttp, which is a fully async HTTP client.
    """
    print(f"[aiohttp] Fetching {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"[aiohttp] Got response from {url}: {response.status}")
            return await response.text()


# -----------------------
# 🚀 Main async function
# -----------------------
async def main():
    # Step 1: Offload a blocking operation to the thread pool
    await run_in_thread_pool()

    # Step 2: Define URLs to fetch
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.github.com",
    ]

    # Step 3: Create asynchronous tasks to fetch content
    # You can switch between fetch_with_aiohttp or fetch_with_requests
    fetch_tasks = [fetch_with_aiohttp(url) for url in urls]

    # Optionally add another blocking operation as a concurrent task
    fetch_tasks.append(run_in_thread_pool())

    # Step 4: Run all tasks concurrently and wait for completion
    results = await asyncio.gather(*fetch_tasks)

    # Step 5: Display content length for fetched pages (excluding blocking task result)
    for i, url in enumerate(urls):
        print(f"[Result] Content length from {url}: {len(results[i])}")


# -----------------------
# 🧵 Run the event loop
# -----------------------
if __name__ == "__main__":
    # asyncio.run: entry point to run async code
    asyncio.run(main())
