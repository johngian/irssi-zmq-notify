import argparse
import zmq

parser = argparse.ArgumentParser()
parser.add_argument("msg", type=str,
                    help="Message to be published")
parser.add_argument("address", type=str,
                    help="Pub server address")
parser.add_argument("port", type=int,
                    help="Pub server port")
args = parser.parse_args()

def send_message(socket, msg):
    socket.send(msg)

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://%s:%d" % (args.address, args.port))
    send_message(socket, args.msg)
    reply = socket.recv()
