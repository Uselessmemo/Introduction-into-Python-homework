import socket
import time

class Client():
    def __init__(self, addres, port, timeout):
        self.addres = addres
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((self.addres, self.port), timeout = self.timeout)
        self.sock.settimeout(self.timeout)
        try:
            print("Connection set!")
        except socket.timeout:
            print('Timeout')
            self.sock.close()

    def get(self, key):
        self.sock.sendall(f'get {key}\n'.encode())
        data = self.sock.recv(1024).decode().split('\n')
        answer = dict()
        if data[0] == 'ok':
            for num in range(1,len(data)):
                tmp = data[num].split()
                if tmp:
                    if answer.get(tmp[0], None):
                        answer[tmp[0]].append((tmp[1], tmp[2]))
                    else:
                        answer[tmp[0]] = [(tmp[1], tmp[2]),]
        return answer

    def put(self, key, value, timestamp = None):
        self.sock.sendall(f'put {key} {value} {timestamp}\n'.encode())
        data = self.sock.recv(1024).decode()
        data =  data or 'Connection error'
        return data

