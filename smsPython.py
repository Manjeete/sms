from twilio.rest import Client 
 
account_sid = 'AC2b3a032de734f4bd31fa6102671637fb' 
auth_token = 'auth_token' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12564084374',
                              body = 'Hey ! This is my python Scripting part',        
                              to='+91xxxxxxxxx' 
                          ) 
 
print(message.sid)