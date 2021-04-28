import requests, os
from bs4 import BeautifulSoup

print(os.system('cd /github/workspace/0'))
print("========================")
print(os.system('pwd'))
print("========================")
print(os.system('ls'))

req = requests.get(os.getenv('INPUT_URLACTION'))
soup = BeautifulSoup(req.text, features="html.parser")
verify = soup.find_all("svg", {"class": "octicon octicon-verified text-blue-light"})

if not len(verify):
    print("PELIGRO")