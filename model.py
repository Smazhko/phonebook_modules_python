import json
import view
import text

path = 'phones.json'

def open_file():
    global phonebook
    try:
        with open(path, 'r', encoding="UTF-8") as phonebook_file:
            phonebook = json.load(phonebook_file)
        view.print_message(text.successOpenFile)
    except:
        view.print_message(text.errorOpenFile)


def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as phonebook_file:
            json.dump(phonebook, phonebook_file, ensure_ascii=False)
        view.print_message(text.successSaveFile)
    except:
        view.print_message(text.errorSaveFile)
    

def search_contact(target = ''):
    result = {}
    requestWord = view.get_request_word(target)
    for i, contact in phonebook.items():
        if requestWord in ' '.join(list(contact.values())).lower():
            result[i] = contact
    if len(result) == 0:
        print(text.emptySearch)
        select = input(text.searchRepeat)
        if select == "+":
            return search_contact(target)
    return result


def add_contact(newContact: dict[str: str]):
    if len(phonebook) != 0:
        newID = max(list(map(int, phonebook.keys()))) + 1
    else:
        newID = 1
    phonebook.update({newID: newContact})
    view.print_message(text.successAddContact(newContact['name']))


def remove_contact():
    removeDict = search_contact(text.searchOptionRemove)
    if len(removeDict) != 0:
        view.print_contacts(removeDict)
        while True:
            removeContactID = view.get_ID(text.removeInput)
            print(removeContactID, type(removeContactID))
            if  removeContactID in removeDict.keys():
                contactToRemove = phonebook.pop(removeContactID)
                view.print_message(text.successRemoveContact(contactToRemove['name']))
                break
            else:
                print(text.emptyID)


def edit_contact():
    editDict = search_contact(text.searchOptionEdit)
    if len(editDict) != 0:
        view.print_contacts(editDict)
        while True:
            editContactID = view.get_ID(text.editInput)
            if  editContactID in editDict.keys():
                editContact = view.input_new_contact('edit')
                phonebook.update({editContactID: editContact})
                view.print_message(text.successEditContact(editContact['name']))
                break
            else:
                print(text.emptyID)


def exit_program(saveFlag: bool):
    if saveFlag:
        save_file()
    view.print_message(text.exitMessage)

