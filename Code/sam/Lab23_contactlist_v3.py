class Contact:

    def __init__(self, name, phone_number, favorite_fruit, favorite_color, catch_phrase):
        self.name = name
        self.phone_number = phone_number
        self.favorite_fruit = favorite_fruit
        self.favorite_color = favorite_color
        self.catch_phrase = catch_phrase

    def __str__(self):
        return 'name: ' + self.name + '|' + 'favorite fruit ' + self.favorite_fruit + '|' + 'favorite color ' + self.favorite_color + '|' + 'catch phrase ' + self.catch_phrase


def find_contact(name, contacts):
    for contact in contacts:
        if contact.name == name:
            return contact
    return None

def load(path):
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
            contacts.append(contact)
    return contacts





def main():
    from twilio.rest import Client
    account_sid = 'AC89d0fd5dff581ec57fe20430868376b5'
    auth_token = 'b15cccb7a26aa86b42a5f14ebccf23cf'
    client = Client(account_sid, auth_token)


    contacts = load('contacts.csv')
    while True:
        user_input = input('Please input the command you would like to perform:\n\t List \n\t Create\n\t Retrieve\n\t Update \n\t Delete\n\t Send SMS\n\t ')
        if user_input == 'List':
            for contact in contacts:
                print(contact)
                print()
        elif user_input == 'Create':
            name = input('What is the contacts name?: ')
            phone_number = input('What is the contacts phone number?: ')
            favorite_fruit = input('What is the contacts favorite fruit?: ')
            favorite_color = input('What is the contacts favorite color?: ')
            catch_phrase = input('What is the contacts favorite catch phrase?: ')
            contact = Contact(name, phone_number, favorite_fruit, favorite_color, catch_phrase)
            contacts.append(contact)
        elif user_input == 'Retrieve':
            contact_name = input('Please input the name of the contact you would like to retrieve: ')
            contact = find_contact(contact_name, contacts)
            print(contact)
        elif user_input == 'Update':
            contact_name = input('Please input the name of the contact you would like to update: ')
            contact = find_contact(contact_name, contacts)
            attribute_name = input('Please input the attribute you would like to update: ')
            attribute_value = input('What would you like to update this attribute too?: ')
            if attribute_name == 'name':
                contact.name = attribute_value
            elif attribute_name == 'favorite fruit':
                contact.favorite_fruit = attribute_value
            elif attribute_name == 'favorite color':
                contact.favorite_color = attribute_value
            elif attribute_name == 'catch phrase':
                contact.catch_phrase = attribute_value
            elif attribute_name == 'phone number':
                contact.phone_number = attribute_value
        elif user_input == 'Delete':
            contact_name = input('Please input the name of the contact you would like to delete: ')
            contact = find_contact(contact_name, contacts)
            contacts.remove(contact)
        elif user_input == 'Send SMS':
            contact_name = input('Please input the name of the contact you would like to send an SMS: ')
            contact = find_contact(contact_name, contacts)
            sms = input('Input the message you would like to send: ')
            message = client.api.account.messages.create(to=contact.phone_number,
                                                         from_="+19718033720",
                                                         body=sms)









main()