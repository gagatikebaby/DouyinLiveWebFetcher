#!/usr/bin/python
# coding:utf-8

# @FileName:    main.py
# @Time:        2024/1/2 22:27
# @Author:      bubu
# @Project:     douyinLiveWebFetcher

import asyncio
import websockets
from liveMan import DouyinLiveWebFetcher

async def main():
    live_id = '519836445130'
    DouyinLiveWebFetcher(live_id).start()

    async def echo(websocket, path):
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")

    start_server = websockets.serve(echo, "localhost", 8765)
    await start_server

asyncio.run(main())


