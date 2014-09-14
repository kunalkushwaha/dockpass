import subprocess
import docker
import json
import os

def do_docker_setup(tag):
 
    print tag  
    #print echo_git_init
    c = docker.Client(base_url='unix://var/run/docker.sock',
                  version='1.12',
                  timeout=20)
   
    #/home/samrat/DOCPASS/dockpass/server
 
    #fo = open("./repolist/nodejs/Dockerfile", "r")   
    
   # build_responce = c.build(path='/home/samrat/DOCPASS/repolist/nodejs/Dockerfile', tag=None, quiet=False,
    #                         fileobj=None, nocache=False,
     #                        rm=False, stream=False, timeout=None,
      #                       custom_context=False, encoding=None)
    
    

   #build_responce = c.create_container("ubuntu", command='/bin/bash', hostname=None, user=None,
    #                               detach=False, stdin_open=False, tty=True, mem_limit=0,
     #                              ports=None, environment=None, dns=None, volumes=None,
      #                             volumes_from=None, network_disabled=False, name=tag,
       #                            entrypoint=None, cpu_shares=None, working_dir=None,
        #                           memswap_limit=0)
   


#import os
  #echo_git_dir = 'echo "RUN mkdir -p /gitserver/%s.git" >> /DockerRepo/%s/Dockerfile' %( reponame, dockerfile)
  #echo_git_init = 'echo "RUN git init --bare --shared /gitserver/%s.git" >> /DockerRepo/%s/Dockerfile' %( reponame, dockerfile)
 # os.system(echo_git_dir)
  #os.system(echo_git_init)
#docker tag 91a9f658acd7 python:pyapp
 # cmd = 'docker build -t %s /DockerRepo/%s' % ( reponame, dockerfile )
    delete_dockerfile = 'rm -f ./repolist/%s/Dockerfile' % ( tag )
    os.system(delete_dockerfile) 
    docker_build = 'docker build ./repolist/%s' % ( tag )
    #os.system(docker_build)
    create_temp_file = 'touch ./repolist/%s/Dockerfile' % ( tag )
    os.system(create_temp_file)
    copy_template = 'cp ./repolist/%s/%s ./repolist/%s/Dockerfile' % ( tag, tag, tag)
    os.system(copy_template)
    echo_git_dir = 'echo "RUN mkdir -p /gitserver/%s.git" >> ./repolist/%s/Dockerfile' %( tag, tag)
    echo_git_init = 'echo "RUN git init --bare --shared /gitserver/%s.git" >> ./repolist/%s/Dockerfile' %( tag, tag)
    os.system(echo_git_dir)
    os.system(echo_git_init)
    output = subprocess.check_output(docker_build, shell=True)
    log = open("./repolist/temp.txt", "a")
    log.write(output)
    print output
    cmd_image_id = 'cat ./repolist/temp.txt | tail -1 | awk \'{print $3}\' | head'
    image_id = subprocess.check_output(cmd_image_id, shell=True)
    print image_id
    run_image = 'docker run -d %s /bin/bash' % ( image_id )
    print run_image 
    os.system(run_image)
    return(output);






 
    #print build_responce
    #print json.dumps(build_responce)
 
   # return json.dumps(build_responce)
   
