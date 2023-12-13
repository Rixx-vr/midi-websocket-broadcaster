#!/usr/bin/env python

import argparse
import asyncio
import os
import rtmidi
import websockets
from websocket_server import MidiMenu, WebsocketServer

def midi_callback(signal, user_data):
    status = int(f'{signal[0][0]:08b}'[0:4], 2)
    channel = int(f'{signal[0][0]:08b}'[4:8], 2)

    if len(signal[0]) == 3:
        print(f"status: {status} channel: {channel} byte3: {signal[0][1]} byte4: {signal[0][2]} :: t: {signal[1]}")
    else:
        print(f"status: {status} channel: {channel} byte3: {signal[0][1]} :: t: {signal[1]}")
    msg = bytes(bytearray(signal[0])).hex(sep="-")

    asyncio.run(user_data.send_to_clients(msg))


def main():
    parser = argparse.ArgumentParser(
        prog="midi-websocket-broadcaster",
        description="Start the MIDI broadcast server."
    )
    parser.add_argument("-H", "--host", type=str, help="Interface to host server on (default: %(default)s)", default=os.getenv("HOST", "localhost"))
    parser.add_argument("-P", "--port", type=int, help="Port to host server on (default: %(default)s)", default=int(os.getenv("POST", 12345)))

    args = parser.parse_args()

    midi_in = rtmidi.MidiIn()

    menu = MidiMenu(midi_in)
    menu.show_menu()

    server = WebsocketServer()
    start_server = websockets.serve(server.ws_handler, args.host, args.port)

    midi_in.set_callback(midi_callback, server)
    midi_in.open_port(menu.get_device_port())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()


if __name__ == "__main__":
    main()