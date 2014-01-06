#!/usr/bin/env python 

#Done by: Victor
#latest update github.com/codeflavour/susebottle


'''
                                          Deploy Bottle web framework on OpenSuse 13.xx
                                          Uses pip, nginx, uwsgi, uwsgi-python 
                                          OpenSuse 13.xx comes with python by default,
                                          otherwise recommended python version is 2.7xx
'''

import os
import sys
import subprocess as s
import re
_version = 0.1


PKGMAN = 'zypper'
SUPERU = 'sudo'
DEBUG = True  #using this for debuging purpose
INSTALL = 'install' 
PIP = 'pip'
AUTOZYP = '-n'
AUTOPIP = 'YES'
BAR = '|'
PIPUP = '--upgrade'
zypTpl = ('python-pip','uwsgi-python','nginx') #list of programs zypper will install
pipTpl = ('bottle','uwsgi') # list of python modules pip will install


#open devnull and redirect all output there
if DEBUG:
   SUPERU = 'sudo'
   
def check_zyp(returncode):
   returncode = str(''.join(returncode))
   if re.search('is already installed',returncode,re.I):
       print '[>>>Already installed]'
       return
   if re.search('NEW package',returncode,re.I):
       print '[>>>Installed]'
   if re.search('is locked by',returncode,re.I):
       exit("Can't spawn new zypper process, app is locked")
   
#start updating with zypper 
def zyp_install():
   for zyppkg in zypTpl:
       print 'Using zypper to install', zyppkg
       try:
          check_zyp(s.Popen([SUPERU, PKGMAN ,AUTOZYP ,INSTALL ,zyppkg],stderr=s.PIPE,stdout=s.PIPE).communicate())
       except OSError:
          print "There was an error installing",zyppkg,": --", sys.stderr
   

def check_pip(pipop):
   pipop = str(''.join(pipop))
   if re.search('already satisfied',pipop,re.I):
      print '[>>> Already installed]'
   if re.search('Successfully installed',pipop,re.I):
      print '[>>>Installed]'
      return
   if re.search('Downloading',pipop,re.I):
      print 'got here as well'

#install python modules with pip
def pip_install():
    for pipmod in pipTpl:
       print 'Using pip to install', pipmod
       try:
          yescmd= s.Popen('yes',stdout=s.PIPE)
          check_pip(s.Popen([SUPERU,PIP, INSTALL,pipmod],stdin=yescmd.stdout,stderr=s.PIPE,stdout=s.PIPE).communicate())
       except OSError:
          print "There was an error installing python-module", pipmod

def main():
    if not DEBUG and os.getuid() != 0:
        exit("You don't have the necessary access privileges, try running this with sudo")
    else:
         zyp_install()
         pip_install()

if __name__=='__main__':
     main()
