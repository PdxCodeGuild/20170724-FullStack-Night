class Contact:
    def __init__(self, name, favorite_fruit, favorite_color, catch_phrase):
        self.name = name
        self.favorite_fruit = favorite_fruit
        self.favorite_color = favorite_color
        self.catch_phrase = catch_phrase

    def __str__(self):
        return f'name: {self.name}\nfavorite fruit: {self.favorite_fruit}\nfavorite color: {self.favorite_color}\n' \
               f'favorite catch phrase: {self.catch_phrase}'


def parse_csv(path):
    contacts = []

    with open('contacts.csv', 'r') as file:
        text = file.read()
        lines = text.split('\n')
        for i in range(1, len(lines)):
            contact_values = lines[i].split(',')

            name = contact_values[0]
            favorite_fruit = contact_values[1]
            favorite_color = contact_values[2]
            catch_phrase = contact_values[3]

            contact = Contact(name, favorite_fruit, favorite_color, catch_phrase)
            contacts.append(contact)

    return contacts


def update_csv(contacts):
    output = 'name,favorite fruit,favorite color,catch phrase'
    for i in range(len(contacts)):
        output += contacts[i].name + ','
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
        action = input('What action do you want to take? (create, retrieve, update, delete, list or done). ')
        if action == 'done':
            print('goodbye')
            break
        elif action == 'create':
            name = input('What is the contact\'s name? ')
            favorite_fruit = input('What is their favorite fruit? ')
            favorite_color = input('What is their favorite color? ')
            favorite_catch_phrase = input('What is their favorite catch phrase? ')

            contact = Contact(name, favorite_fruit, favorite_color, favorite_catch_phrase)
            contacts.append(contact)
        elif action == 'retrieve':
            find_name = input('What is the users name? ')
            for i in range(len(contacts)):
                if contacts[i].name == find_name:
                    print(contacts[i])
        elif action == 'update':
            update_name = input('Provide name: ')
            attribute_name = input('Provide attribute: ')
            attribute_value = input('Provide attribute value: ')
            for i in range(len(contacts)):
                if contacts[i].name == update_name:
                    if attribute_name == 'name':
                        contacts[i].name = attribute_value
                    elif attribute_name == 'favorite fruit':
                        contacts[i].favorite_fruit = attribute_value
                    elif attribute_name == 'favorite color':
                        contacts[i].favorite_color = attribute_value
                    elif attribute_name == 'catch phrase':
                        contacts[i].favorite_catch_phrase = attribute_value
            print_contacts(contacts)
        elif action == 'delete':
            delete_name = input('Provide name: ')
            for i in range(len(contacts)):
                if contacts[i].name == delete_name:
                    del contacts[i]
                    break
        elif action == 'list':
            print_contacts(contacts)
    update_csv(contacts)
main()
