try:import random,os,re,threading;from colorama import Fore;from requests import get,post
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()


class Lightning:
    

    def __init__(self,ThreadER,length,sis):
        self.ThreadER=ThreadER
        self.length=length
        self.sis=sis


    def Lightning_updater(self):
        try:
            filename=os.path.basename(__file__)
            if filename!='Tik-Lightning.py':exit(f'[!] Error "{filename}" is not in database please rename it to original name : "Tik-Lightning.py" ...')
            updater=get('https://raw.githubusercontent.com/Filza2/TIK-Lightning/main/Tik-Lightning.py').text
            if os.path.exists('U-Tik-Lightning.py')==False:file=open('U-Tik-Lightning.py','a');file.write(updater);file.close();exit('[!] Tool is old .. New update Has been downloaded in "U-Tik-Lightning.py" ')
            elif os.path.exists('U-Tik-Lightning.py')==True:file=open('U2-Tik-Lightning.py','a');file.write(updater);file.close();exit('[!] Tool is old .. New update Has been downloaded in "U2-Tik-Lightning.py" ')
            else:exit('[!] Error Downlaoding The Update , Delete the old tools !!')
        except Exception as i:print('[!] Error in the automatic updater , You must download it manually !!');exit('[!] Your Tool is old and need for update , update it from here "https://github.com/Filza2/TIK-Lightning" ..')


    def Lightning_Saver(self,user):
        ID=''#Telegram ID
        token=''#Telegram Bot Token
        try:
            urlsaver=f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=• New username’s Claimed @{user} 🦦\n\nBy\t@TweakPY\t-\t@vv1ck'
            if '@TweakPY\t-\t@vv1ck' not in urlsaver:user='@TweakPY\t-\t@vv1ck 🦦';urlsaver=f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text='+user
            post(urlsaver)    
        except:pass
        with open('Lightning_Available.txt', 'a') as x:
            x.write(user+'\n')


    def Lightning_User_Maker(self):
        chars="qw_ertyuiopa.123456789.0sdfghjkl_z.xc_vbn_mqwer.t_yuiopasd0123466.559856_fghjkl.zxcvbnmqwert000.yuio_pasdf.ghjklzxc.vbnmqw.ertyuiopasd_fghj.klzx.cvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890.";user=""
        for user in range(1):
            user=""
            for item in range(length):
                user+=random.choice(chars)	
        if user.endswith('.'):
            return self.Lightning_User_Maker()
        else:
            return user
    
    
    def Lightning_N(self):
        try:
            while True:
                user=self.Lightning_User_Maker()
                ru=get(f"https://tokcount.com/?user={user}",headers={'Host': 'tokcount.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Cache-Control': 'max-age=0','Te': 'trailers'})				
                if 'error' in re.findall('<title>(.*?)</title>',ru.text)[0]:
                    self.Lightning_N2(user)
                elif re.findall(',"id":"(.*?)"',ru.text)[0] in ru.text:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} ')			
                else:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} ')	
        except Exception as i:
            #raise UserWarning(f'Error Found : {i}')
            pass


    def Lightning_N2(self,user):
        try:
            dv="";dv2="102132435465768798090"
            for dv in range(1):
                dv=""
                for item in range(4):
                    dv+=random.choice(dv2)	
            device_id=dv
            while True:
                r1=get(f'https://www.tiktok.com/api/uniqueid/check/?aid=1988&app_language=en&device_id={device_id}424033622476290&unique_id={user}',headers={'Host': 'www.tiktok.com','Cookie': f'sessionid={sis}','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'})
                #print(r1.text)	
                if 'Login expired' in r1.text:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Login Expired {Fore.RESET} : {user} ')	
                elif 'This username isn’t available. Try a suggested username, or enter a new one.' in r1.text:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} - {Fore.LIGHTRED_EX}{str(r1.json()["is_valid"])}{Fore.RESET}')	
                elif '{}' in r1.text:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Ban {Fore.RESET} : {user} ')
                elif 'True' in str(r1.json()["is_valid"]):
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available {Fore.RESET} : {user} - {Fore.GREEN}{str(r1.json()["is_valid"])}{Fore.RESET}')
                    self.Lightning_Saver(user)
                else:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} - {Fore.LIGHTRED_EX}{str(r1.json()["is_valid"])}{Fore.RESET}')	
        except:pass
    

    def Lightning_starter(self):
        for Lightning in range(int(self.ThreadER)):
            threading.Thread(target=self.Lightning_N).start()
	

print(f"""
████████╗██╗██╗  ██╗     ██╗     ██╗ ██████╗ ██╗  ██╗████████╗   
╚══██╔══╝██║██║ ██╔╝     ██║     ██║██╔════╝ ██║  ██║╚══██╔══╝   
   ██║   ██║█████╔╝█████╗██║     ██║██║  ███╗███████║   ██║      
   ██║   ██║██╔═██╗╚════╝██║     ██║██║   ██║██╔══██║   ██║      
   ██║   ██║██║  ██╗     ███████╗██║╚██████╔╝██║  ██║   ██║ {Fore.LIGHTRED_EX}██╗ ██╗{Fore.RESET}
   ╚═╝   ╚═╝╚═╝  ╚═╝     ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝ {Fore.LIGHTRED_EX}╚═╝ ╚═╝{Fore.RESET}
                                                                                                      
                 By @TweakPY - @vv1ck                                                                 
""")		
update='2.3'
try:
    s=get("https://raw.githubusercontent.com/Filza2/TIK-Lightning/main/update.txt").text
    if update in s:pass
    else:Lightning('Error','Update','Proplem').Lightning_updater()
    ThreadER=int(input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] Thread  [{Fore.LIGHTRED_EX}50-900{Fore.RESET}]: '))# Phone : [10-70]    ||    Computer : [100-900]
    length=int(input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] User Length: '))
    sis=input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] session id : ')
except Exception as i:print(f'Error Found : {i}');exit()


Lightning(ThreadER,length,sis).Lightning_starter()
