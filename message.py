#sending text messages
import twilio
import twilio.rest
from twilio.rest import TwilioRestClient
accountSID='ACbcccf5d7007895a74e45fac4f5ce2e39'
authtoken='da98937a6467f2a584ca6b3a725871a2'
twilio=TwilioRestClient(accountSID,authtoken)
mynumber='+15129483374'
try:
    cellphone=input("enter the recepient phone number")

    message=twilio.messages.create(body=input('enter message'),from_ =         mynumber,to=cellphone)
except Exception as e:
    print("please enter a valid phone number")
