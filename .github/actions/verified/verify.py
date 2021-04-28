import requests, yaml, os
from bs4 import BeautifulSoup

workflow_file = open('.github/workflows/main.yml', 'r')
lines = workflow_file.readlines()

repos  = []
for line in lines:
    if line.strip().startswith("- uses:") or line.strip().startswith("uses:"):
        if not line.split(":")[1].strip().startswith("."):
            req_to_repo = requests.get("https://github.com/" + line.split(":")[1].split("@")[0].strip())
            print(req_to_repo)
            soup = BeautifulSoup(req.text, features="html.parser")
            action = soup.find("a", string="View on Marketplace")['href']
            print(action)
            req_to_action = requests.get("https://github.com" + action)
            verify = soup.find_all("svg", {"class": "octicon octicon-verified text-blue-light"})
            
            if not len(verify):
                print("La acción: " + action + " no está verificada.")