import asyncio

class server():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.loop = asyncio.get_event_loop()
        self.coro = self.loop.create_server(
            ClientServerProtocol,
            self.host, self.port
        )
        self.server = self.loop.run_until_complete(self.coro)
        try:
            self.loop.run_forever()
        except (KeyboardInterrupt, TimeoutError, asyncio.TimeoutError):
            pass
        self.server.close()
        self.loop.run_until_complete(self.server.wait_closed())
        self.loop.close()

    storage = dict()


class ClientServerProtocol(asyncio.Protocol):
    def process_data(self, data):
        data = data.strip('\n').split()
        if data[0] == 'put':
            try:
                (command, key, value, timesnap) = tuple(data)
            except ValueError:
                return 'Error'

            if server.storage.get(key, None):
                for mark in range(len(server.storage[key])):
                    if server.storage[key][mark][0] == timesnap:
                        server.storage[key][mark] = (timesnap, value)
                        break
                else:
                    server.storage[key].append((timesnap, value))
            else:
                server.storage[key] = [(timesnap, value),]
            return 'ok'

        elif data[0] == 'get':
            try:
                (command, key) = tuple(data)
                if key != '*':
                    server.storage[key]
            except (ValueError, KeyError):
                return 'Error'
            
            return_value =  'ok\n'
            if key == '*':
                for note in list(server.storage.items()):
                    print(note)
                    for pair in note[1]:
                        return_value += (note[0] + ' ' + pair[0] + ' ' + pair[1] + '\n')
            else:
                for pair in server.storage[key]:
                    return_value += (key + ' ' + pair[0] + ' ' + pair[1] + '\n')
            return return_value

        else:
            return 'Error'
                
    def connection_made(self, transport):
        self.transport = transport
        print('Connection made')

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

