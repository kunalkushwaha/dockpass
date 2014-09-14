import subprocess
import docker
import json

def do_docker_setup(tag):
 
    
    c = docker.Client(base_url='unix://var/run/docker.sock',
                  version='1.12',
                  timeout=10)
    
    fo = open("./repolist/nodejs/Dockerfile", "r")   
    
    #build_responce = c.build(path='./repolist/nodejs/', tag=tag, quiet=False,
    #                         fileobj=None, nocache=False,
    #                         rm=False, stream=False, timeout=None,
    #                         custom_context=False, encoding='tar')
    
    build_responce = c.create_container("ubuntu", command='/bin/bash', hostname=None, user=None,
                                   detach=False, stdin_open=False, tty=True, mem_limit=0,
                                   ports=None, environment=None, dns=None, volumes=None,
                                   volumes_from=None, network_disabled=False, name=tag,
                                   entrypoint=None, cpu_shares=None, working_dir=None,
                                   memswap_limit=0)
    
    print build_responce
    #print json.dumps(build_responce)
 
    return json.dumps(build_responce)
    
