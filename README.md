# SMS-SBAM-DF


# Spam SMS Tool

A Python-based tool to send multiple SMS messages using an external API with random proxy and User-Agent support.

---

## Developer

- **Dev**: [@A_Y_TR](https://t.me/A_Y_TR)
- **Telegram Channel**: [CybersecurityTemDF](https://t.me/cybersecurityTemDF)

---

## Features

- Interactive CLI interface with PyFiglet ASCII art
- Proxy rotation to bypass rate limits
- User-Agent randomization for stealth
- Count success/failure for each request
- Delay between requests for anti-block
- Sends data via TwistMENA login API

---

## Requirements

- Python 3.7 or newer
- The following Python libraries:
  - `requests`
  - `pyfiglet`
  - `termcolor`

---

## Installation Instructions

### For Termux (Android):

```bash
pkg update && pkg upgrade
pkg install python git
pkg install python3
pip install requests pyfiglet termcolor
git clone https://github.com/MohamedAbuAl-Saud/SMS-SBAM-DF/
cd SBAM-SMS-DF
pip install -r requirements.txt
python3 sms.py
```

For Kali Linux / Debian:
```
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip git -y
pip3 install requests pyfiglet termcolor
git clone https://github.com/MohamedAbuAl-Saud/SMS-SBAM-DF/
cd SBAM-SMS-DF
pip install -r requirements.txt
python3 sms.py
```

For Windows:

1. Install Python from https://python.org


2. Open Command Prompt or PowerShell.


3. Run the following:


```
pip install requests pyfiglet termcolor
git clone https://github.com/MohamedAbuAl-Saud/SMS-SBAM-DF/
cd SBAM-SMS-DF
pip install -r requirements.txt
python3 sms.py
```

---
#For automatic installation 
```
pip install -r requirements.txt
```
How to Use

1. Run the tool:



python sms.py

2. Input the target phone number (without country code — it auto-adds +20).


3. Input the number of messages you want to send.




---

Example Output

Enter Your Number: 1001234567
Enter number of messages: 5
============================
SUCCESS: 200
SUCCESS: 200
Request failed: Timeout
...
Total successful requests: 4
Total failed requests: 1


---

Legal Disclaimer

This tool is made for educational purposes only. Any illegal usage is not the responsibility of the developer. By using this tool, you agree that you're solely responsible for your actions.


---

Credits

Created with passion by آلقيـــــــــــــــآدهہ‌‏ آلزعيـــم a.k.a @A_Y_TR

---


