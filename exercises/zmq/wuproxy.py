# Weather proxy device
#
# Author: Lev Givon <lev(at)columbia(dot)edu>

import zmq

context = zmq.Context()

# This is where the weather server sits
frontend = context.socket(zmq.SUB)
frontend.connect("tcp://*:5556")

# This is our public endpoint for subscribers
backend = context.socket(zmq.PUB)
backend.bind("tcp://*:5555")

# Subscribe on everything
frontend.setsockopt(zmq.SUBSCRIBE, b'')

# Shunt messages out to our own subscribers
while True:
    # Process all parts of the message
    message = frontend.recv_multipart()
    backend.send_multipart(message)
