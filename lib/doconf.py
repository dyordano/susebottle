#!/usr/bin/env python


'''
         writes config files to current environment
         this is a good way to start using classes
         and get a level up
         Experimental for now. i also know i don't
         need a class, but using this anyway for now
         to learn
'''


class WriteConfig:
    'Write config file based on what is served'

 
    def __init__(self, path, filename):
        print path


    def commit_nginx(self):
    ''' nginx config file, if it got here, it means that the directory was created
        need to push config to /etc/nginx/sites-available, and do symlink to 
        /etc/nginx/sites-enabled, also must modify nginx.conf with
       ` include /etc/nginx/sites-available`
        need to have the config written somewhere, either as a tuple or something else
      '''
       
