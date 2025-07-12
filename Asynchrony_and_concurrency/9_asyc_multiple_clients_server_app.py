import asyncio
# import ssl  # ssl library for secure communication. SSL context with certificate and key files.

##ssl_context.load_cert_chain(certfile="server.crt", keyfile="server.key")
# This code sets up an SSL context for secure communication.
# It loads a certificate and key file for the server to use.
# Make sure to replace "server.crt" and "server
clients = []


async def handle_client(reader, writer):
    clients.append(writer)
    try:
        while True:
            data = await reader.read(1024)  # Read up to 1024 bytes from the client
            if not data:
                break  # Exit loop if no data is received (client disconnected)
            message = data.decode()
            print(f"Received {message} from client")
            if message.strip().lower() == "exit":
                print("Client requested to exit")
                break
            response = f"Hello, {message}!"
            for client in clients:
                client.write(response.encode())
                await client.drain()  # Ensure the response is sent
            print("Response sent to all clients")
    finally:
        clients.remove(writer)  # Remove the client from the list when done
        writer.close()  # Close the connection
        await writer.wait_closed()  # Wait for the connection to close


async def main():
    server = await asyncio.start_server(
        handle_client,
        "localhost",
        8888,  # ssl=ssl_context  # Uncomment this line to enable SSL
    )  # Start the server on localhost:8888 with SSL
    print("Server started on localhost:8888")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
# This code creates a simple asynchronous TCP server that listens for incoming connections on localhost:8888
# When a client connects, it reads data from the client, processes it, and sends a response back.
# The server can handle multiple clients concurrently due to the asynchronous nature of the code.
# To test the server, you can use a simple client script or a tool like `telnet` or `nc` (netcat) to connect to the server and send messages.
# Example client code to test the server:
# In a separate terminals
