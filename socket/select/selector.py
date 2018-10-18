import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    try:
        data = conn.recv(1000)  # Should be ready
        if not data:
            raise Exception
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    except Exception as err:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(("127.0.0.1", 8001))
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)