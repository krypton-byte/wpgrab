#Made with love by Krypton-Byte
#https://github.com/krypton-byte
import os
import re
import threading
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore								
from colorama import Style								
from colorama import init												
init(autoreset=True)
fr  =   Fore.RED
fc  =   Fore.CYAN
fm  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fb  =   Fore.BLUE
fg  =   Fore.GREEN											
fre =   Fore.RESET
sd  =   Style.DIM
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
version=lambda sc:re.search('WordPress (.*?)\"',sc)[1] if re.search('WordPress (.*?)\"',sc) else m+"Unknown"
themes=lambda sc:re.findall('wp-content\/themes\/(.*?)\/',sc)[1] if re.findall('wp-content\/themes\/(.*?)\/',sc) else m+"Unknown" 
plugins=lambda sc:list(set(re.findall('wp-content\/plugins\/(.*?)\/',sc))) if re.findall('wp-content\/plugins\/(.*?)\/',sc) else []
author=lambda url:re.search('/author/(.*?)/', url)[1] if re.search('/author/(.*?)/', url) else m+"Unknown"

p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

def banner():
	return '''
%s%s __          __   %s  _____           _     
%s%s \ \        / /   %s / ____|         | |    
%s%s  \ \  /\  / / __ %s| |  __ _ __ __ _| |__  
%s%s   \ \/  \/ / '_ \%s| | |_ | '__/ _` | '_ \ 
%s%s    \  /\  /| |_) %s| |__| | | | (_| | |_) |
%s%s     \/  \/ | .__/%s \_____|_|  \__,_|_.__/ 
%s%s            | |   %s  %sV1.0 %sby %sKrypton-Byte         
%s%s            |_|   %s  
''' % (fc,sb,fw,fc,sb,fw,fc,sb,fw,fc,sb,fw,fc,sb,fw,fc,sb,fw,fc,sb,fw,fg,fr,fc,fc,sb,fw)

def owhkey(url):
    req=requests.get(url,params={"author":1})
    plugin="- "+"\n\t\t - ".join(plugins(req.text))
    print(f"""\t
\t%sURL    %s: %s{url}
\t%sAuthor %s: %s{author(req.url)}
\t%sThemes %s: %s{themes(req.text)}
\t%sPlugins%s: %s{plugin}
\t%sVersion%s: %s{version(req.text)}
    """ % (fm,fr,fg,fm,fr,fg,fm,fr,fg,fm,fr,fg,fm,fr,fg,))
def main():
    while True:
        print(banner())
        print("""
\t%s%s[%s1%s] %sSingle
\t%s%s[%s2%s] %sMultiple
        """ % (sb,fc,fy,fc,fg,sb,fc,fy,fc,fg))
        inp=input(u+'\t   •'+m+'▶ '+h)
        if inp in ["1","01"]:
            url=input(u+'       URL •'+m+'▶ '+h)
            threading.Thread(target=owhkey, args=(url,)).start()
            break
        elif inp in ["2", "02"]:
            file=input(u+'      File •'+m+'▶ '+h)
            work=input(u+'   Threads •'+m+'▶ '+h)
            if file in os.listdir('.'):
                with ThreadPoolExecutor(max_workers=int(work) if work.isnumeric() else 5) as th:
                    for i in list(set(open(file,"r").read().splitlines()) ^ {''}):
                        th.submit(owhkey, i)
            else:
                print(m+"\t["+k+"+"+m+"]"+bm+" File Tidak Di Temukan "+m+"["+k+"+"+m+"]")
            break
if __name__ == '__main__':
    main()
