import sys

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
    def inner(phone, name):
        try:
            s_result = func(phone, name)
        except:
            print("Error")
        return s_result
    return inner


def command_hello() -> str:
    return ANSWER["1"]


@input_error
def command_add(phone="", name="") -> str:
    CONTACTS[name] = phone
    answer = ANSWER["2"]
    return answer


@input_error
def command_change(phone="", name="") -> str:
    CONTACTS[name] = phone
    answer = ANSWER["3"]
    return answer


@input_error
def command_phone(name="") -> str:
    answer = CONTACTS[name]
    return answer


def command_show_all() -> str:
    list_a = []
    print(CONTACTS)
    for k in CONTACTS.keys():
        list_a.append(k)
        list_a.append(" ")
        list_a.append(CONTACTS[k])
        list_a.append("\n")
    answer = "".join(list_a)
    return answer


def command_exit():
    sys.exit("Good bye!")


def main():
    while True:
        s = input("Enter command:").lower()
        if s == ".":
            break
        input_list = s.split(" ")
        input_com = input_list[0]
        if input_com == "hello":
            result = command_hello()
        elif (input_com == "good bye") or (input_com == "exit") or (input_com == "close"):
            command_exit()
        elif input_com == "add":
            result = command_add(input_list[1], input_list[2])
        elif input_com == "change":
            result = command(input_list[1], input_list[2])
        elif input_com == "phone":
            result = command_phone(input_list[1])
        elif input_com == "show all":
            result = command_show_all(input_list[1])
        else:
            print("Command undefined! Try again!")
            continue
        print(result)


main()
