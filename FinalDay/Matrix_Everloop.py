# This is how we connect to the creator. IP and port.
# The IP is the IP I'm using and you need to edit it.
# By default, MALOS has its 0MQ ports open to the world.
#
# Every device is identified by a base port. Then the mapping works
# as follows:
# BasePort     => Configuration port. Used to config the device.
# BasePort + 1 => Keepalive port. Send pings to this port.
# BasePort + 2 => Error port. Receive errros from device.
# BasePort + 3 => Data port. Receive data from device.
# (see README file for more details)

# NOTE:
# before run this example please execute:
# pip install pyzmq protobuf matrix_io-proto

import os
import random
import time
import zmq
from matrix_io.proto.malos.v1 import driver_pb2
from matrix_io.proto.malos.v1 import io_pb2

# sets all of the LEDS to a given rgbw value
def set_everloop_color(red=0, green=0, blue=0, white=0):
    """Submit a R,G,B,W value between 0-255"""

    # or local ip of MATRIX creator
    creator_ip = os.environ.get('CREATOR_IP', '127.0.0.1')

    # port for everloop driver
    creator_everloop_base_port = 20013 + 8

    # grab zmq context
    context = zmq.Context()

    # get socket for config
    config_socket = context.socket(zmq.PUSH)
    config_socket.connect('tcp://{0}:{1}'.format(creator_ip, creator_everloop_base_port))

    # create a new driver config strut
    config = driver_pb2.DriverConfig()

    # initialize an empty list for the "image" or LEDS
    image = []

    # iterate over all 35 LEDS and set the rgbw value of each
    # then append it to the end of the list/image thing
    for led in range(35):
        ledValue = io_pb2.LedValue()
        ledValue.blue = blue
        ledValue.red = red
        ledValue.green = green
        ledValue.white = white
        image.append(ledValue)

    # add the "image" to the config driver
    config.image.led.extend(image)

    # send a serialized string of the driver config
    # to the config socket
    config_socket.send(config.SerializeToString())


if __name__ == '__main__':
    while True:
        # Set random values for R, G and B
        set_everloop_color(255,255,255)
        time.sleep(1)
	set_everloop_color(0,0,0)
	time.sleep(1)
