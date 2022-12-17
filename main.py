import sys

CONTACTS = {
    "name": "phones"
}

ANSWER = {
    "1": "How can I help you?",
    "2": "Contact save fine!",
    "3": "Contact update fine!",
    "4": "Enter user name!",
    "5": "Give me name and phone please!",
    "6": "Unknown error. Try entering the command again!",
    "7": "There is no user with this name!",
    "8": "You entered something wrong!"
}


def input_error_main(func):
    def inner(*args, **kwargs):
        while True:
            try:
                s_result = func(*args, **kwargs)
                return s_result
            except Exception as e:
                if e.__class__ == UnboundLocalError:
                    if "name" in e.args[0]:
                        print(ANSWER["4"])
                    elif "phone" in e.args[0]:
                        print(ANSWER["5"])
                    else:
                        print(ANSWER["6"])
    return inner


def input_error(func):
    def inner(*args, **kwargs):
        try:
            s_result = func(*args, **kwargs)
            return s_result
        except Exception as e:
            if e.__class__ == UnboundLocalError:
                if "name" in e.args[0]:
                    print(ANSWER["4"])
                elif "phone" in e.args[0]:
                    print(ANSWER["5"])
                else:
                    print(ANSWER["6"])
            elif e.__class__ == IndexError:
                return ANSWER["7"]
            elif e.__class__ == KeyError:
                return ANSWER["7"]
            elif e.__class__ == ValueError:
                return ANSWER["8"]
            else:
                print(ANSWER["6"])
    return inner


def command_hello() -> str:
    return ANSWER["1"]


@input_error
def command_add(phone, name) -> str:
    CONTACTS[name] = phone
    return ANSWER["2"]


@input_error
def command_change(phone, name) -> str:
    if CONTACTS[name]:
        CONTACTS[name] = CONTACTS[name] + " ," + phone
        return ANSWER["3"]
    else:
        return ANSWER["7"]


@input_error
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


PARSER_1 = {
    "add": command_add,
    "change": command_change,
    "phone": command_phone
}
PARSER_2 = {
    "hello": command_hello,
    "show all": command_show_all,
    "good bye": command_exit,
    "close": command_exit,
    "exit": command_exit
}


def command(input_command: str):
    if PARSER_1.get(input_command, False):
        return PARSER_1[input_command]
    else:
        return PARSER_2[input_command]()


@input_error_main
def main():
    PARSER = PARSER_1.copy()
    PARSER.update(PARSER_2)
    while True:
        s = input("Enter command:").lower()
        if s == ".":
            break
        itar_avel = False
        for k in PARSER.keys():
            if k in s:
                input_com = k
                pert_2_s = s.removeprefix(k).strip()
                itar_avel = True
                break
        if not itar_avel:
            print("Command undefined! Try again!")
            continue
        input_list = pert_2_s.split(" ")
        for i in input_list:
            if i.isalpha():
                name = i
                input_list.remove(name)
                phone = " ".join(input_list)
                break
        if (input_com == "add") or (input_com == "change"):
            result = command(input_com)(phone, name)
            del name, phone
        elif input_com == "phone":
            result = command(input_com)(name)
            del name
        else:
            result = command(input_com)
        print(result)


main()
