import math
import text


def print_message(message): #┌─┐└─┘│
    print("┌" + "─" * (len(message) + 2) + "┐")
    print("│ " +        message         + " │")
    print("└" + "─" * (len(message) + 2) + "┘")


def menu() -> int:
    print(text.title)
    menuLength = len(text.mainMenu)
    columnSize = math.ceil(menuLength / 2)
    for index in range(0, columnSize):
        print((f"({index + 1}) {text.mainMenu[index]:<30}"), end="")
        if index + columnSize < menuLength:
            print(f"({index + 1 + columnSize}) {text.mainMenu[index + columnSize]}")
        else:
            print()
    while True:
        select = input("\n" + text.selectMenu)
        if select.isdigit() and 0 < int(select) < menuLength + 1:
            return int(select)
        print_message(text.errorSelectMenu)


def input_new_contact(flag = 'new'):
    newContact = {}
    if flag == 'new':
        print_message(text.newContactMessage)
    if flag == 'edit':
        print_message(text.editMessage)
    for field, message in text.inputNewContact.items():
        newContact[field]  = input(message).strip()
    return newContact

 
def print_contacts (data: dict[int, dict[str: str]]):#┌─┬─┐└─┴─┘│├─┼─┤
    if len(data) != 0:
        idField      = max([len(str(item)) for item in data.keys()]) + 2
        nameField    = max([len(item['name']) for item in data.values()]) #максимальная из списка длин полей NAME
        commentField = max([len(item['comment']) for item in data.values()])
        phoneField   = max([len(item['phone']) for item in data.values()])
        if nameField < len(text.titleID) + 1:
            nameField = len(text.titleID) + 2
        if commentField < len(text.titleComment):
            commentField = len(text.titleComment) + 2
        if phoneField < len(text.titlePhone):
            phoneField = len(text.titlePhone) + 2
        print("┌" + "─" * idField + "┬" + "─" * nameField + "┬" +"─" * commentField + "┬" + "─" * phoneField + "┐")
        print("│" + text.titleID.center(idField) + "│" + text.titleName.center(nameField) + "│" + text.titleComment.center(commentField) + "│" + text.titlePhone.center(phoneField) + "│")
        print("├" + "─" * idField + "┼" + "─" * nameField + "┼" +"─" * commentField + "┼" + "─" * phoneField + "┤")
        for i, contact in data.items():
            print(f"│{i:^{idField}}│{contact['name']:<{nameField}}│{contact['comment']:<{commentField}}│{contact['phone']:<{phoneField}}│")
        print("└" + "─" * idField + "┴" + "─" * nameField + "┴" +"─" * commentField + "┴" + "─" * phoneField + "┘")
    else:
        print(text.errorEmptyList)


def get_ID(message) -> str:
    while True:
        userInput = input(message + " >> ")
        if len(userInput) != 0:
            result = userInput
            return result
        else:
            print(text.errorInputID, end="")


def get_request_word(target = ''):
    print_message(f" ПОИСК {target.upper()}... ")
    return input("Введите поисковый запрос >> ").lower()

