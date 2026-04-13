import asyncio
import websockets


async def main():
    uri = "ws://localhost:8765"
    print(f"Подключаемся к {uri}...")

    async with websockets.connect(uri) as websocket:
        print("✅ Подключено! Пиши команды (например: exchange 2 USD EUR)")

        while True:
            command = input(">>> ")

            if command.lower() in ["exit", "quit"]:
                print("Выход...")
                break

            await websocket.send(command)
            response = await websocket.recv()
            print(response)


if __name__ == "__main__":
    asyncio.run(main())