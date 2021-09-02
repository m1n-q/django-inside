#!/usr/bin/env python

# WS server example
import sys
import asyncio
import websockets

async def chatserver(websocket, path):
    while True:
        data = await websocket.recv()
        user = data[0:data.index(':')]
        msg = data[data.index(':') + 1:]
        print(user, msg)
        await websocket.send(msg)

port = int(sys.argv[1])
start_server = websockets.serve(chatserver, "localhost", port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
