import requests, os
from bs4 import BeautifulSoup

req = requests.get(os.getenv('INPUT_URLACTION'))
soup = BeautifulSoup(req.text, features="html.parser")
verify = soup.find_all("svg", {"class": "octicon octicon-verified text-blue-light"})

if not len(verify):
    print("PELIGRO")