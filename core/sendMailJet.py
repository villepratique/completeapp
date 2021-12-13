from mailjet_rest import Client
import os

def executeSendMail(subject , from_email , to_email , body):
    api_key = os.environ['MJ_APIKEY_PUBLIC']
    api_secret = os.environ['MJ_APIKEY_PRIVATE']
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": from_email,
            "Name": "NOM DU PROJET"
        },
        "To": [
            {
            "Email": to_email,
            "Name": ""
            }
        ],
        "Subject": subject,
        "TextPart": "",
        "HTMLPart": body
        }
    ]
    }
    try:
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())
        return True
    except:
        print("error sending mail")
        return False