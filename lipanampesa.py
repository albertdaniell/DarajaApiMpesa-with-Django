import datetime
import base64


import requests
from requests.auth import HTTPBasicAuth
import keys
import access_tk
#print(datetime.datetime.now())

unformated_time=datetime.datetime.now()
formatted_time=unformated_time.strftime("%Y%m%d%H%M%S")

#print(formatted_time)

#generating a time stamp

#base 64
data_to_encode=keys.businessShortCode + keys.lipa_na_mpesa_passkey + formatted_time
encoded_string=base64.b64encode(data_to_encode.encode())

decoded_pass=encoded_string.decode('utf8')

#print (decoded_pass)




#print(myaccess_token)

    #print (r.json())


def lipa_na_mpesa():
    access_token = access_tk.myaccess_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": keys.businessShortCode,
    "Password": decoded_pass,
    "Timestamp":formatted_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": keys.partA,
    "PartyB":keys.partB,  
    "PhoneNumber": keys.partA,
    "CallBackURL": "https://fullstack.com/myLMP",
    "AccountReference": "122111",
    "TransactionDesc": "fee payment"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

#generate_token()


lipa_na_mpesa()