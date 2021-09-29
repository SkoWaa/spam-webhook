import requests, time

from colorama import Fore

print(f"[{Fore.GREEN}>{Fore.RESET}] Lien Webhook  ")
link = input(" > ")
print(f"[{Fore.GREEN}>{Fore.RESET}] Message à envoyé ")
message = input(" > ")
print(f"[{Fore.GREEN}>{Fore.RESET}] Nom du Webhook ")
name = input(" > ")

payload = {
  'content': message,
  'username': name
}

while True:
  try:
    time.sleep(0.5)
    r = requests.post(link, json=payload)
    f = open('log.txt', 'a+') 
    if 'Limite atteint.' in r.text:
      f.write('Ratelimited\n')
    else:
      f.write(f"Spam : {message}\n")  
    f.close()
    if r.status_code == 204:
      print(f"[{Fore.GREEN}+{Fore.RESET}] Message envoyé !")
    else:
      print(f"[{Fore.RED}-{Fore.RESET}] Ratelimit/Error")
  except requests.exceptions.MissingSchema:
    print(f"[{Fore.RED}-{Fore.RESET}] Url invalide ou introuvable.");break
