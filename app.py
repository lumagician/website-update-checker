from base64 import encode
import requests
import hashlib
from bs4 import BeautifulSoup

HASH_FILE = "hash.txt"

# get response from website, parse it and get the value of the div in question using its id attribute
r = requests.get("https://www.vtg.admin.ch/de/aktuell/themen/cyberdefence/cyber-miliz.html#ui-collapse-739")
soup = BeautifulSoup(r.text, "html.parser")
content = soup.find(id="collapse_id_content_vtg-internet_de_aktuell_themen_cyberdefence_cyber-miliz_jcr_content_contentPar_accordion_1").get_text()

# hash the value which was extracted above
hash = hashlib.md5(content.encode('utf-8')).hexdigest()

with open(HASH_FILE, "r") as file:
    hash_old = file.read().rstrip()

    if(hash == hash_old):
        print("no change")
    if(hash != hash_old):
        print("hash changed")


print(hash_old)
print(hash)
