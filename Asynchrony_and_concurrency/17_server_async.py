# =====================================================
# Asynchronous Chat Server using asyncio in Python
# =====================================================
# This server allows multiple clients to connect and exchange messages.
# Messages received from one client are broadcasted to all other connected clients.
# -----------------------------------------------------

import asyncio


class ChatServer:
    """
    Asynchronous chat server that handles multiple clients concurrently.
    It receives messages from one client and broadcasts them to all other connected clients.
    """

    def __init__(self):
        # List to keep track of all connected client writers (used for broadcasting)
        self.clients = []

    async def handle_client(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ):
        """
        Coroutine that handles communication with a single client.

        Parameters:
        - reader: StreamReader object to receive data from the client.
        - writer: StreamWriter object to send data to the client.
        """
        # Add the new client writer to the list of clients
        self.clients.append(writer)
        addr = writer.get_extra_info("peername")
        print(f"Client connected: {addr}")

        try:
            while True:
                # Wait for incoming data from the client
                data = await reader.read(100)

                if not data:
                    # No data means client disconnected
                    print(f"Client {addr} disconnected")
                    break

                # Decode and display the message
                message = data.decode().strip()
                print(f"Received from {addr}: {message}")

                # Broadcast the message to all other clients
                for client in self.clients:
                    if client != writer:
                        client.write(data)
                        await client.drain()  # Ensure message is sent

        except asyncio.CancelledError:
            # Handle cancellation (e.g., server shutdown)
            print(f"Connection to {addr} was cancelled.")

        except Exception as e:
            print(f"Error with client {addr}: {e}")

        finally:
            # Remove client and clean up the connection
            if writer in self.clients:
                self.clients.remove(writer)
            writer.close()
            await writer.wait_closed()
            print(f"Cleaned up client {addr}.")

    async def start_server(self, host: str, port: int):
        """
        Starts the asynchronous TCP server.

        Parameters:
        - host: Hostname or IP address to bind the server (e.g., "localhost").
        - port: Port number to listen on (e.g., 8888).
        """
        # Create the server and bind to host/port
        server = await asyncio.start_server(self.handle_client, host, port)
        addr = server.sockets[0].getsockname()
        print(f"Server started and listening on {addr}")

        # Keep the server running
        async with server:
            await server.serve_forever()


# ----------------------------------------------------
# Entry point: Run this script to start the chat server
# ----------------------------------------------------
if __name__ == "__main__":
    try:
        # Create a server instance
        server = ChatServer()

        # Run the server on localhost:8888
        asyncio.run(server.start_server("localhost", 8888))

    except KeyboardInterrupt:
        print("\nServer stopped manually.")
