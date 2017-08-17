#   Lab 23  Contact List


def create(header):
    contact_create = {}
    for attribute_name in header:
        attribute = input('What is your ' + attribute_name + ': ')
        contact_create[attribute_name] = attribute
    return contact_create


def retrieve(header, contacts):
    value_retrieve = input('What is the name of the contact? ')  # user inputs name as a string
    for contact in contacts:
        if contact['name'] == value_retrieve:
            return contact


def update(header, contacts):
    contact = retrieve(header, contacts)
    print(header)
    attribute_update = input('What attribute above would you like to update? ')
    value_update = input('What is the value of the attribute you\'d like to update? ')
    contact[attribute_update] = value_update
    return contact, attribute_update


def delete(header, contacts):
    contact = retrieve(header, contacts)
    deleted_contact = contact
    attribute_delete = input('Are you sure you want to delete this contact? ')
    if attribute_delete == ['yes', 'y', 'Yes', 'YEs', 'YES', 'yea', 'definitely']:
        del contacts[attribute_delete]
        return contact


def parse_csv(path):
    contacts = []
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


def save(path, header, contacts):
    output = ','.join(header) + '\n'
    for i in range(len(contacts)):
        for j in range(len(header)):
            output += contacts[i][header[j]]
            if j < len(header)-1:
                output += ','
        if i < len(contacts)-1:
            output += '\n'

    print(output)
    with open(path, 'w') as file:
        file.write(output)


def main():
    header, contacts = parse_csv('contacts.csv')
    while True:
            command = input('What operation would you like to perform or type \'done\' ')
            if command == 'create':
                new_contact = create(header)
                contacts.append(new_contact)
                print(new_contact)
            elif command == 'retrieve':
                retrieved_contact = retrieve(header, contacts)
                print(retrieved_contact)
            elif command == 'update':
                updated_contact = update(header, contacts)
                print(updated_contact)
            elif command == 'delete':
                delete(header, contacts)
                print('Contact has been deleted.')
            elif command == 'done':
                break
    save('contacts.csv', header, contacts)

main()
