import asyncio


async def download_file(file_name):
    print(f"Started downloading {file_name}")
    await asyncio.sleep(2)
    print(f"Finished downloading {file_name}")
    return f"{file_name} downloaded!"


async def main():
    file_lst = ["file1.txt", "file2.txt", "file3.txt"]

    # ✅ Create Task objects from coroutines
    download_tasks = [asyncio.create_task(download_file(f)) for f in file_lst]

    # ✅ Pass Task objects to asyncio.wait()
    completed, pending = await asyncio.wait(
        download_tasks, return_when=asyncio.ALL_COMPLETED
    )

    for task in completed:
        print(task.result())


if __name__ == "__main__":
    asyncio.run(main())
