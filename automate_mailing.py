import requests
import logging
from credentials import API_KEY, URL, USERNAME
from sms_template import construct_message


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


payload = {
    'user_name': USERNAME,
    'api_key': API_KEY,
    'action': 'calls.send_sms',
}


with requests.Session() as session, open('test.py', 'r') as users:
    for user in users:
        user = list(user.split(':'))
        payload['to'] = user[0]
        payload['text'] = construct_message(*user[1:])    
        response = session.post(URL, json=payload)
        logger.info(f'SMS sent to {payload["to"]}, response status: {response.status_code}')

