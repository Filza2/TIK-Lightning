try:import random,re,threading;from colorama import Fore;from requests import get,post
except ModuleNotFoundError:exit('[!] Download The Missing Module !')

class Lightning:
    

    def __init__(self,ThreadER,length,sis):
        self.ThreadER=ThreadER
        self.length=length
        self.sis=sis
    

    def Lightning_Saver(self,user):
        ID=''#Telegram ID
        token=''#Telegram Bot Token
        try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=[✅]\t\tNew\tuser\t:\t{user}\n\n[🔍]\t\t@TweakPY\t-\t@vv1ck')
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
                    self.Lightning_N2(user)
                elif 'false' in re.findall('"success":(.*?),',ru.text)[0]:
                    self.Lightning_N2(user)
                elif 'true' in re.findall('"success":(.*?),',ru.text)[0]:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} ')			
                else:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} ')	
        except Exception as i:
            #raise UserWarning(f'Error Found : {i}')
            pass


    def Lightning_N2(self,user):
        try:
            while True:
                r1=get(f'https://www.tiktok.com/api/uniqueid/check/?aid=1988&app_language=en&app_name=tiktok_web&browser_language=en&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%29&channel=tiktok_web&cookie_enabled=true&device_id=7122424033622476290&device_platform=web_pc&focus_state=true&from_page=user&history_len=5&is_fullscreen=false&is_page_visible=true&os=linux&priority_region=SA&referer=https%3A%2F%2Fwww.tiktok.com%2F%40onlliiyy&region=SA&root_referer=https%3A%2F%2Fwww.tiktok.com%2F%40onlliiyy&screen_height=768&screen_width=1366&tz_name=Asia%2FRiyadh&unique_id={user}&verifyFp=verify_l7indiyn_v8eav1JO_pySN_4jFL_9R8I_V8IJm5kmpCLB&webcast_language=ar&msToken=YOzHUFI5nCylxN7YW0skxqGdJSOPVgKhwk7MxUFbxxqlc50ZUHO-oL1LDXsSO0jCpJeNfKJQuSTQWwvyKgBwPSczaxZwrB3HTZ6h8ETbMPTsaAh8ZQgHHJRG-xzt5lq97H8G&X-Bogus=DFSzsIjLkjsANxYXSQwQXsybrUR7&_signature=_02B4Z6wo000018ro4uAAAIDCyAx3SZrGZFPK6e5AAJGz70',headers={'Host': 'www.tiktok.com','Cookie': f'ttwid=1%7Cf1d9mI-3uCgb1W1ykT_ZvVGVVmxnggmGJ2TkBooEM1k%7C1662012995%7C30ebc2e41b988fbe839dd0f5db1e1e53bddf1c5ce12ace799946882afc1f0ca3; _abck=22E1C240F157DDF6067B25DFB9B821C1~-1~YAAQ3jNWskyO8PaCAQAAUlYg9wixQovCo/eVENMQPvodoAQtqJ2sJNBcs9S+IH2m8z+FLvNQXZmk3ep/4p/hm761SyNJ3jlKEK5Gi0fEGDR48PhYwh22FgDTrxM3W3mmgQQP7SHYZNQqrde6N1zYfToC7FMqD2a7Iq5KgPhtHPO7YI6kNJ6fH5qrTiuVoP10obxBgBOpIi40BwPodghfPF6GjS7J8A+ZyOae66YON9FD68ye09O9ZWx5AoNJPm5HPKyRCIH/+pKkz/jYozus92dZvaVjTD0zL/y+sY8bJgxTK4H586YKGBKGr9VAz5w1NLyxbmZPtkRfCcAdd+gIarFozaGxaImvKHuWouj8aQ+3yrWU9iIiQ3/Bw6VvbBAQs27m39RBXKrDEg==~-1~-1~-1; __tea_cache_tokens_1988='+str('{%22user_unique_id%22:%227122424033622476290%22%2C%22timestamp%22:1662003420532%2C%22_type_%22:%22default%22}')+f'; msToken=YOzHUFI5nCylxN7YW0skxqGdJSOPVgKhwk7MxUFbxxqlc50ZUHO-oL1LDXsSO0jCpJeNfKJQuSTQWwvyKgBwPSczaxZwrB3HTZ6h8ETbMPTsaAh8ZQgHHJRG-xzt5lq97H8G; passport_csrf_token=13ece5f7e525190b87f121f3036fc2fa; passport_csrf_token_default=13ece5f7e525190b87f121f3036fc2fa; odin_tt=9cd65446c1cae84acda1abb8ed8d966e484b817811a3ab8dd6c2b9e0ca75f62433291b8f67f2d348b6b98844eaf9bca919f8e97c183dc881a509d636fd841244dd5a316e9cb1289e5b7fe43277de437d; cmpl_token=AgQQAPO_F-RMpbM0c6QIM104-LZ337Ba_4A0YMUzrQ; sid_guard={sis}%7C1661640060%7C5184000%7CWed%2C+26-Oct-2022+22%3A41%3A00+GMT; uid_tt=45ac0a8230548d27c192f810cca59123e7516d2cb30dfe412bf79aa3373a7b35; uid_tt_ss=45ac0a8230548d27c192f810cca59123e7516d2cb30dfe412bf79aa3373a7b35; sid_tt={sis}; sessionid={sis}; sessionid_ss={sis}; sid_ucp_v1=1.0.0-KGQ5NTE4NmVjOTNmODFiNGRkOTc2MGMxYTVlOGI2ZWFlMGI2ZDQ2MjAKIAiBiIaAuKCnhWMQ_LqqmAYYswsgDDCuuqqYBjgEQOoHEAMaBm1hbGl2YSIgM2E4OWZjMDVmZmE5ZWIwMDE0NTU3ODM4ZTcwODE4ZTI; ssid_ucp_v1=1.0.0-KGQ5NTE4NmVjOTNmODFiNGRkOTc2MGMxYTVlOGI2ZWFlMGI2ZDQ2MjAKIAiBiIaAuKCnhWMQ_LqqmAYYswsgDDCuuqqYBjgEQOoHEAMaBm1hbGl2YSIgM2E4OWZjMDVmZmE5ZWIwMDE0NTU3ODM4ZTcwODE4ZTI; store-idc=alisg; store-country-code=sa; store-country-code-src=uid; tt-target-idc=alisg; bm_sz=1D20E6A1D75F369AD11925677BF94733~YAAQ3jNWsk2O8PaCAQAAUlYg9xAbvBUA47skfPKkTLVxGbWagVojW0VdJl6x2MEcq7Wj5Mgq6RtEHNMjlEpL3S7MGaMAuDR1szj11ztFzW/JttqUNnAbFLPeA05uqYg+5V5xHMGpKUJQps+LPmVLjfIF2aqjC+o/mSHoKWboOwtZliUXtcz6HwGv4SoeY7IJ0SyNcMxLUECUwJU2yACJNSlmYKYdmDU/mk8GGmhjuMgswRWn3tvTfIW1vN6ckM54DhTIISO7Y6Lr4Kc0FqzaLCQxqgU4can4M5ZdolFKMno9NX0=~4534853~3229238; __tea_cookie_tokens_1988=%257B%2522web_id%2522%253A%2522%2522%252C%2522timestamp%2522%253A1662003420532%257D; tt_csrf_token=zSh4R6c2-4O8nFbFgNzfPYu1ac964oxvIuOc; passport_fe_beating_status=true; ak_bmsc=B82981C1656559B29883D5BBF973F35E~000000000000000000000000000000~YAAQdjNWsndV2u6CAQAA2E6r9xAGl8snvrTvuLFQ/26L3PCSMu12R2SpEaf5kVoDdruu8YMkS7Jlhzg3srtfvtgJrtCgplHouuYurc1rogCDS4b/NK0jX+KnMNJUbZ36QeC9RBZdu5WyHQ6oKzXV1/JTZpPqxhkJcNZs2pFZlEwT2EjCYTllBQ+5mDgO0rX7c8ar3n6M9K2s6Ojk9OxONx1gRiaE2NuWk9jXgm0ys9qzKnNzGDZ/CBkjndc2r4cgvIy+bLL9b8fTiEH9h56bA12IFIlZBWTCo8RL4CewXwJp8LfHPsiuJ3NsioohBxTrDHKLulDDe1OkVAvFpzBNuUWWFuDYupVXgEwZp90l9X8tCVoHrGcOI6sVDVNsHlFfz92gF7R1WXw=; bm_sv=CD7EC3FEB08139B40BC103D8994F8D07~YAAQJjNWsneC6PaCAQAAck6y9xAKZmJk+QTuK7Ih80ZH3w/LmmkSlxOML0+yD0ifvkk1VhLfJhGNrZDhTsY3cCIfWrA5sA8WKig3MuieJ6PVOoB2jW8jjZFuNiR5p82B8cK7Y3qqqTwvP3F9ECcnfYhDPV2Sz3ZiLtGNmCdzVfdHETTy+OBNXrepx1S8RTyCFhLgvN6/8lDhwWIhS0KGK5C1PYXUbmRqViZQtdpftwIwaHSfZPe4fF179hntjZhN~1; s_v_web_id=verify_l7indiyn_v8eav1JO_pySN_4jFL_9R8I_V8IJm5kmpCLB; bm_mi=F6B8D571CF7AFB18F5579D3DC65F31FA~YAAQJjNWskiC6PaCAQAAmq2x9xCgHDJITqR0AsdEEZ9HKEKm9mhiyfoRpapEKOG524J6xQoMXNM8MspomOluJOgM5huKFbvsGcfE+JpTB6X8+7XqBFE9vMtNgFTm1PiI03JZKHbYLhaQ2x+0vVorPLjeT5yrJUe5lFg8BqrDLPbabL3NabwTJ2m7zFaJUymBzfSNZg+CIA2shBy4omePwnRg6JPye8AB6D3puNFGyfef0NTcSclnq5jgXC1NjSSrnbfoswRmE5JMB15oSa8ChbGCM5C5C17pJe53K34kP3qOAMkCdYNK2ouDnSt++uYmzVbp~1; msToken=G_rlzt2ThZxLRknhtXqbZehlenTeS89Et4hkE3H9IrlA-W_7SydwWfyd5hDorw9H8sfIc1o6GW4xjnynuCBn87dkLcWDdJAbf4m6JGKUCnOCmV_I9grjlExUkXMVtjbUFgzS','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Tt-Csrf-Token': 'zSh4R6c2-4O8nFbFgNzfPYu1ac964oxvIuOc','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Referer': f'https://www.tiktok.com/@{user}','Te': 'trailers'})
                if 'Login expired' in r1.text:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Login Expired {Fore.RESET} : {user} ')	
                elif 'True' in str(r1.json()["is_valid"]):
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available {Fore.RESET} : {user} - {Fore.GREEN}{str(r1.json()["is_valid"])}{Fore.RESET}')
                    self.Lightning_Saver(user)
                elif 'This username isn’t available. Try a suggested username, or enter a new one.' in r1.text:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} - {Fore.LIGHTRED_EX}{str(r1.json()["is_valid"])}{Fore.RESET}')	
                else:
                    print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.LIGHTRED_EX} Not Available {Fore.RESET} : {user} - {Fore.LIGHTRED_EX}{str(r1.json()["is_valid"])}{Fore.RESET}')	
        except:pass
    

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
sis=input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] session id : ')


Lightning(ThreadER,length,sis).Lightning_starter()
