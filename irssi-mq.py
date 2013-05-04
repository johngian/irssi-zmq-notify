import zmq

def main():
    try:
        context = zmq.Context()
        # Socket facing clients
        frontend = context.socket(zmq.XREP)
        frontend.bind("tcp://127.0.0.1:5559")
        # Socket facing services
        backend = context.socket(zmq.XREQ)
        backend.bind("tcp://127.0.0.1:5560")
        zmq.device(zmq.QUEUE, frontend, backend)
    except Exception, e:
        print e
        print "bringing down zmq device"
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":
    main()
