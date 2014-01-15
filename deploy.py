#!/usr/bin/env python 

#Done by: Victor
#latest update github.com/codeflavour/susebottle

'''
                                          Deploy Bottle web framework on OpenSuse 13.xx
                                          Uses pip, nginx, uwsgi, uwsgi-python 
                                          OpenSuse 13.xx comes with python by default,
                                          otherwise recommended python version is 2.7xx
                                          Adds to nginx vhost file, and to uWsgi bottle.ini
                                          config file, sets uWsgi(emperor) as a service,
                                          adds it to startup
'''

import os
import sys
import subprocess as s
import re

_version = 0.1
PKGMAN = 'zypper'
SUPERU = 'sudo'
DEBUG = True
#DEBUG = False
INSTALL = 'install' 
PIP = 'pip'
AUTOZYP = '-n'
#PIPUP = '--upgrade'
zypTpl = ('python-pip','uWsgi','uwsgi-python','nginx') #list of programs zypper will install
pipTpl = ('bottle',) # list of python modules pip will install
dirsTpl = ('/etc/nginx/sites-enabled','/etc/nginx/sites-available','/etc/uwsgi','/run/sockets')

if DEBUG: SUPERU = 'sudo'

def check_dir():
   for path in dirsTpl:
       if not os.path.exists(path):
          print "Directory", path, "missing, creating it!"
          try : 
                os.makedirs(path)
          except OSError as e:
                exit("Can't create directory %s , Error: %s" % (path, e))
   

def check_install(returncode):
   psat = re.compile(r'already installed|satisfied',re.I)
   pinst = re.compile(r'new package|successfully installed',re.I)
 #  if DEBUG:  print ('\n').join(returncode)    #patfail = re.compile(r'(\\)|(\\)')
   for line in returncode:
       if re.search(psat,line):
            print "[Skipping]"
       if re.search(pinst,line):
            print "[Done]"
       if re.search("connection failed",line,re.I):
            exit(">>> No internet connection")
       if re.search("is locked by",line,re.I):
            exit(">>> Can\'t spawn zypper, process busy")
   
#start updating with zypper 
def zyp_install():
   print "Using Zypper to install package: "
   for zyppkg in zypTpl:
       print zyppkg
       try:
          check_install(s.Popen([SUPERU, PKGMAN ,AUTOZYP ,INSTALL ,zyppkg],stderr=s.PIPE,stdout=s.PIPE).communicate())
       except OSError as e:
          print "Error installing",zyppkg,": --", e
   
#install python modules with pip
def pip_install():
    for pipmod in pipTpl:
       print "Using pip to install", pipmod
       try:
         check_install(s.Popen([SUPERU, PIP, INSTALL,pipmod],stderr=s.PIPE,stdout=s.PIPE).communicate())
       except OSError as e: 
          print "Error installing python-module", pipmod, e

def main():
    if not DEBUG and os.getuid() != 0:
        exit("You don't have the necessary permissions,  try running this with sudo")
    else:
         if DEBUG : 
            check_dir()
         else:
            zyp_install()
            pip_install()

if __name__=='__main__':
     main()
