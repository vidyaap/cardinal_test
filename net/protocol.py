import asyncio
from .handler import Handler


class CardinalProtocol(asyncio.Protocol):
    def __init__(self, peer):
        self.peer = peer
        self.buffer = b""
        self.transport = None
        self.handler = Handler(peer, self)

    def connection_made(self, transport: asyncio.transports.BaseTransport):

        peername = transport.get_extra_info("peername")
        print("Server connection made from: {}".format(peername))
        self.transport = transport

    def connection_lost(self, exc):
        print('The server closed the connection')

    def data_received(self, data: bytes):
        self.buffer += data
        self.handle_lines()

    def handle_lines(self):
        while b"\n\n\n" in self.buffer:
            data, self.buffer = self.buffer.split(b"\n\n\n", 1)
            self.handler.handle_msg(data)