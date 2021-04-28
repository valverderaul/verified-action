import requests, yaml, os
from bs4 import BeautifulSoup

workflow_file = open('.github/workflows/main.yml', 'r')
lines = workflow_file.readlines()

repos  = []
for line in lines:
    if line.strip().startswith("- uses:") or line.strip().startswith("uses:"):
        if not line.split(":")[1].strip().startswith("."):
            req = requests.get("https://github.com/" + line.split(":")[1].split("@")[0].strip())
            soup = BeautifulSoup(req.text, features="html.parser")
            print(soup)


req = requests.get(os.getenv('INPUT_URLACTION'))
soup = BeautifulSoup(req.text, features="html.parser")
verify = soup.find_all("svg", {"class": "octicon octicon-verified text-blue-light"})

if not len(verify):
    print("PELIGRO")