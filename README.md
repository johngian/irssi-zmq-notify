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
* argparse (only required for python < 2.7)

Installation:
-------------
Run:
    python setup.py build
    python setup.py install

Copy the modified notify.pl on irssi scripts folder and run:
    /load perl
    /script load notify.pl

How to use:
-----------
Initialize the ZeroMQ device:
    nohup ./irssi-mq.py

Run on your local machine the notifications server:
    nohup ./irssi-notify-server.py
