import os
from twilio.rest import Client

# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
# TWILIO_PHONE_NUMBER = "+15126451472"

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
#account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
#auth_token = os.environ['TWILIO_AUTH_TOKEN']

account_sid = "ACb56a5f78a63da9e3798a8fb5dfe7ca64"
auth_token = "21bdfbbddda75d589f46a497db272059"

# print (account_sid)
# print (auth_token)

client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+6596467552',
                        from_='+15126451472'
                    )

print(call.sid)
#