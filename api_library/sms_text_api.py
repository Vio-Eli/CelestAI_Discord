"""
A simple API to send SMS text messages to mobile devices
"""

import requests

from celestai.classes.api import Api
from celestai.apis import api_lib

URL = 'http://textbelt.com/text'


class SmsTextApi(Api):

    def __init__(self):
        super(SmsTextApi, self).__init__('sms_text_api')

    def send_text(self, text, number=None):
        """ Sends the text message to the desired phone number """
        if number is None:
            if hasattr(api_lib['user_api'], 'phone'):
                number = api_lib['user_api'].phone
            else:
                print('\n~ I could not find a default phone number.\n')
                return
        print('\n~ Sending text to '+str(number)+'...\n')
        params = {'number': number, 'message': text}
        resp = requests.post(URL, params)
        print('~ SMS Text success? '+str(resp)+'\n')
