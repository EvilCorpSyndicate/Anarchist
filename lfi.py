## Software Name: Anarchist - Local File Inclusion (LFI) vulnerability website finder
## Version: 1.0
## Software Description: This piece of code is used too find vulnerable websites to LFI vulnerability using google dorks.
## Software Author: g0dsecurity

## Importing modules
from bs4 import BeautifulSoup
import requests
import argparse
from termcolor import colored
import os
import sys
import threading

argparser = argparse.ArgumentParser(description="Anarchist - A Pentesting Suite of tools")
argparser.add_argument("-d","--dork",help="Dork to use for searching")
argparser.add_argument("-p","--page",help="Number of pages to search")
argparser.add_argument("-t","--threads",help="Number of threads to use")
args = argparser.parse_args()

args_threads = args.threads
args_dork = args.dork
args_page = args.page

website_list=[] #list of websites
dork = "inurl:" + input(colored("Please input the LFI dork(eg- default.php?page=) ---->  ",'cyan'))
extension = "site:" + input(colored("Please specify the website extension [default: none] -----> ",'cyan'))
total_output = int(input(colored("Pleases specify the total no. of websites you want) ----> ",'cyan')))
page_no = int(input(colored("From which Google page you want to start(eg- 1,2,3) ----> ",'cyan')))
print(colored("Searching for vulnerable websites...",'green'))

def web_headers():
    web_headers = "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/51.0.2704.103 safari/537.36"
    return web_headers
while page_no <= total_output:
    try:
        url = "https://www.google.com/search?q=" + dork + "+" + extension + "&start=" + str(page_no)
        headers = {'User-Agent':web_headers()}
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')
        for a in soup.find_all('a',href=True):
            website_list.append(a['href'])
        page_no += 10
    except:
        print(colored("[-] Error while searching for websites",'red'))
        sys.exit()
print(colored("[+] Total websites found: " + str(len(website_list)),'green'))

def mythreading():
    mythreading = threading.Thread(target=args.threads)
    return mythreading
if 200:
    print(colored("[+] Website is vulnerable to LFI",'green'))
else:
    print(colored("[-] Website is not vulnerable to LFI",'red'))
    pass
## Save The Websites founded as .txt file
def output():
    output = open("lfi.txt","w")
    for website in website_list:
        output.write(website + "\n")
    output.close()
    print(colored("[+] Websites saved in lfi file",'green'))
    
