def command_hello(dictcontact_dict: dict, phone="", name="") -> str:
    s = "How can I help you?"
    return s


def command_add(dictcontact_dict: dict, phone="", name="") -> str:
    if name == "":
        return ""
    dictcontact_dict[name] = phone
    answer = "Contact save fine!"
    return answer


def command_change(dictcontact_dict: dict, phone="", name="") -> str:
    dictcontact_dict[name] = phone
    answer = "Contact update fine!"
    return answer


def command_phone(dictcontact_dict: dict, phone="", name="") -> str:
    print()
    answer = "Contact update fine!"
    return answer


def command_show_all(dictcontact_dict: dict, phone="", name="") -> str:
    pass


def command_exit(dictcontact_dict: dict, phone="", name="") -> str:
    return "Good bye!"
