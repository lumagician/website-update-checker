# website-update-checker

Regularly checks if the content of the info page for the pre-duty cyber training has changed. Deployed on Linode on a light linux box. The python script is run regularly.

## instructions

setup env

    python3 -m venv venv
    source venv/bin/activate

install required python packages

    pip install -r requirements.txt

add bot token to environment as variable

    export TELEGRAM_BOT_TOKEN=<YOUR_BOT_TOKEN>