# Функція parse_input розбирає введений користувачем рядок на команду та її аргументи.
# Команди та аргументи розпізнаються незалежно від регістру введення.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Функції обробки команд


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "User is not found"


def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "User is not found"


def show_all(contacts):
    result = ''
    for name in contacts:
        result += f"{name}'s phone number: {contacts[name]}\n"
    return result


# Функція main управляє основним циклом обробки команд.
# Команди розпізнаються незалежно від регістру введення або зайвих пропусків.


def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts), end='')
        else:
            print('Invalid command')


if __name__ == "__main__":
    main()
