import asyncore
import socket
import lib.repolist
import lib.setup
import lib.instancelist


class PAASCmdHandler(asyncore.dispatcher_with_send):

    def get_repo_list(self):
	#lib.repolist.get_repolist()
	return lib.repolist.get_repolist()
    
    def setup_docker(self, tag):
	print "executing setup"
	return lib.setup.do_docker_setup(tag)
	#return "setup"
    
    def rmi(self):
	return "rmi"

    def instancelist(self):
	#return "OK"
	return lib.instancelist.get_image_list()

    def handle_read(self):
        data = self.recv(8192)
	token, value = data.split()
	print token
	print value

	if token == "repolist":
	    returnmsg = self.get_repo_list()
	    self.send(returnmsg)
	if token == "setup":
	    #returnmsg = self.setup_docker(value)
	    self.send(self.setup_docker(value))
	    
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
            #print 'Incoming connection from %s' % repr(addr)
            handler = PAASCmdHandler(sock)

server = PAASServer('localhost', 8080)
asyncore.loop()
