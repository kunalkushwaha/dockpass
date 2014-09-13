import asyncore
import socket
import lib.repolist


class PAASCmdHandler(asyncore.dispatcher_with_send):

    def get_repo_list(self):
	#lib.repolist.get_repolist()
	return lib.repolist.get_repolist()
    
    def setup_docker(name):
	print name
	return "238429"
    
    def rmi(self):
	return "rmi"

    def instancelist(self):
	return "instancelist"
	
    
    

    def handle_read(self):
        data = self.recv(8192)
	arguments = data.split()

	for token in arguments:
            print(token)
	    if token == "repolist":
		returnmsg = self.get_repo_list()
		print returnmsg
		self.send(returnmsg)
	    if token == "setup":
		returnmsg = self.setup_docker()
		print returnmsg
		self.send(returnmsg)
	    if token == "rmi":
		returnmsg = self.rmi()
		print returnmsg
		self.send(returnmsg)	
	    if token == "instancelist":
		returnmsg = self.instancelist()
		print returnmsg
		self.send(returnmsg)
	#    if token == "repolist":
	#	returnmsg = self.get_repo_list()
	#	print returnmsg
	#	self.send(returnmsg)
	#    if token == "repolist":
	#	returnmsg = self.get_repo_list()
	#	print returnmsg
	#	self.send(returnmsg)
	#    if token == "repolist":
	#	returnmsg = self.get_repo_list()
	#	print returnmsg
	#	self.send(returnmsg)
	#    if token == "repolist":
	#	returnmsg = self.get_repo_list()
	#	print returnmsg
	#	self.send(returnmsg)
	#    if token == "repolist":
	#	returnmsg = self.get_repo_list()
	#	print returnmsg
	#	self.send(returnmsg)		
	

class PAASServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = PAASCmdHandler(sock)

server = PAASServer('localhost', 8080)
asyncore.loop()
