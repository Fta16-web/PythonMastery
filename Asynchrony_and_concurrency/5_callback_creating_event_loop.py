# use asyncio.new_eventloop to create a new eventloop
# run_until-complete method is used to run the coroutine until it is finished
# it is important to properly close the event loop after running the coroutine to clean up resources
# in some cases you want to run an asynchrounes operation and recieve result in a callback functions
# The asyncio.ensure_future function schedules the coroutine for execution and returns a future object
# The add_done_callback method on future object allows you to register a callback function to be called when the coroutine completes
#
#
import asyncio


# Callback function that will be called once the coroutine is complete
def callback(future):
    print(f"Callback received result: {future.result()}")


# An asynchronous coroutine that simulates a delay and returns a value
async def my_coroutine():
    await asyncio.sleep(1)
    return 42


if __name__ == "__main__":
    # Step 1: Create a new event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)  # Optional but good practice

    try:
        # Step 2: Create coroutine and schedule it as a future
        coroutine = my_coroutine()
        future = asyncio.ensure_future(coroutine)

        # Step 3: Add callback to be executed when coroutine is done
        future.add_done_callback(callback)

        # Step 4: Run event loop until the coroutine is complete
        loop.run_until_complete(future)

    finally:
        # Step 5: Close the loop to clean up resources
        loop.close()
