import asyncore, socket

class PAASClient(asyncore.dispatcher):

    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, 8080) )
        self.buffer = 'Hello World'

    def handle_connect(self):
	print "Connected"
        pass

    def handle_close(self):
	print "Closed"
        self.close()

    def handle_read(self):
	
        print self.recv(8192)

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]


client = PAASClient('localhost', '/')
asyncore.loop()
