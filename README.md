IRSSI notifications over ZeroMQ
===============================

Features:
---------

* This project aims to enable notifications on local machine when using IRSSI client remotely.
* Based on ZeroMQ (...actually started it to see how zmq works :smile: )
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
    /set notify_remote_host remote_hostname
    /set notify_remote_port port
```
How to use:
-----------
Initialize the ZeroMQ device on the remote machine:
```   
    nohup irssi-mq remote_hostname xrep_port xreq_port &
```

Run on your local machine the notifications server:
```   
    nohup irssi-notify-server remote_hostname xreq_port &
```