import asyncio
import websockets


async def main():
    uri = "ws://localhost:8765"

    print("🔌 Connecting...")

    async with websockets.connect(uri) as websocket:
        print("✅ Connected!")

        # первое сообщение от сервера
        welcome = await websocket.recv()
        print(welcome)

        while True:
            msg = input(">>> ")

            await websocket.send(msg)
            response = await websocket.recv()

            print(response)


if __name__ == "__main__":
    asyncio.run(main())