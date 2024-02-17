from fastapi import FastAPI, HTTPException
from hypercorn.config import Config
from hypercorn.asyncio import serve
import asyncio
from pydantic import BaseModel
from typing import Tuple
from sniffer_parser import AlbionPacketSniffer


class Player(BaseModel):
    position: Tuple[float, float]


app = FastAPI()
sniffer = AlbionPacketSniffer()
sniffer.start()


@app.get("/master/position", response_model=Player, summary="Gets the current master player position.")
async def get_position():
    pos = sniffer.player.pos

    if pos is None:
        raise HTTPException(status_code=404, detail="Player have not moved yet.")
    return Player(position=pos)

if __name__ == "__main__":
    config = Config()
    config.bind = ["0.0.0.0:8080"]

    asyncio.run(serve(app, config))
