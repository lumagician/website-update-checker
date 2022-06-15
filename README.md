# website-update-checker

Regularly checks if the content of the info page for the pre-duty cyber training has changed.

## instructions

setup env

    virtualenv venv
    source venv/bin/activate

install required python packages

    pip install -r requirements.txt

create .env file

    touch .env

then add your ifttt key and event name as an env variable

    IFTTT_KEY={key}
    IFTTT_EVENT_NAME={event name}