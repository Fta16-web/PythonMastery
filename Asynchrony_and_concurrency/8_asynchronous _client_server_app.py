# by leveraging asychrounous programming techniques apps can handle multiple connections cocurrenly
#
import asyncio


async def handle_client(reader, writer):
    data = await reader.read(1024)  # Read up to 1024 bytes from the client
    message = data.decode()
    print(f"Received {message} from client")
    response = f"Hello, {message}!"
    writer.write(response.encode())
    await writer.drain()  # Ensure the response is sent
    print("Response sent to client")
    writer.close()  # closes the connection after a single message
    await writer.wait_closed()  # Wait for the connection to close


async def main():
    server = await asyncio.start_server(handle_client, "localhost", 8888)
    print("Server started on localhost:8888")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
# This code creates a simple asynchronous TCP server that listens for incoming connections on localhost:8888
# When a client connects, it reads data from the client, processes it, and sends a response back.
# The server can handle multiple clients concurrently due to the asynchronous nature of the code.
# To test the server, you can use a simple client script or a tool like `telnet` or `nc` (netcat) to connect to the server and send messages.
## Example client code to test the server:
# In a separate terminal, you can run the following client code: nc localhost 8888
