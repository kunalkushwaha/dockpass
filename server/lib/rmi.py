import subprocess
import docker
import json

def get_image_list():
   
    c = docker.Client(base_url='unix://var/run/docker.sock',
                  version='1.12',
                  timeout=10)
   
    msg = c.containers(quiet=False, all=False, trunc=True, latest=False, since=None,
             before=None, limit=-1)
 
    return json.dumps(msg)
    