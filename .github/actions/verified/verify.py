import requests, yaml, os
from bs4 import BeautifulSoup

workflow_file = open('.github/workflows/main.yml', 'r')
lines = workflow_file.readlines()

for line in lines:
    if line.strip().startswith("- uses:") or line.strip().startswith("uses:"): # Cogemos todas las acciones del workflow, quitamos tabs
        if not line.split(":")[1].strip().startswith("."): # Descartamos nuestras propias actions
            req_to_repo = requests.get("https://github.com/" + line.split(":")[1].split("@")[0].strip()) # Quitamos la branch y hacemos la req al repo 
            soup = BeautifulSoup(req_to_repo.text, features="html.parser")
            action = soup.find("a", string="View on Marketplace")['href'] # Buscamos el botón del View on Marketplace y cogemos el enlace al marketplace
            req_to_action = requests.get("https://github.com" + action)
            soup = BeautifulSoup(req_to_action.text, features="html.parser")
            verify = soup.find_all("svg", {"class": "octicon octicon-verified text-blue-light"}) # Buscamos el icono de verificado
            
            if len(verify):
                print("La acción: " + action + " está verificada.")
            else:
                print("La acción: " + action + " no está verificada.")