import asyncore, socket
import argparse

class PAASClient(asyncore.dispatcher):

    def __init__(self, host, path, buff):
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
	#print "Reading"	
        print self.recv(8192)
	exit()

    def writable(self):
	#print "Writable.."
        return (len(self.buffer) > 0)

    def handle_write(self):
	#print "writeing..."
        sent = self.send(self.buffer)
	self.buffer = self.buffer[sent:]
	


parser = argparse.ArgumentParser(description='DocPAAS Client')
parser.add_argument('repolist', metavar='-rl', help='list all enviornment image at server')
parser.add_argument('setup', metavar='-s', help='Setup environment for specified repo ')
#p = PASSCmdLine(parser)
args = parser.parse_args()
print args

if args.repolist == "232":
	client = PAASClient('localhost', '/',args.setup)
	asyncore.loop()
