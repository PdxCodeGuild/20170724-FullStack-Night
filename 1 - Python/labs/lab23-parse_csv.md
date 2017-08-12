
# Lab 22: Contact List


Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of `name`, `favorite fruit`, `favorite color`, `catch phrase`.



## Version 2

Implement a CRUD REPL

- **C**reate a record
- **R**etrieve a record
- **U**pdate a record
- **D**elete a record

## Version 4

When REPL loop finishes, write the updated contact info to the CSV file to be saved.

## Version 5

Add a `phone number` column. We'll use the Twilio API to send SMS messages from the terminal.


```python
# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+12316851234",
                                             from_="+15555555555",
                                             body="Hello there!")
```


