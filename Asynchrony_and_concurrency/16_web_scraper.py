# First, install aiohttp if you haven't already:
# pip install aiohttp

import asyncio  # Core Python module for asynchronous programming
import aiohttp  # Third-party library for asynchronous HTTP client functionality


async def fetch_page(session, url):
    """
    Asynchronously fetch a single web page using an aiohttp session.

    Args:
        session (aiohttp.ClientSession): An active aiohttp session.
        url (str): The URL of the page to fetch.

    Returns:
        str: The content of the fetched page as text.
    """
    # Use an asynchronous context manager to send a GET request
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

        # Raise an exception if the response status is not 200 OK
        if response.status != 200:
            raise Exception(f"Failed to fetch {url}: {response.status}")

        # Return the full text content of the response
        return await response.text()


async def main():
    """
    Main coroutine that runs the web scraping logic.
    It sets up the session and schedules all fetch tasks concurrently.
    """
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        # "https://httpbin.org/status/404",  # Uncomment this line to test error handling
    ]

    # Use aiohttp.ClientSession for managing connection pooling efficiently
    async with aiohttp.ClientSession() as session:
        # Create a list of coroutine tasks for all URLs
        tasks = [fetch_page(session, url) for url in urls]

        try:
            # Run all tasks concurrently and wait for their completion
            results = await asyncio.gather(*tasks)

            # Process and display each result
            for result in results:
                print(f"Page content length: {len(result)}")
                print(f"Page content: {result}")

        except Exception as e:
            # Catch and display any error that occurs during the fetch
            print(f"An error occurred: {e}")


# Run the async event loop if this script is the main module
if __name__ == "__main__":
    # Start the event loop and run the main coroutine
    asyncio.run(main())

    print("Web scraping completed.")

    # Summary:
    # - This script uses asyncio + aiohttp for asynchronous web scraping.
    # - It fetches pages concurrently and prints content or errors.
    # - aiohttp.ClientSession is used to efficiently manage connections.
    # - asyncio.gather runs all fetches in parallel and returns their results.
