import os

def get_repolist():
    dirlist = ''
    for dirname, dirnames, filenames in os.walk('./repolist'):
        print dirnames
        dirlist += '\n'.join(dirnames)
    print dirlist
    return dirlist

