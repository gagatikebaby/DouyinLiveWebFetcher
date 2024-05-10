#!/usr/bin/python
# coding:utf-8

# @FileName:    main.py
# @Time:        2024/1/2 22:27
# @Author:      bubu
# @Project:     douyinLiveWebFetcher

import asyncio
import websockets
from liveMan import DouyinLiveWebFetcher

# async def echo(websocket, path):
#     async for message in websocket:
#         print(f"Received message: {message}")
#         await websocket.send(f"Echo: {message}")
# start_server = websockets.serve(echo, "localhost", 8765)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    live_id = '26012747113'
    DouyinLiveWebFetcher(live_id).start()
