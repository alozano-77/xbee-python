# Copyright 2019, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from digi.xbee.devices import XBeeDevice
from digi.xbee.models.options import XBeeLocalInterface
import time

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600
DEST_INTERFACE = XBeeLocalInterface.BLUETOOTH
# TODO: Optionally, replace with the text of the message.
DATA_TO_SEND = "Hello from the serial interface (#%s)"


def main():
    print(" +-------------------------------------------------+")
    print(" | XBee Python Library Send User Data Relay Sample |")
    print(" +-------------------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        for i in range(10):
            data = (DATA_TO_SEND % (i + 1))

            print("Sending User Data Relay to %s >> '%s'... " %
                  (DEST_INTERFACE.name, data), end="")

            device.send_user_data_relay(DEST_INTERFACE, data.encode("utf-8"))

            print("Success")

            time.sleep(1)
    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
