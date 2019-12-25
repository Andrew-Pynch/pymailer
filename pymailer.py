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

    sentence = ' '.join(word[0] for word in message_lines)
    return sentence

#get_address()
#get_subject()
print(get_message())
