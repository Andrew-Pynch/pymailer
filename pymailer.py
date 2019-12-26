def get_address():
    email_address = input("Please enter the email address of the person you are trying to contact: ")
    return email_address


def get_subject():
    subject = input("Please enter the subject of the email: ")
    return subject


def get_message():
    print("Please enter your message. When you are done type STOP and press ENTER: ")

    message_lines = []
    while True:
        message = input()
        if message == "STOP":
            break
        else:
            message_lines.append(message)
            continue

    return message_lines


def print_message(target_address, subject, message_lines):
    print('To: %s \nSubject: %s' % (target_address, subject))
    print('Message:')
    for i in range(len(message_lines)):
        print(message_lines[i] + '\n')
        

def main():
    target_address = get_address()
    subject = get_subject()
    message = get_message()
    print_message(target_address, subject, message)

main()