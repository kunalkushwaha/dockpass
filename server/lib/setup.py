import subprocess
import docker
import json

def do_docker_setup(tag):
 
    
    c = docker.Client(base_url='unix://var/run/docker.sock',
                  version='1.12',
                  timeout=10)
    
    
    msg = c.images()
    msgstr = json.dumps(msg)
    print msgstr
 
    return msgstr
    
