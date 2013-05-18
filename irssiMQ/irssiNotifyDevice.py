import argparse
import threading
import zmq
import Queue


class Reader(threading.Thread):

    def __init__(self, queue, socket):
        threading.Thread.__init__(self)
        self.queue = queue
        self.socket = socket

    def run(self):
        """Recv messages from frontend."""

        while True:
            msg = self.socket.recv()
            print "Message:", msg
            self.socket.send("ACK")
            self.queue.put(msg)


class Writer(threading.Thread):

    def __init__(self, queue, socket):
        threading.Thread.__init__(self)
        self.queue = queue
        self.socket = socket

    def run(self):
        """Send messages to backend."""

        while True:
            msg = self.queue.get()
            print msg

            self.socket.send(msg)
            self.socket.recv()


def main():
    """ZMQ device to enqueue/dequeue messages"""

    parser = argparse.ArgumentParser()

    parser.add_argument("frontend_host", type=str,
                        help="Local server address")
    parser.add_argument("backend_host", type=str,
                        help="Pub server address")
    parser.add_argument("xrep_port", type=int,
                        help="Frontend server port")
    parser.add_argument("xreq_port", type=int,
                        help="Backend server port")

    args = parser.parse_args()

    msg_queue = Queue.Queue()

    try:
        context = zmq.Context()
        xrep_port = args.xrep_port
        xreq_port = args.xreq_port
        # Socket facing clients
        frontend = context.socket(zmq.REP)
        frontend.bind("tcp://%s:%d" % (args.frontend_host, xrep_port))

        # Socket facing services
        backend = context.socket(zmq.REQ)
        backend.bind("tcp://%s:%d" % (args.backend_host, xreq_port))

        reader = Reader(msg_queue, frontend)
        reader.start()
        
        writer = Writer(msg_queue, backend)
        writer.start()

        while True:
            continue

    except Exception, e:
        print e
        print "Bringing down ZMQ device..."
    finally:
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":

    main()
