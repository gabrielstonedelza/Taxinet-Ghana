#!/usr/bin/env python
import urllib3
import urllib
import urllib.parse
from datetime import datetime
import urllib.request


def send_sms(api_key, phone, message, sender_id):
    params = {"apikey": api_key, "destination": phone, "message": message, "source": sender_id, "dlr": 0,
              "type": 0, "time": datetime.now()}

    # prepare your url
    url = 'https://sms.textcus.com/api/send?' + urllib.parse.urlencode(params, doseq=True)

    # content = urllib.urlopen(url).read()
    content = urllib.request.urlopen(url)
    print("Message sent")
    # content contains the response from TextCus

    # Defining variables to be used inside function
    api_key = '9OqfypgGXyAUx7422qylPLGrJxz17Nsmq'  # Remember to put your account API Key here
    phone = '23324XXXXXXX'  # International format (233) excluding the (+)
    message = 'This is just a test on TextCus!'
    sender_id = 'TextCus'  # 11 Characters maximum
    date_time = "2017-05-02 00:59:00"


# Calling function that was created to send sms
# send_sms("TG0VqHEFA9ZoqNtnw43GdVkKnBSBIpf2", "233593380008", "Hello Gabriel", "Taxinet")
