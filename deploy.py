#!/usr/bin/env python 

#Done by: Victor
#latest update github.com/codeflavour/susebottle/deploy.py


'''
                                          Deploy Bottle web framework on OpenSuse 13.1
                                          Uses pip, nginx, uwsgi, uwsgi-python 
                                          OpenSuse 13.1 comes with python by default,
                                          recommended python version is 2.7xx
'''

import os
import sys
import subprocess

_version = 0.1


PKGMAN = 'zypper'
SUPERU = 'sudo'
#DEBUG = True  #using this for debuging purpose
DEBUG = False
INSTALL = 'in' 
PIP = 'pip'

zypTpl = ('python-pip','uwsgi','uwsgi-python','nginx')

pipTpl = ('bottle','uwsgi')

#open devnull and redirect all output there
if not DEBUG:
   redout = open('/dev/null','w')
else:
   redout = sys.stdout
   SUPERU = ''

#start updating with zypper 

def zypinstall():
   for module in zypTpl:
        print 'Using zypper to install', str(module)
        try:
           returncode = subprocess.check_call([SUPERU, PKGMAN,INSTALL ,module],stdout=redout)
           print "[...Done]", returncode
        except OSError:
           print "There was an error installing",module, sys.stderr

def main():
    if os.getuid() != 0:
        exit("You don't have the necessary access privileges, try running this with sudo")
    else:
         zypinstall()
    

if __name__=='__main__':
    main()
