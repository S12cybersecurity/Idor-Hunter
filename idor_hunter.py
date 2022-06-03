import requests
import argparse

parser = argparse.ArgumentParser(description="Python Bruteforce Login")
parser.add_argument('--url', help="Website to target", required=True)
parser.add_argument('--cookie', help="Cookie of Valid User", required=True)
parser.add_argument('--proxy', help="Connect with Proxy", required=False)
parser.add_argument('--params', help="Add parameters in your request", required=False)

args = parser.parse_args()

lista = args.cookie

palabras = lista.split(": ")

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET


proxy = {
  'http': args.proxy,
  'https': args.proxy,
}

if len(palabras) == 1:
  palabras.append(": sdkmnasdlks")
  print(len(palabras))


random = args.cookie+"yw4NnyGkPIq5NPFeAhmkLfQK2Y24U1tPaQdRpJAv"
headers_dict = {palabras[0]:palabras[1]}
headers_dict2 = {palabras[0]:random}

status_codes = list()
content_lenght = list()




def get():
    print(f"{bcolors.OK}GET REQUESTS{bcolors.RESET}")
    header = args.cookie
    original = requests.get(args.url,proxies=proxy,headers=headers_dict,data=args.params)
    print("Authenticated Request")
    print("Status Code: ",original.status_code)
    ee = len(original.content)
    print("Content-Lenght",ee)
    status_codes.append(original.status_code)
    content_lenght.append(ee)
    print("------------------------------------")
    unauthenticated = requests.get(args.url,proxies=proxy,data=args.params)
    print("Unauthenticated Request")
    print("Status Code: ",unauthenticated.status_code)
    eee = len(unauthenticated.content)
    print("Content-Lenght: ",eee)
    status_codes.append(unauthenticated.status_code)
    content_lenght.append(eee)
    print("------------------------------------")
    modified = requests.get(args.url,headers=headers_dict2,proxies=proxy,data=args.params)
    print("Modified Request")
    print("Status Code: ",modified.status_code)
    eeee = len(modified.content)
    print("Content-Lenght: ",eeee)
    print("------------------------------------")
    print("Calculing Results...")
    status_codes.append(modified.status_code)
    content_lenght.append(eeee)


    if content_lenght[0] == content_lenght[1] and content_lenght[2]:
      if status_codes[0] == status_codes[1] and status_codes[2]:
        print(f"{bcolors.OK}[+] Vulnerable to IDOR{bcolors.RESET}")
      else:
        print(f"{bcolors.OK}[+] Possible Vulnerability{bcolors.RESET}")
    elif content_lenght[0] != content_lenght[1]:
      print(f"{bcolors.FAIL}[-] Unauthenticated use it's blocked{bcolors.RESET}")
      if content_lenght[0] == content_lenght[2]:
        print(f"{bcolors.OK}[+] Vuln: Not Verifyng Cookie{bcolors.RESET}")
      else:
        print(f"{bcolors.FAIL}[-] Website verify Cookie{bcolors.RESET}")
        print(f"{bcolors.FAIL}[-] Not vulnearble to IDOR{bcolors.RESET}")
    elif content_lenght[0] != content_lenght[2]:
      print(f"{bcolors.FAIL}[-] Website verify Cookie{bcolors.RESET}")
      if content_lenght[0] == content_lenght[1]:
        print(f"{bcolors.OK}[+] Vuln: Unauthenticated use it's allowed{bcolors.RESET}")
      else:
        print(f"{bcolors.FAIL}[-] Unauthenticated use it's blocked{bcolors.RESET}")
        print(f"{bcolors.FAIL}[-] Not vulnearble to IDOR{bcolors.RESET}")

    else:
      print(f"{bcolors.FAIL}[-] REQUEST ERROR{bcolors.RESET}")




def post():
    print("\n")
    print(f"{bcolors.OK}POST REQUESTS{bcolors.RESET}")
    header = args.cookie
    original = requests.post(args.url,proxies=proxy,headers=headers_dict,data=args.params)
    print("Authenticated Request")
    print("Status Code: ",original.status_code)
    ee = len(original.content)
    print("Content-Lenght",ee)
    status_codes.append(original.status_code)
    content_lenght.append(ee)
    print("------------------------------------")
    unauthenticated = requests.post(args.url,proxies=proxy,data=args.params)
    print("Unauthenticated Request")
    print("Status Code: ",unauthenticated.status_code)
    eee = len(unauthenticated.content)
    print("Content-Lenght: ",eee)
    status_codes.append(unauthenticated.status_code)
    content_lenght.append(eee)
    print("------------------------------------")
    modified = requests.post(args.url,headers=headers_dict2,proxies=proxy,data=args.params)
    print("Modified Request")
    print("Status Code: ",modified.status_code)
    eeee = len(modified.content)
    print("Content-Lenght: ",eeee)
    print("------------------------------------")
    print("Calculing Results...")
    status_codes.append(modified.status_code)
    content_lenght.append(eeee)


    if content_lenght[0] == content_lenght[1] and content_lenght[2]:
      if status_codes[0] == status_codes[1] and status_codes[2]:
        print(f"{bcolors.OK}[+] Vulnerable to IDOR{bcolors.RESET}")
      else:
        print(f"{bcolors.OK}[+] Possible Vulnerability{bcolors.RESET}")
    elif content_lenght[0] != content_lenght[1]:
      print(f"{bcolors.FAIL}[-] Unauthenticated use it's blocked{bcolors.RESET}")
      if content_lenght[0] == content_lenght[2]:
        print(f"{bcolors.OK}[+] Vuln: Not Verifyng Cookie{bcolors.RESET}")
      else:
        print(f"{bcolors.FAIL}[-] Website verify Cookie{bcolors.RESET}")
        print(f"{bcolors.FAIL}[-] Not vulnearble to IDOR{bcolors.RESET}")
    elif content_lenght[0] != content_lenght[2]:
      print(f"{bcolors.FAIL}[-] Website verify Cookie{bcolors.RESET}")
      if content_lenght[0] == content_lenght[1]:
        print(f"{bcolors.OK}[+] Vuln: Unauthenticated use it's allowed{bcolors.RESET}")
      else:
        print(f"{bcolors.FAIL}[-] Unauthenticated use it's blocked{bcolors.RESET}")
        print(f"{bcolors.FAIL}[-] Not vulnearble to IDOR{bcolors.RESET}")

    else:
      print(f"{bcolors.FAIL}[-] REQUEST ERROR{bcolors.RESET}")


def delete():
    print("\n")
    print(f"{bcolors.OK}DELETE REQUESTS{bcolors.RESET}")
    header = args.cookie
    original = requests.delete(args.url,proxies=proxy,headers=headers_dict,data=args.params)
    print("Authenticated Request")
    print("Status Code: ",original.status_code)
    ee = len(original.content)
    print("Content-Lenght",ee)
    status_codes.append(original.status_code)
    content_lenght.append(ee)
    print("------------------------------------")
    unauthenticated = requests.delete(args.url,proxies=proxy,data=args.params)
    print("Unauthenticated Request")
    print("Status Code: ",unauthenticated.status_code)
    eee = len(unauthenticated.content)
    print("Content-Lenght: ",eee)
    status_codes.append(unauthenticated.status_code)
    content_lenght.append(eee)
    print("------------------------------------")
    modified = requests.delete(args.url,headers=headers_dict2,proxies=proxy,data=args.params)
    print("Modified Request")
    print("Status Code: ",modified.status_code)
    eeee = len(modified.content)
    print("Content-Lenght: ",eeee)
    print("------------------------------------")
    print("Calculing Results...")
    status_codes.append(modified.status_code)
    content_lenght.append(eeee)

    if content_lenght[0] == content_lenght[1] and content_lenght[2]:
      if status_codes[0] == status_codes[1] and status_codes[2]:
        print(f"{bcolors.OK}[+] Vulnerable to IDOR{bcolors.RESET}")
      else:
        print(f"{bcolors.OK}[+] Possible Vulnerability{bcolors.RESET}")
    elif content_lenght[0] != content_lenght[1]:
      print(f"{bcolors.FAIL}[-] Unauthenticated use it's blocked{bcolors.RESET}")
      if content_lenght[0] == content_lenght[2]:
        print(f"{bcolors.OK}[+] Vuln: Not Verifyng Cookie{bcolors.RESET}")
      else:
        print(f"{bcolors.FAIL}[-] Website verify Cookie{bcolors.RESET}")
        print(f"{bcolors.FAIL}[-] Not vulnearble to IDOR{bcolors.RESET}")
    elif content_lenght[0] != content_lenght[2]:
      print(f"{bcolors.FAIL}[-] Website verify Cookie{bcolors.RESET}")
      if content_lenght[0] == content_lenght[1]:
        print(f"{bcolors.OK}[+] Vuln: Unauthenticated use it's allowed{bcolors.RESET}")
      else:
        print(f"{bcolors.FAIL}[-] Unauthenticated use it's blocked{bcolors.RESET}")
        print(f"{bcolors.FAIL}[-] Not vulnearble to IDOR{bcolors.RESET}")

    else:
      print(f"{bcolors.FAIL}[-] REQUEST ERROR{bcolors.RESET}")



get()
post()
delete()