import argparse
import pynotify
import zmq


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str,
                        help="Pub server address")
    parser.add_argument("port", type=int,
                        help="Frontend server port")
    args = parser.parse_args()

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    server_id = 'local-irssi'
    socket.connect("tcp://%s:%d" % (args.host, args.port))

    pynotify.init('IRSSI notifications')

    while True:
        message = socket.recv()
        notification = pynotify.Notification("IRSSI", message)
        print "Received request:", message
        socket.send("ACK from server %s" % server_id)
        notification.show()
        
if __name__ == "__main__":
    main()
