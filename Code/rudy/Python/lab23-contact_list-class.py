#   Lab 23  Contact List (Class)

from twilio.rest import Client


class Contact:          # class names are CamelCase (No underscores with capitalization for spaces)
    def __init__(self, name, phone_number, favorite_fruit, favorite_color, catch_phrase):
        self.name = name
        self.phone_number = phone_number
        self.favorite_fruit = favorite_fruit
        self.favorite_color = favorite_color
        self.catch_phrase = catch_phrase

    def __str__(self):
        return f'name: {self.name}, phone number: {self.phone_number} favorite fruit: {self.favorite_fruit}, favorite color: {self.favorite_color}, catch phrase: {self.catch_phrase}'


def load(path):
    contacts = []
    with open(path, 'r') as file:
        text = file.read()
        lines = text.split('\n')
        for i in range(1, len(lines)):
            contact_values = lines[i].split(',')

            name = contact_values[0]
            phone_number = contact_values[1]
            favorite_fruit = contact_values[2]
            favorite_color = contact_values[3]
            catch_phrase = contact_values[4]
            contact = Contact(name, phone_number, favorite_fruit,favorite_color, catch_phrase)

            contacts.append(contact)
    return contacts


def save(path, contacts):
    output = 'name, phone number, favorite fruit, favorite color, catch phrase'
    for i in range(contacts):
        pass


def main():
    path = 'contacts.csv'
    contacts = load(path)

    #create
    while True:
        command = input('What operation would you like to perform or type \'done\' ')
        if command == 'create':
            name = input('What is new contact name? ')
            phone_number = input(f'What is {name}\s phone number? ')
            favorite_fruit = input(f'What is {name}\'s favorite fruit? ')
            favorite_color = input(f'What is {name}\'s favorite color? ')
            catch_phrase = input(f'What is {name}\'s catch phrase? ')
            contact = Contact(name, phone_number, favorite_fruit, favorite_color, catch_phrase)
            contacts.append(contact)
            print(contact)
        #retrieve
        elif command == 'retrieve':
            find_name = input('What is the name you would like to retrieve? ')
            for contact in contacts:
                if contact.name == find_name:
                    print(contact)
        #update
        elif command == "update":
            #attribute_name - get attribute name
            #attribute_value - get new attribute value
            #setattr(contact, attribute_name, attribute_value)

            name_update = input('What is the name you\'d like to update? ')
            attribute_update = input('What is the attribute you\'d like to update? ')

        elif command == 'list':
            for contact in contacts:
                print(contact)

        elif command == 'send sms':
            account_sid = "AC89d0fd5dff581ec57fe20430868376b5"      #user id for Twilio
            auth_token = "b15cccb7a26aa86b42a5f14ebccf23cf"         #authorizing token send by Twilio
            client = Client(account_sid, auth_token)                #client variable assigned to Client Class with above variables

            to_name = input('Who are you sending the message to? ')
            message = input('Type the message here: ')
            contact_num = None
            for contact in contacts:
                if contact.name == to_name:
                    contact_num = contact.phone_number

            client.api.account.messages.create(to=contact_num, from_="+19718033720",body=message)


main()

