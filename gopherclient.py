
import socket,sys

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]



try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
    print("Strange error creating socket: {0}".format(e))
    sys.exit(1)

try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservbyname(textport,"tcp")
    except socket.error as e:
        print("couldn't find your port :{0}".format(e))
        sys.exit(1)
try:
    s.connect((host,port))
except socket.gaierror as e:
    print("Address-related error connecting to server: {0}".format(e))
    sys.exit(1)
except socket.error as e:
    print("Connection error:{0}".format(e))
    sys.exit(1)

try:
    s.sendall("GET {0} HTTP/1.0\r\n\r\n".format(filename))
except socket.error as e :
    print("Error sending data: {0}".format(e))
    sys.exit(1)

while 1:
    try:
        buf = s.recv(2048)
    except socket.error as e:
        print("Error receiving data: {0}".format(e))
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)