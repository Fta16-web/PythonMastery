# asyncIO supports asynchronous programming in Python, allowing for concurrent execution of code.
# through the use of coroutines, which are special functions that can pause and resume their execution.
# popular asynchronous libraries include asyncio, aiohttp, and aiomysql.
# AsyncPG -> for PostgreSQL, Motor -> for MongoDB, and aioredis -> for Redis,
# Aio_pika -> for RabbitMQ, and aiokafka -> for Kafka ,...
# db.execute methods are used to execute SQL queries or commands asynchronously.
# db.commit() is used to commit the transaction, ensuring that all changes made during the transaction are saved to the database.
#
import asyncio
import aiosqlite


async def create_table(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        await db.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, message TEXT)"
        )
        await db.commit()
        print(f"Table {table_name}created or already exists.")


async def insert_data(db_name, table_name, message):
    async with aiosqlite.connect(db_name) as db:
        await db.execute(f"INSERT INTO {table_name} (message) VALUES (?)", (message,))
        await db.commit()
        print(f"Inserted message: {message} into table {table_name}.")


async def fetch_data(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute(f"SELECT * FROM {table_name}") as cursor:
            rows = await cursor.fetchall()
            print(f"Fetched data from table {table_name}:")
            for greeting in rows:
                print(f"Greeting ID: {greeting[0]}, Message: {greeting[1]}")


async def main():
    db_name = "example.db"
    table_name = "messages"

    await create_table(db_name, table_name)
    await insert_data(db_name, table_name, "Hello, World!")
    await insert_data(db_name, table_name, "AsyncIO is great!")
    await fetch_data(db_name, table_name)


if __name__ == "__main__":
    asyncio.run(main())
# This code demonstrates how to perform asynchronous database operations using aiosqlite.
# It creates a table, inserts data into it, and fetches the data asynchronously.
# aiosqlite is an asynchronous library for SQLite that allows you to perform database operations without blocking the event loop.
# This is useful for applications that require high concurrency and responsiveness, such as web applications or real-time systems.
# The code uses async/await syntax to define asynchronous functions and manage the event loop.
# The create_table function creates a table if it doesn't exist, insert_data inserts messages into the table,
# and fetch_data retrieves all rows from the table. The main function orchestrates these operations.
# The database operations are performed within an async context manager to ensure proper resource management.
# The aiosqlite library is built on top of SQLite, providing an easy-to-use interface for asynchronous database operations.
# It allows you to perform CRUD (Create, Read, Update, Delete) operations on SQLite databases without blocking the event loop.
# This is particularly useful in applications that require high concurrency, such as web servers or real-time applications.
# The code demonstrates how to create a table, insert data into it, and fetch data asynchronously using aiosqlite.
## To run this code, you need to have the aiosqlite library installed in venv. You can install it using pip:
# pip install aiosqlite
# Make sure to have SQLite installed on your system as well, as aiosqlite is built on top of it.
# You can then run the script, and it will create a database file named "example.db" in the current directory.
# The script will create a table named "messages", insert two messages into it, and then fetch and print the data from the table.
## This code is a simple demonstration of how to use aiosqlite for asynchronous database operations in Python.
# It can be extended to include more complex operations, such as updating or deleting records,
# handling transactions, or integrating with web frameworks like FastAPI or Flask for building web applications.
