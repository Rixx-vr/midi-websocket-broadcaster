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
    global g_server
    msg = bytes(bytearray(signal[0])).hex(sep="-")
    asyncio.run(g_server.send_to_clients(msg))

parser = argparse.ArgumentParser(
    prog="midi-websocket-broadcaster",
    description="Start the MIDI broadcast server."
)
parser.add_argument("-H", "--host", type=str, help="Interface to host server on (default: %(default)s)", default=os.getenv("HOST", "localhost"))
parser.add_argument("-P", "--port", type=int, help="Port to host server on (default: %(default)s)", default=int(os.getenv("POST", 12345)))

args = parser.parse_args()

global g_midi_in
g_midi_in = rtmidi.MidiIn()
global g_websocket
g_websocket = None

menu = MidiMenu(g_midi_in)
menu.show_menu()

global g_server
g_server = WebsocketServer()
start_server = websockets.serve(g_server.ws_handler, args.host, args.port)

g_midi_in.set_callback(midi_callback)
g_midi_in.open_port(menu.get_device_port())

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()