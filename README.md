# midi-websocket-broadcaster

This package contains a websocket server that will broadcast MIDI from a selected port through a websocket.

This currently supports the selection of only one midi device, but supports multiple clients.

## Running the server

usage: midi-websocket-broadcaster [-h] [-H HOST] [-P PORT]

Start the MIDI broadcast server.

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  Interface to host server on (default: localhost)
  -P PORT, --port PORT  Port to host server on (default: 12345)

## Using the server

The server will infinitely loop until it detects MIDI devices to select from, then show a menu prompt to select, like so:
```
[0] :: Oxygen 61 0

Select device:    
```

Enter the number in the square brackets to select the device you wish to transmit.

## Stopping the server

To stop the server, provide the keyboard interrupt signal for your terminal / os. (Usually CTRL + C)