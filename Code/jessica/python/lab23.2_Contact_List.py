from twilio.rest import Client


class Contact:
    def __init__(self, name, phone_number, favorite_fruit, favorite_color, catch_phrase):
        self.name = name
        self.phone_number = phone_number
        self.favorite_fruit = favorite_fruit
        self.favorite_color = favorite_color
        self.catch_phrase = catch_phrase

    def __str__(self):
        return f'name: {self.name}\nphone number: {self.phone_number}\nfavorite fruit: {self.favorite_fruit}\n' \
               f'favorite color: {self.favorite_color}\ncatch phrase: {self.catch_phrase}'


def parse_csv(path):
    contacts = []
    with open('contacts.csv', 'r') as file:
        text = file.read()
        lines = text.split('\n')
        for i in range(1, len(lines)):
            contact_values = lines[i].split(',')
            name = contact_values[0]
           phone_number = contact_values[1]
            favorite_fruit = contact_values[2]
            favorite_color = contact_values[3]
           catch_phrase = contact_values[4]
            contact = Contact(name, phone_number, favorite_fruit, favorite_color, catch_phrase)
            # or contact = Contact(name = contact_values[0], etc...catch_phrase = contact_values[4])
             contacts.append(contact)
     #return contacts


 def update_csv(contacts):
     output = 'name,phone number,favorite fruit,favorite color,catch phrase'
     for i in range(len(contacts)):
         output += contacts[i].name + ','
         output += contacts[i].phone_number + ','
         output += contacts[i].favorite_fruit + ','
         output += contacts[i].favorite_color + ','
         output += contacts[i].catch_phrase
         if i < len(contacts) - 1:
             output += '\n'
     with open('contacts.csv', 'w') as file:
         file.write(output)


 def print_contacts(contacts):
     for contact in contacts:
         print(contact)
         print()


 def main():
     contacts = parse_csv('contacts.csv')

     while True:
         action = input('What action do you want to take? (create, retrieve, update, delete, list, send SMS, or done). ')
         if action == 'done':
             print('goodbye')
             break
         elif action == 'create':
             name = input('What is the contact\'s name? ')
             phone_number = input('What is their phone number? ')
             favorite_fruit = input('What is their favorite fruit? ')
             favorite_color = input('What is their favorite color? ')
             favorite_catch_phrase = input('What is their catch phrase? ')

             contact = Contact(name, phone_number, favorite_fruit, favorite_color, favorite_catch_phrase)
             contacts.append(contact)
         elif action == 'retrieve':
             find_name = input('What is the users name? ')
             for i in range(len(contacts)): #could use a find contact function instead of using loop
                 if contacts[i].name == find_name:
                     print(contacts[i])
         elif action == 'update':
             update_name = input('Provide name: ')
             attribute_name = input('Provide attribute: ')
             attribute_value = input('Provide attribute value: ')
             for i in range(len(contacts)): #could use a find contact function instead of using loop
                 if contacts[i].name == update_name:
                     #setattr(contact,attribute_name, attribute_value) setattr is a built in function would need
                     #  validation so that for example attribute_name is not set to something weird (ie Fred)
                     if attribute_name == 'name':
                        contacts[i].name = attribute_value
                     elif attribute_name == 'phone number':
                         contacts[i].phone_number = attribute_value
                     elif attribute_name == 'favorite fruit':
                         contacts[i].favorite_fruit = attribute_value
                     elif attribute_name == 'favorite color':
                         contacts[i].favorite_color = attribute_value
                    elif attribute_name == 'catch phrase':
                         contacts[i].favorite_catch_phrase = attribute_value
             print_contacts(contacts)
         elif action == 'delete':
             delete_name = input('Provide name: ')
            for i in range(len(contacts)): #could use a find contact function instead of using loop
                 if contacts[i].name == delete_name:
                     del contacts[i]
                     break
         elif action == 'list':
             print_contacts(contacts)
         elif action == 'send SMS':\
            contact_name = input('Who do you want to send the message to? ') # if you want to send to everyone loop thru
            # message_to_send = input('What do you want the message to say? ')
             for i in range(len(contacts)):
                 if contacts[i].name == contact_name:
                     account_sid = 'XXXXXX'
                     auth_token = 'XXXXX'
                     client = Client(account_sid, auth_token)
                     message = client.api.account.messages.create(
                        to=contacts[i].phone_number,
                        from_="+19718033720",
                        body=message_to_send)
     update_csv(contacts)
 main()