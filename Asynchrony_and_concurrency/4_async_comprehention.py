# Asyncio comprehention allow you to create lists, dictionaries,
# or sets using asyncrounous operations in a concise and readable way


import asyncio


async def my_coroutine(number):
    await asyncio.sleep(1)
    return number**2


async def main():
    numbers = [1, 2, 3, 4, 5]
    print("numbers:", numbers)
    squared_numbers = [await my_coroutine(n) for n in numbers]
    print("squared_numbers:", squared_numbers)


if __name__ == "__main__":
    asyncio.run(main())
