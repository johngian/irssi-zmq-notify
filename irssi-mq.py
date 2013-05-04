import zmq

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
    host = "127.0.0.1"
    xrep_port = 5559
    xreq_port = 5560
    run_device(host, xrep_port, xreq_port)
