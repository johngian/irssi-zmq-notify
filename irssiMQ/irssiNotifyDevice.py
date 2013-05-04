import zmq
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host", type=str,
                    help="Pub server address")
parser.add_argument("xrep_port", type=int,
                    help="Frontend server port")
parser.add_argument("xreq_port", type=int,
                    help="Backend server port")
args = parser.parse_args()


def run_device(host, xrep_port, xreq_port):
    """ZMQ device to enqueue/dequeue messages"""
    try:
        context = zmq.Context()
        # Socket facing clients
        frontend = context.socket(zmq.XREP)
        frontend.bind("tcp://%s:%d" % (host, xrep_port))
        # Socket facing services
        backend = context.socket(zmq.XREQ)
        backend.bind("tcp://%s:%d" % (host, xreq_port))
        zmq.device(zmq.QUEUE, frontend, backend)
    except Exception, e:
        print e
        print "Bringing down ZMQ device..."
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":
    run_device(args.host, args.xrep_port, args.xreq_port)
