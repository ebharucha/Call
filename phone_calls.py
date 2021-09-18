import os
from twilio.rest import Client

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# print (account_sid)
# print (auth_token)

client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+xxxxxxxxxx',
                        from_='+1yyyyyyyyyy'
                    )

print(call.sid)