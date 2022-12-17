import sys
# import functools

CONTACTS = {
    "name": "+38099066222"
}

ANSWER = {
    "1": "How can I help you?",
    "2": "Contact save fine!",
    "3": "Contact update fine!",
    "4": "Enter user name",
    "5": "Give me name and phone please"
}


def input_error(func):
    def inner(*contacts):
        try:
            s_result = func(*contacts)
        except:
            print("Error")
        return s_result
    return inner()


def command_hello() -> str:
    return ANSWER["1"]


@input_error
def command_add(phone, name) -> str:
    CONTACTS[name] = phone
    return ANSWER["2"]


@input_error
def command_change(phone, name) -> str:
    CONTACTS[name] = phone
    return ANSWER["3"]


def command_phone(name) -> str:
    answer = CONTACTS[name]
    return answer


def command_show_all() -> str:
    list_a = []
    for k in CONTACTS.keys():
        list_a.append(k)
        list_a.append(CONTACTS[k])
        list_a.append("\n")
    answer = " ".join(list_a)
    return answer


def command_exit():
    sys.exit("Good bye!")


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
    return PARSER[input_command]()


def main():
    while True:
        s = input("Enter command:").lower()
        if s == ".":
            break
        itar_avel = False
        for k in PARSER.keys():
            if k in s:
                input_com = k
                pert_2_s = s.removeprefix(k)
                itar_avel = True
                break
        if not itar_avel:
            print("Command undefined! Try again!")
            break
        input_list = pert_2_s.split(" ")
        input_list.remove("")
        if pert_2_s == '':
            result = command(input_com)
        elif len(input_list) >= 2:
            result = command(input_com)(input_list[0], input_list[1])
        else:
            result = command(input_com)(input_list[0])
        print(result)


main()
