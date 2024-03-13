def write_to_file(title, body, file_path):
    with open(file_path, 'a+') as file:  # With Statement makes sure the file closes
        file.write(f'{title}: {body}\n')  # Writes new line to file


def read_from_file(file_path):
    entries = []  # Store data read from file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            title, body = map(str.strip, line.split(':'))  # str.strip remove any white space, line.split() is separator
            entries.append({'title': title,
                            'body': body
                            })  # Dictionary
    return entries


# Example usage
note_choice = input('Would you like to 𝙎𝙏𝙊𝙍𝙀 or 𝙍𝙀𝘼𝘿 all notes? ').lower()

if note_choice == 'store':
    title_input = input('\033[1mEnter Title: \033[0m').title().capitalize()  # \033[1m \033[0m is bold text
    body_input = input('Enter body: ')

    write_to_file(title_input, body_input, 'notes.txt')  # Value obtained by user input
    print('Your note has been added to the file.')

elif note_choice == 'read':
    entries = read_from_file('notes.txt')

    for entry in entries:
        print(f'\n\033[1mTitle: \033[0m\n {entry["title"]}',
              f'\n\nBody:\n {entry["body"]}')
else:
    print('Invalid input')

