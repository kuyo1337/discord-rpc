import asyncio
import json
import websockets
from config import *
from utils.helpers import start_time


async def build_presence():
    config = NORMAL_CONFIG

    return {
        "op": 3,
        "d": {
            "status": config["Status"],
            "since": 0,
            "activities": [
                {
                    "name": config["Title"],
                    "details": config["Description"],
                    "state": config["SubText"],
                    "type": 3,
                    "timestamps": {
                        "start": int(start_time * 1000)
                    } if config["Timer"] else {}
                }
            ],
            "afk": True
        }
    }


async def connect_discord_gateway():
    ws = await websockets.connect(
        "wss://gateway.discord.gg/?v=9&encoding=json"
    )

    async for message in ws:
        data = json.loads(message)

        if data["op"] == 10:
            await ws.send(json.dumps({
                "op": 2,
                "d": {
                    "token": DISCORD_TOKEN,
                    "properties": {
                        "os": "Windows",
                        "browser": "Discord Client",
                        "device": "PC"
                    }
                }
            }))

            while True:
                presence = await build_presence()
                await ws.send(json.dumps(presence))
                print("presence updated")
                await asyncio.sleep(15) # i remember cheddlatron selfbot doing this so i just add it idk
