import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
#This is a comment added to check github
s.connect(("www.python.org", 82))
#how fixwd length is important in socket
import socket

class SocketHandler:

  def __init__(self, sock=None):
    if sock is None:
      self.sock = socket.socket(
      socket.AF_INET, socket.SOCK_STREAM)
    else:
      self.sock = sock

  def connect(self, host, port):
    self.sock.connect((host, port))

  def send(self, msg):
    totalsent = 0
    MSGLEN = len(msg)
    while totalsent < MSGLEN:
      sent = self.sock.send(msg[totalsent:])
      if sent == 0:
        raise RuntimeError("socket connection broken")

      totalsent = totalsent + sent

  def receive(self, EOFChar='\036'):
    msg = ''
    MSGLEN = 100
    while len(msg) < MSGLEN:
      chunk = self.sock.recv(MSGLEN-len(msg))
      if chunk.find(EOFChar) != -1:
        msg = msg + chunk
        return msg

      msg = msg + chunk
      return msg

