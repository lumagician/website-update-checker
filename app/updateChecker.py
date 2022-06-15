from base64 import encode
import requests
import hashlib
from bs4 import BeautifulSoup

def getDivContent():
    r = requests.get("https://www.vtg.admin.ch/de/aktuell/themen/cyberdefence/cyber-miliz.html#ui-collapse-739")
    soup = BeautifulSoup(r.text, "html.parser")
    content = soup.find(id="collapse_id_content_vtg-internet_de_aktuell_themen_cyberdefence_cyber-miliz_jcr_content_contentPar_accordion_1").get_text()
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def checkForUpdates():
    hash_old = ""
    hash_new = ""

    # check if hash.txt file already exists
    try:
        with open("./hash.txt", "r") as f:

            hash_old = f.readline()
            hash_new = getDivContent()
            f.close()
        
        with open("./hash.txt", "w") as f:
            f.write(hash_new)
            f.close()

    # create if it doesnt already exist
    except FileNotFoundError:
        with open("./hash.txt", "w") as f:
            f.write(getDivContent())
            f.close()

    if hash_old == hash_new:
        return False
    else:
        return True