import socket
import argparse



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

def useArguments(args):

    if args.repolist:
        client_socket.send("repolist ")
        pass
    if args.setup:
        client_socket.send("setup " + args.setup)
        pass
    if args.rmi:
        client_socket.send("rmi " + args.rmi)
    if args.instancelist:
        client_socket.send("instancelist ")
    if args.init:
        client_socket.send("init " + args.init)
    if args.add:
        client_socket.send("add " + args.add)
    if args.push:
        client_socket.send("push " + args.push)
    if args.pull:
        client_socket.send("pull " + args.pull)
      


parser = argparse.ArgumentParser(description='DocPAAS Client')
parser.add_argument('-l','--repolist', action='store_true', help='list all enviornment image at server')
parser.add_argument('-s','--setup', help='Setup environment for specified repo ')
parser.add_argument('-r','--rmi', help='remove/delete the instance ')
parser.add_argument('-il','--instancelist', action='store_true', help='instance list ')
parser.add_argument('-init','--init', help='git init ')
parser.add_argument('-add','--add', help='git add ')
parser.add_argument('-push','--push', help='git push')
parser.add_argument('-pull','--pull', help='git pull ')

args = parser.parse_args()
useArguments(args)

data = client_socket.recv(8192)
print data
client_socket.close()


