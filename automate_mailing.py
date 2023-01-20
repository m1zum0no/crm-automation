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


with requests.Session() as session, open('names.py', 'r') as parsed_data:
    for client_record in parsed_data:
        client_record = list(client_record.split(':'))
        payload['to'] = client_record[0]
        payload['text'] = construct_message(*client_record[1:])    
        response = session.post(URL, json=payload)
        logger.info(f'SMS sent to {payload["to"]}, response status: {response.status_code}')

