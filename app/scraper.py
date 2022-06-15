from base64 import encode
import requests
import hashlib
from bs4 import BeautifulSoup

def getDivContent():
    r = requests.get("https://www.vtg.admin.ch/de/aktuell/themen/cyberdefence/cyber-miliz.html#ui-collapse-739")
    soup = BeautifulSoup(r.text, "html.parser")
    content = soup.find(id="collapse_id_content_vtg-internet_de_aktuell_themen_cyberdefence_cyber-miliz_jcr_content_contentPar_accordion_1").get_text()
    return hashlib.md5(content.encode('utf-8')).hexdigest()