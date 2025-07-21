# ===============================================
# Asynchronous Chat Client using asyncio in Python
# ===============================================

# This script connects to a chat server asynchronously using asyncio.
# It allows a user to send messages to a server and receive responses.
# The server should be running separately and listening on the same host and port.

import asyncio


async def chat_client(name: str, host: str, port: int):
    """
    Asynchronous chat client that connects to a server and sends/receives messages.

    Parameters:
    - name (str): User's name to identify messages.
    - host (str): Server hostname or IP address (e.g., "localhost").
    - port (int): Server port number (e.g., 8888).
    """
    try:
        # Establish connection to the server
        reader, writer = await asyncio.open_connection(host, port)
        print(
            f"{name} connected to the server at {host}:{port}\nType 'exit' to leave the chat.\n"
        )

        while True:
            # Get message input from user
            message = input(f"{name}: ")

            # Exit the loop and disconnect if user types 'exit'
            if message.strip().lower() == "exit":
                print(f"{name} is disconnecting...")
                break
            message = f"{name}: {message}"
            # Send the message to the server
            writer.write(message.encode())
            await writer.drain()  # Ensure the data is sent

            # Wait for the response from the server (max 100 bytes)
            data = await reader.read(100)
            if data:
                print(f"Received: {data.decode()}\n")
            else:
                # If server closes the connection
                print("Server closed the connection.")
                break

    except ConnectionRefusedError:
        print("Failed to connect to the server. Make sure the server is running.")

    except asyncio.CancelledError:
        # Graceful handling of task cancellation
        print(f"{name} connection was cancelled.")

    except Exception as e:
        # Handle unexpected exceptions gracefully
        print(f"An unexpected error occurred: {e}")

    finally:
        # Ensure the writer is closed properly
        try:
            writer.close()
            await writer.wait_closed()
            print(f"{name} disconnected.")
        except Exception:
            pass  # Ignore any exceptions during close if not connected


async def main():
    """
    Entry point of the client application.
    Collects user input for configuration and starts the chat client.
    """
    # Configuration for connection
    host = "localhost"  # Change this if connecting to a remote server
    port = 8888  # The port must match the server's listening port

    # Get the user's name
    name = input("Enter your name: ").strip()

    # Start the chat client
    await chat_client(name, host, port)


# -----------------------------------------------
# Start the asyncio event loop to run the client
# -----------------------------------------------
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nChat client closed by user.")
