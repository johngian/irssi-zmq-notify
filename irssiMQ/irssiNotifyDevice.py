import argparse
import threading
import zmq
import Queue


class Reader(threading.Thread):

    def __init__(self, queue, port, host):
        threading.Thread.__init__(self)
        self.queue = queue
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://%s:%d" % (host, port))


    def run(self):
        """Recv messages from frontend."""

        while True:
            msg = self.socket.recv()
            print "Message:", msg
            self.socket.send("ACK")
            self.queue.put(msg)


class Writer(threading.Thread):

    def __init__(self, queue, port, host):
        threading.Thread.__init__(self)
        self.queue = queue
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.bind("tcp://%s:%d" % (host, port))


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
        xrep_port = args.xrep_port
        xreq_port = args.xreq_port

        reader = Reader(msg_queue, xrep_port, args.frontend_host)
        reader.start()
        
        writer = Writer(msg_queue, xreq_port, args.backend_host)
        writer.start()
        
        reader.join()
        writer.join()

    except Exception, e:
        print e
        print "Bringing down ZMQ device..."


if __name__ == "__main__":

    main()
