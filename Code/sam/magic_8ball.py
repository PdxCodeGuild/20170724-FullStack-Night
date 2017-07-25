import random  # import the random module

responses = ['possibly', 'probably not', 'seems likely', 'don\'t think so', 'yes', 'no', 'don\'t think so', 'I doubt it',]  # create a list of possible responses

question = input('Ask me anything.')  # Have user ask question

reply = random.choice(responses)  # assign random value to reply variable by using random.choice
                                  #  to randomly pick from list of responses
print(reply)