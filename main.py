CONTACTS = {}


def command_hello(phone="", name="") -> str:
    s = "How can I help you?"
    return s


def command_add(phone="", name="") -> str:
    CONTACTS[name] = phone
    answer = "Contact save fine!"
    return answer


def command_change(phone="", name="") -> str:
    CONTACTS[name] = phone
    answer = "Contact update fine!"
    return answer


def command_phone(phone="", name="") -> str:
    print()
    answer = "Contact update fine!"
    return answer


def command_show_all(phone="", name="") -> str:
    pass


def command_exit(phone="", name="") -> str:
    return "Good bye!"


PARSER = {
    "hello": command_hello,
    "add": command_add,
    "change": command_change,
    "phone": command_phone,
    "show all": command_show_all,
    "good bye": command_exit,
    "close": command_exit,
    "exit": command_exit
}


def command(input_command: str):
    return PARSER[input_command]


def main():
    while True:
        s = input("Введіть команду:").islower()
        if s == ".":
            break
        input_list = s.split(" ")
        if len(input_list) == 1:
            print(command(s[0])(CONTACTS)
        else:
            print(command(s[0])(s[1], s[2]))


main()
