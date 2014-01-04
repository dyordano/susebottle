#!/usr/bin/env python 

#Done by: Victor
#latest update github.com/codeflavour/susebottle


'''
                                          Deploy Bottle web framework on OpenSuse 13.1
                                          Uses pip, nginx, uwsgi, uwsgi-python 
                                          OpenSuse 13.1 comes with python by default,
                                          recommended python version is 2.7xx
'''

import os
import sys
import subprocess as s

_version = 0.1


PKGMAN = 'zypper'
SUPERU = 'sudo'
DEBUG = True  #using this for debuging purpose
#DEBUG = False
INSTALL = 'in' 
PIP = 'pip'
zypTpl = ('python-pip','uwsgi','uwsgi-python','nginx') #list of programs zypper will install
pipTpl = ('bottle','uwsgi') # list of python modules pip will install


#open devnull and redirect all output there
if not DEBUG:
   redout = open('/dev/null','w')
else:
   redout = sys.stdout
   SUPERU = 'sudo'
   rederr = open('error.log','w')

def check_install(returncode):
   #check regex, see what i have to find out
   print returncode
#start updating with zypper 
def zyp_install():
   for module in zypTpl:
        print 'Using zypper to install', str(module)
        try:
           returncode = s.Popen([SUPERU, PKGMAN,INSTALL ,module],stderr=s.PIPE,stdout=s.PIPE).communicate()
           check_install(returncode)
        except OSError:
           print "There was an error installing",module, sys.stderr
   rederr.close()

def main():
    if not DEBUG and os.getuid() != 0:
        exit("You don't have the necessary access privileges, try running this with sudo")
    else:
         zypinstall()
    

if __name__=='__main__':
    main()
