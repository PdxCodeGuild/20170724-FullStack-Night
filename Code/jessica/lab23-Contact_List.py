def parse_csv(path):
    contacts = []
    header = []
    with open('contacts.csv', 'r') as file:
        text = file.read()
        lines = text.split('\n')
        header = lines[0].split(',')
        for i in range(1, len(lines)):
            contact_values = lines[i].split(',')

            contact = {}
            for j in range(len(header)):
                contact[header[j]] = contact_values[j]
            contacts.append(contact)
    return header, contacts

header, contacts = parse_csv('contacts.csv')

while True:
    action = input('What action do you want to take? (create, retrieve, update, delete or done). ')
    if action == 'done':
        print('goodbye')
        break
    elif action == 'create':
        contact = {}
        for attribute_name in header:
            attribute = input('What is the contact\'s ' + attribute_name)
            contact[attribute_name] = attribute
            contacts.append(contact)
    elif action == 'retrieve':
        find_name = input('What is the users name? ')
        for i in range(len(contacts)):
            contact = contacts[i]
            if contact['name'] == find_name:
                print(contact)
    elif action == 'update':
        update_name = input('Provide name: ')
        update_attribute = input('Provide attribute: ')
        attribute_value = input('Provide attribute value: ')

    # elif action == 'delete':







