import random, string, os
import requests, httpx, time
from colorama import Fore, init

# PUT YOUR CAPTCHA KEY HERE
global captchakey
captchakey = 'CAPTCHA KEY IN HERE 2CAP'

init()

def useragent():
    file = open('useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

    for element in useragent2:
        useragent1.append(element.strip())
    finaluseragent = ''.join(str(e) for e in useragent1)
    return finaluseragent

def name():
    names = []
    name = []
    with open('names.txt','r') as username:
        for line in username:
            names.append(line)
        for element in names:
            name.append(element.strip())

    return random.choice(name)

def proxy():
    proxies = []
    proxy1 = []
    with open('proxies.txt','r') as proxi:
        for line in proxi:
            proxies.append(line)

        for element in proxies:
            proxy1.append(element.strip())

    return random.choice(proxy1)

def dob():
    dateofbirth = str(random.randint(1990, 2002))+'-'+'{:02d}'.format(random.randint(1,12))+'-'+'{:02d}'.format(random.randint(1,28))
    return dateofbirth

def password():
    chars = string.ascii_letters + string.digits
    upcase = random.choice(string.ascii_uppercase)
    password1 = upcase + ''.join(random.choice(chars)for x in range(11))

    return password1

def main(amout):
    for x in range(amout):
        username = name()
        passwod = password()
        userage = useragent()

        cookiemonster = httpx.get('https://discord.com/register').headers['set-cookie']
        sep = cookiemonster.split(";")
        sx = sep[0]
        sx2 = sx.split("=")
        dfc = sx2[1]
        split = sep[6]
        split2 = split.split(",")
        split3 = split2[1]
        split4 = split3.split("=")
        sdc = split4[1]
        print(f'{Fore.GREEN}Got Cookie!')

        while __name__ == '__main__':
            fingerprints = httpx.get("https://discord.com/api/v9/experiments",timeout=10)
            if fingerprints.text == '':
                pass
            else:
                realfingerprint = fingerprints.json()['fingerprint']
                print(f'{Fore.GREEN}Got Fingerprints!')
                break

        header = {
            "Host": "discord.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
            "X-Fingerprint": realfingerprint,
            "Accept-Language": "en-US",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": userage,
            "Content-Type": "application/json",
            "Authorization": "undefined",
            "Accept": "*/*",
            "Origin": "https://discord.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://discord.com/register",
            "X-Debug-Options": "bugReporterEnabled",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}"
        }
        print(f'{Fore.GREEN}Got User-Agent!')

        captchadata = {
            'User-Agent':userage
        }

        print(f'{Fore.GREEN}Solving Captcha...')
        captchaurl = f'http://2captcha.com/in.php?key={captchakey}&method=hcaptcha&sitekey=f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34&pageurl=http://discord.com/register'
        captcharequests = requests.post(captchaurl, data=captchadata, json=1)

        captchares = (captcharequests.text)
        x = captchares.split('|')
        id = x[1]
        time.sleep(15)

        while True:
            resurl = requests.get(f'http://2captcha.com/res.php?key={captchakey}&action=get&id={id}')
            if resurl.text == "CAPCHA_NOT_READY":
                pass
            else:
                break

        captoken = resurl.text
        final, captchatoken = captoken.split('|')

        if captcharequests.text == 'ERROR_ZERO_BALANCE':
            print(f'{Fore.RED}Error: You do not have any balance!')

        print(f'{Fore.GREEN}Got Captcha Token!')
        print(f'{Fore.GREEN}Registering Account...')

        domainlist = ['@gmail.com','@yahoo.com','@protonmail.com','@hotmail.com','@icloud.com','@aol.com']
        email = ''.join(random.choice(string.ascii_letters + string.digits)for x in range(12)) + random.choice(domainlist)

        payload = {
            'fingerprint': realfingerprint, 
            'email': email,
            'captcha_key': captchatoken,
            'consent': 'true',
            'date_of_birth': dob(),
            'gift_code_sku_id': 'null',
            'invite': 'null',
            'password': passwod,
            'username': username
        }

        tries = 0
        while tries != 5:
            try:
                registeraccount = httpx.post('https://discord.com/api/v9/auth/register',headers=header,  json=payload, timeout=10)
                if registeraccount.status_code == 201:
                    print(f'{Fore.GREEN}Successfully Registered Account!')
                    break

                elif registeraccount.status_code == 200:
                    print(f'Successfully Registered Account!')
                    break

                elif registeraccount.status_code == 429:
                    print(f'{Fore.RED}Resource is being rate limited! For {registeraccount.text["retry_after"]}')
                    tries += 1
                    time.sleep(3)

                else:
                    print(f'{Fore.RED}Status Code: {registeraccount.status_code}')
                    tries += 1
                    time.sleep(3)

            except Exception as e:
                print(f'Error: {e}')
                tries += 1
                time.sleep(3)

        if tries == 5:
            print(f'{Fore.RED}Max Retries exceeded aborting connection')
            return

        print(f'{Fore.GREEN}Getting Token...')

        token = registeraccount.json()['token']
        
        os.system('cls' if os.name=='nt' else 'clear')
        print(f'{Fore.GREEN}{username}:{email}:{passwod}:{token}')

        with open('tokens.txt','a') as tokenfile:
            tokenfile.write(token + '\n')
        print(f'{Fore.GREEN}Token: {token}')

        print(f'{Fore.GREEN}Waiting 2 minutes')
        time.sleep(120)


amtoftokens = int(input('How many tokens do you want to gen?: '))
print(f'{Fore.RED}Note: Almost all tokens will be locked!')
main(amtoftokens)
