try:import random,re,threading;from colorama import Fore;from requests import get,post
except ModuleNotFoundError:exit('[!] Download The Missing Module !')

	
class Lightning:
    

    def __init__(self,ThreadER,length):
        self.ThreadER=ThreadER
        self.length=length
    

    def Lightning_Saver(self,user):
        ID=''#Telegram ID
        token=''#Telegram Bot Token
        try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=• New username’s Claimed @{user} 🦦\n\nBy\t@TweakPY\t-\t@vv1ck')
        except:pass
        with open('Lightning_Available.txt', 'a') as x:
            x.write(user+'\n')
    

    def Lightning_User_Maker(self):
        user=""
        chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
        for user in range(1):
            user=""
            for item in range(length):
                user+=random.choice(chars)	
        return user
    
    
    def Lightning_N(self):
        try:
            while True:
                user=self.Lightning_User_Maker()
                ru=get(f"https://tokcount.com/?user={user}",headers={'Host': 'tokcount.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Cache-Control': 'max-age=0','Te': 'trailers'})				
                if 'undefined' in re.findall('<title>(.*?)</title>',ru.text)[0]:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available {Fore.RESET} : {user} ')
                    self.Lightning_Saver(user)
                elif 'false' in re.findall('"success":(.*?),',ru.text)[0]:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available {Fore.RESET} : {user} ')
                    self.Lightning_Saver(user)
                elif 'true' in re.findall('"success":(.*?),',ru.text)[0]:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} ')			
                else:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} ')	
        except Exception as i:
            #raise UserWarning(f'Error Found : {i}')
            pass
    
    
    def Lightning_starter(self):
        for Lightning in range(int(self.ThreadER)):
            threading.Thread(target=self.Lightning_N).start()
	

print(f"""
88888888888 8888888 888    d8P        888      d8b          888      888             d8b                   
    888       888   888   d8P         888      Y8P          888      888             Y8P                   
    888       888   888  d8P          888                   888      888                                   
    888       888   888d88K           888      888  .d88b.  88888b.  888888 88888b.  888 88888b.   .d88b.  
    888       888   8888888b          888      888 d88P"88b 888 "88b 888    888 "88b 888 888 "88b d88P"88b 
    888       888   888  Y88b  888888 888      888 888  888 888  888 888    888  888 888 888  888 888  888 
    888       888   888   Y88b        888      888 Y88b 888 888  888 Y88b.  888  888 888 888  888 Y88b 888 
    888     8888888 888    Y88b       88888888 888  "Y88888 888  888  "Y888 888  888 888 888  888  "Y88888 
                                                        888                                            888 
                                                   Y8b d88P                                       Y8b d88P 
    By @TweakPY - @vv1ck                            "Y88P"                                         "Y88P"  
{Fore.LIGHTRED_EX}01010100 01001001 01001011 00101101 01001100 01101001 01100111 01101000 01110100 01101110 01101001 01101110 01100111{Fore.RESET}
""")		
ThreadER=int(input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] Thread  [{Fore.LIGHTRED_EX}50-100{Fore.RESET}]: '))
length=int(input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] User Length: '))


Lightning(ThreadER,length).Lightning_starter()
