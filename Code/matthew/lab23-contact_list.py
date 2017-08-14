"""
Lab 23: Contact List
"""


def parse_csv(path):
    contacts = []
    header = None
    with open(path, 'r') as file:
        text = file.read()
        lines = text.split('\n')
        header = lines[0].split(',')
        for i in range(1, len(lines)):
            contact_values = lines[i].split(',')

    return header, contacts


header, contacts = parse_csv('contacts.csv')

while True:
    command = input('what operation would you like to perform?')
    if command == 'create':
        for attribute_name in header:
            attribute = input('what is the contact\'s ' + attribute_name)

