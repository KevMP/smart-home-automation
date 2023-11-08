import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")
        # Here you would handle the message and potentially
        # communicate with your AI agent to process it.
        await websocket.send("Message received")

start_server = websockets.serve(handler, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
