import view
import model

def start():
    model.open_file()
    while True:
        select = view.menu()
        match select:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                view.print_contacts(model.phonebook)
            case 4:
                new = view.input_new_contact()
                model.add_contact(new)
            case 5:
                view.print_contacts(model.search_contact())
            case 6:
                model.edit_contact()
            case 7:
                model.remove_contact()
            case 8:
                model.exit_program(False)
                break
            case 9:
                model.exit_program(True)
                break
        print("░" * 100)