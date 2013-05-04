import zmq

port = "5560"
context = zmq.Context()
socket = context.socket(zmq.REP)
server_id = 'local-irssi'

socket.connect("tcp://127.0.0.1:%s" % port)

while True:
    message = socket.recv()
    print "Received request:", message
    socket.send("ACK from server %s" % server_id)
