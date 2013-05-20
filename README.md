IRSSI notifications over ZeroMQ
===============================

Features:
---------

* This project aims to enable notifications on local machine when using IRSSI client remotely.
* Based on ZeroMQ
* Heavily based on irssi-libnotify: http://code.google.com/p/irssi-libnotify

Dependencies:
-------------
* pyzmq
    * python-dev
    * libzmq-dev
* argparse (only required for python < 2.7)
* pynotify

Installation:
-------------
Installation tested only on debian system.
First you need to install the required packages:
```
    apt-get install libzmq-dev python-dev python-notify
```

To install the irssi-zmq-notify scripts run:
```
    python setup.py build
    python setup.py install
```
Copy the modified notify.pl on irssi scripts folder and run:
```
    /load perl
    /script load notify.pl
    /set notify_remote_host local_interface
    /set notify_remote_port local_port
```
How to use:
-----------
Initialize the ZeroMQ device on the remote machine (e.g 127.0.0.1 for local interface, public IP for the public interface, 5559, 5560 ports for connections):
```   
    nohup irssi-mq local_interface public_interface rep_port req_port &
```

Run on your local machine the notifications server:
```   
    nohup irssi-notify-server remote_hostname req_port &
```
