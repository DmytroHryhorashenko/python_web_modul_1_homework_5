from aiofile import AIOFile, Writer
from datetime import datetime

async def log_command(command: str):
    async with AIOFile("exchange_log.txt", "a") as afp:
        writer = Writer(afp)
        await writer(f"{datetime.now()} - {command}\n")
        await afp.fsync()