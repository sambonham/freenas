#!/usr/local/bin/python

import subprocess

version_running = subprocess.check_output(['cat','/etc/version'])
version_running = version_running.rstrip('\n')
version_string = version_running.split('-')[0]
version_number = version_running.split('-')[-1]
boot_env = version_string+'-'+version_string+'-'+version_number
try:
    subprocess.check_output(['beadm','rename',boot_env,version_running])
except:
    print "boot enviorment {0} does not exists".format(boot_env)
        
