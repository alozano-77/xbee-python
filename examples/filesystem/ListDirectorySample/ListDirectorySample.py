# Copyright 2019, 2020, Digi International Inc.
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

from digi.xbee.filesystem import FileSystemException
from digi.xbee.devices import XBeeDevice
from digi.xbee.exception import XBeeException

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600
# TODO: Replace with the name of the remote XBee to use. If empty, local is used.
REMOTE_NODE_ID = None
# TODO: Replace with the XBee file system path to list its contents. Leave as 'None' to use '/flash'.
PATH_TO_LIST = None


def main():
    print(" +-------------------------------------------+")
    print(" | XBee Python Library List Directory Sample |")
    print(" +-------------------------------------------+\n")

    local_xbee = XBeeDevice(PORT, BAUD_RATE)
    fs_xbee = local_xbee

    try:
        local_xbee.open()

        if REMOTE_NODE_ID:
            # Obtain the remote XBee from the network.
            xbee_network = local_xbee.get_network()
            fs_xbee = xbee_network.discover_device(REMOTE_NODE_ID)
            if not fs_xbee:
                print("Could not find remote device '%s'" % REMOTE_NODE_ID)
                exit(1)

        filesystem_manager = fs_xbee.get_file_manager()

        path_to_list = PATH_TO_LIST
        if not path_to_list:
            path_to_list = "/flash"
        files = filesystem_manager.list_directory(path_to_list)
        print("Contents of '%s' (%s):\n" %
              (path_to_list, fs_xbee if fs_xbee.is_remote() else "local"))
        for file in files:
            print(file)
    except (XBeeException, FileSystemException) as e:
        print("ERROR: %s" % str(e))
        exit(1)
    finally:
        if local_xbee and local_xbee.is_open():
            local_xbee.close()


if __name__ == '__main__':
    main()
