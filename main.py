import asyncio
from utils.discord_rpc import connect_discord_gateway

async def main():
    print("starting rpc")
    await connect_discord_gateway()

if __name__ == "__main__":
    asyncio.run(main())
