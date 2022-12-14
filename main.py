import sys
# import functools

CONTACTS = {}

ANSWER = {
    "1": "How can I help you?",
    "2": "Contact save fine!",
    "3": "Contact update fine!",
    "4": "Enter user name",
    "5": "Give me name and phone please"
}


# def input_error(func):
#     def inner(phone, name):
#         try:
#             s_result = func(phone, name)
#         except:
#             print("Error")
#         return s_result
#     return inner


def command_hello(phone="", name="") -> str:
    return ANSWER["1"]


# @input_error
def command_add(phone="", name="") -> str:
    CONTACTS[name] = phone
    answer = ANSWER["2"]
    return answer


# @input_error
def command_change(phone="", name="") -> str:
    CONTACTS[name] = phone
    answer = ANSWER["3"]
    return answer


# @input_error
def command_phone(phone="", name="") -> str:
    answer = CONTACTS[name]
    return answer


# @input_error
def command_show_all(phone="", name="") -> str:
    list_a = []
    for k, v in CONTACTS.keys(), CONTACTS.values():
        list_a.append(k)
        list_a.append(v)
        list_a.append("\n")
    answer = "".join(list)
    return answer


def command_exit(phone="", name=""):
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
        s = input("Введіть команду:").lower()
        if s == ".":
            break
        itar_avel = False
        for k in PARSER.keys():
            if s.startswith(k):
                input_com = k
                pert_2_s = s.removeprefix(k+" ")
                itar_avel = True
                break
        if not itar_avel:
            print("Команда не распознана! Введите заново!")
            break
        input_list = pert_2_s.split(" ")
        if len(input_list) >= 2:
            result = command(input_com)(input_list[0], input_list[1])
        else:
            result = command(input_com)
        print(result)


main()
