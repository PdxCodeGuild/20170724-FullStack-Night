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


def update_csv(header,contacts):
    output = ','.join(header) + '\n'

    for i in range(len(contacts)):
        # output += contact['name'] + ',' + contact['favorite fruit'] + '\n'
        #print(contacts[i])
        for j in range(len(header)):
            attribute_name = header[j]
            output += contacts[i][attribute_name]
            if j < len(header) - 1:
                output += ','
        if i < len(contacts) - 1:
            output += '\n'
    #print(output)

    with open('contacts.csv', 'w') as file:
        file.write(output)

header, contacts = parse_csv('contacts.csv')



while True:
    action = input('What action do you want to take? (create, retrieve, update, delete, list or done). ')
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
            #contact = contacts[i]
            if contacts[i]['name'] == find_name:
                print(contacts[i])
    elif action == 'update':
        update_name = input('Provide name: ')
        update_attribute = input('Provide attribute: ')
        attribute_value = input('Provide attribute value: ')
        for contact in contacts:
            if contact['name'] == update_name:
                contact[update_attribute] = attribute_value
                print(contact)
    elif action == 'delete':
        delete_name = input('Provide name: ')
        for i in range(len(contacts)):
            if contacts[i]['name'] == delete_name:
                del contacts[i]
                break
    elif action == 'list':
        print(contacts)
update_csv(header,contacts)










