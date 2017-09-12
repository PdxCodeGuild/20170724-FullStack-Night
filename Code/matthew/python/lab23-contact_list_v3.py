"""
Lab 23: Contact List
Manage a list of contacts with a CSV file and a CRUDL REPL
"""
from twilio.rest import Client


class Contact:
    def __init__(self, name, phone_number, favorite_fruit, favorite_color, catch_phrase):
        self.name = name
        self.phone_number = phone_number
        self.favorite_fruit = favorite_fruit
        self.favorite_color = favorite_color
        self.catch_phrase = catch_phrase


# load the contacts from the given CSV
def load(path):
    contacts = []
    with open(path, 'r') as file:
        text = file.read()  # read all the text as one giant string
        lines = text.split('\n')  # split the text into multiple lines
        for i in range(1, len(lines)):  # skip over the header, every line after represents a contact
            contact_values = lines[i].split(',')  # attribute values of the contact
            name = contact_values[0]
            phone_number = contact_values[1]
            favorite_fruit = contact_values[2]
            favorite_color = contact_values[3]
            catch_phrase = contact_values[4]
            contact = Contact(name=contact_values[0],
                                phone_number=contact_values[1],
                                favorite_fruit = contact_values[2],
                                favorite_color = contact_values[3],
                                catch_phrase = contact_values[4])
            contact = Contact(name, phone_number, favorite_fruit, favorite_color, catch_phrase)
            contacts.append(contact)

    return contacts


# save the list of contacts to a csv file
def save(path, contacts):
    output = 'name,phone number,favorite fruit,favorite color,catch phrase'
    for i in range(len(contacts)):

        output += contacts[i].name + ','
        output += contacts[i].phone_number + ','
        output += contacts[i].favorite_fruit + ','
        output += contacts[i].favorite_color + ','
        output += contacts[i].catch_phrase

        if i < len(contacts)-1:  # avoid adding an extra newline at the end
            output += '\n'

    with open(path, 'w') as file:
        file.write(output)


def print_contact(contact):
    output = 'name: ' + contact.name + '\n'
    output += '\tphone_number:   ' + contact.phone_number + '\n'
    output += '\tfavorite fruit: ' + contact.favorite_fruit + '\n'
    output += '\tfavorite color: ' + contact.favorite_color + '\n'
    output += '\tcatch phrase:   ' + contact.catch_phrase + '\n'
    print(output)


def find_contact(name, contacts):
    for contact in contacts:
        if contact.name == name:
            return contact
    return None



def send_sms(contact, message):
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    whatever = client.messages.create(to=contact.phone_number,
                                     from_="+19718033720",
                                     body=message)


def main():
    path = 'contacts2.csv'
    contacts = load(path)

    while True:
        command = input('what operation would you like to perform? ')
        if command == 'help' or command == 'commands':
            print('create: create a contact')
            print('retrieve: retrieve a contact')
            print('update: update a contact')
            print('delete: delete a contact')
            print('list: list all contacts')
            print('send sms: send a contact an sms')
            print('help/commands: show this text')
            print('done: exit the program')
        elif command == 'done':
            break
        elif command == 'create':
            contact = {}
            name = input('what is the contact\'s name? ')
            phone_number = input('what is ' + contact.name + '\'s phone number? ')
            favorite_fruit = input('what is ' + contact.name + '\'s favorite fruit? ')
            favorite_color = input('what is ' + contact.name + '\'s favorite color? ')
            catch_phrase = input('what is ' + contact.name + '\'s catch phrase? ')
            contact = Contact(name, phone_number, favorite_fruit, favorite_color, catch_phrase)
            contacts.append(contact)
        elif command == 'retrieve':
            contact_name = input('what is the name of the contact you\'d like to retrieve? ')
            contact = find_contact(contact_name, contacts)
            if contact is None:
                print('contact not found')
            else:
                print_contact(contact)
        elif command == 'update':
            contact_name = input('what is the name of the contact you\'d like to update? ')
            contact = find_contact(contact_name, contacts)
            if contact is None:
                print('contact not found')
            else:
                attribute_name = input('what attribute would you like to update? ')
                attribute_value = input('what is that attribute\'s value? ')
                setattr(contact, attribute_name, attribute_value)
                # if attribute_name == 'name':
                #     contact.name = attribute_value
                # elif attribute_name == 'phone number':
                #     contact.phone_number = attribute_value
                # ...
        elif command == 'delete':
            contact_name = input('what is the name of the contact you\'d like to delete? ')
            contact = find_contact(contact_name, contacts)
            contacts.remove(contact)
        elif command == 'list':
            for contact in contacts:
                print_contact(contact)
                print()
        elif command == 'send sms':
            contact_name = input('to whom would you like to send an sms? ')
            if contact_name == 'all':
                message = input('what is the message you\'d like to send? ')
                for contact in contacts:
                    send_sms(contact, message)
            else:
                contact = find_contact(contact_name, contacts)
                if contact is None:
                    print('contact not found')
                else:
                    message = input('what is the message you\'d like to send? ')
                    send_sms(contact, message)
                    print('sms sent')
        else:
            print('command not recognized')

    save(path, contacts)

main()
