from base64 import encode
import requests
import hashlib
from bs4 import BeautifulSoup
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()

HASH_FILE = "hash.txt"

"""

# get response from website, parse it and get the value of the div in question using its id attribute
r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")
content = soup.find(id="collapse_id_content_vtg-internet_de_aktuell_themen_cyberdefence_cyber-miliz_jcr_content_contentPar_accordion_1").get_text()

# hash the value which was extracted above
hash = hashlib.md5(content.encode('utf-8')).hexdigest()

with open(HASH_FILE, "r") as file:
    hash_old = file.read().rstrip()

    # check if empty --> first time running


print(hash_old)
print(hash)

"""