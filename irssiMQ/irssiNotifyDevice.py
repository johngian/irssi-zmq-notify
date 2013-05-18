import argparse
import threading
import zmq
import Queue


class Reader(threading.Thread):

    def __init__(self, queue, socket):
        super(Reader, self).__init__(self)
        self.queue = queue
        self.socket = socket

    def run(self):
        """Recv messages from frontend."""

        while True:
            msg = self.socket.recv()
            self.socket.send("ACK")
            self.queue.put(msg)


class Writer(threading.Thread):

    def __init__(self, queue, socket):
        super(Writer, self).__init__(self)
        self.queue = queue
        self.socket = socket

    def run(self):
        """Send messages to backend."""

        while True:
            msg = self.queue.get()
            self.socket.send(msg)
            self.socket.recv()


def main():
    """ZMQ device to enqueue/dequeue messages"""

    parser = argparse.ArgumentParser()

    parser.add_argument("host", type=str,
                        help="Pub server address")
    parser.add_argument("xrep_port", type=int,
                        help="Frontend server port")
    parser.add_argument("xreq_port", type=int,
                        help="Backend server port")

    args = parser.parse_args()

    msg_queue = Queue.Queue()

    try:
        context = zmq.Context()
        host = args.host
        xrep_port = args.xrep_port
        xreq_port = args.xreq_port
        # Socket facing clients
        frontend = context.socket(zmq.XREP)
        frontend.bind("tcp://%s:%d" % (host, xrep_port))
        # Socket facing services
        backend = context.socket(zmq.XREQ)
        backend.bind("tcp://%s:%d" % (host, xreq_port))

        reader = Reader(msg_queue, frontend)
        reader.setDaemon(True)
        reader.start()

        writer = Writer(msg_queue, backend)
        writer.setDaemon(True)
        writer.start()

    except Exception, e:
        print e
        print "Bringing down ZMQ device..."
    finally:
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":

    main()
