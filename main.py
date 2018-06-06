import os
from os import environ
from subprocess import Popen
import time
import urllib
import socket
import socks
from random import randrange
import json
from contextlib import contextmanager


@contextmanager
def tor_proxy(port):

    from tempfile import mkstemp
    fd, tmp = mkstemp(".torrc")
    fd_datadir, data_dir = mkstemp(".data")
    os.unlink(data_dir)
    os.makedirs(data_dir)

    with open(tmp, "w") as f:
        f.write("SOCKSPort {}\n".format(port))
        f.write("DataDirectory {}\n".format(data_dir))

    socks.set_default_proxy(socks.SOCKS5, "localhost", port)
    socket.socket = socks.socksocket

    tor_path = os.path.join(environ["LAMBDA_TASK_ROOT"], "tor")
    process = Popen([tor_path, "-f", tmp], cwd=os.path.dirname(data_dir))
    yield
    process.terminate()


def lambda_handler(event, context):

    port = randrange(9000, 10000)
    with tor_proxy(port):
        count = 10
        while count > 0:
            try:
                s = urllib.request.urlopen('http://ifconfig.co/json').read()
                result = json.loads(s)
                result['port'] = port
                return json.dumps(result)
            except Exception as e:
                time.sleep(3)
                pass

    return '{}'



