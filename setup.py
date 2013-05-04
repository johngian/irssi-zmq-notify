from setuptools import setup, find_packages

setup(
    name = "irssi-zmq-notify",
    version = "0.1",
    packages = ["irssiMQ"],
    install_requires = ['argparse', 'pyzmq==2.2.0.1'],

    entry_points = {
        'console_scripts': [
            'irssi-notify = irssiMQ.irssiNotifyClient:main',
            'irssi-mq = irssiMQ.irssiNotifyDevice:main',
            'irssi-notify-server = irssiMQ.irssiNotifyServer:main'
            ]
        },

    author = "John Giannelos",
    author_email = "johngiannelos@gmail.com",
    description = "Irssi notification over ZeroMQ",
    license = "GNU General Public License",
)
