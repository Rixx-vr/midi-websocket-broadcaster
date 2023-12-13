#!/usr/bin/env python

import asyncio
import logging
from websockets import WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)

class WebsocketServer:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol) -> None:
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connected.')

    async def unregister(self, ws: WebSocketServerProtocol) -> None:
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnected.')

    async def send_to_clients(self, message: str) -> None:
        if self.clients:
            await asyncio.gather(
                *[client.send(message) for client in self.clients]
            )

    async def ws_handler(self, ws: WebSocketServerProtocol, uri: str) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        except Exception as e:
            logging.error(f"Error in message distribution: {e}")
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: WebSocketServerProtocol) -> None:
        async for message in ws:
            try:
                await self.send_to_clients(message)
            except Exception as e:
                logging.error(f"Error sending message: {e}")
                break
