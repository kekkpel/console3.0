import os
import sys
import subprocess as sub

def main_ssh(self, mode_ip):
    sub.run(['ssh',mode_ip])

#main_ssh('w','root@192.168.1.116')
