from model import path

title = "Работа с телефонным справочником:"

mainMenu = ["открыть файл",
            "сохранить файл",
            "показать все контакты", 
            "добавить новый контакт",
            "найти контакт",
            "изменить контакт",
            "удалить контакт",
            "выйти без сохранения",
            "сохранить изменения и выйти"]

selectMenu        = "Выберите пункт меню... > "
newContactMessage = "Введите данные нового контакта"
inputNewContact   = {"name": "Имя контакта >> ", 
                     "phone": "Телефон      >> ", 
                     "comment": "Комментарий  >> "}
searchRemoveTitle = " ПОИСК ДЛЯ УДАЛЕНИЯ... "
searchMessage     = "Введите поисковый запрос >> "
searchRepeat      = "Повторить поиск ? (Введите \"+\", если ДА, и \"-\", если НЕТ) > "

removeInput   = "Введите ID контакта для УДАЛЕНИЯ"
editInput     = "Введите ID контакта для ИЗМЕНЕНИЯ"
editMessage   = "Введите новые данные контакта:"

searchOptionEdit   = "для редактирования"
searchOptionRemove = "для удаления"

errorOpenFile   = "( ! ) Ошибка открытия файла с телефонным справочником"
errorSaveFile   = "( ! ) Ошибка сохранения телефонного справочника"
errorSelectMenu = f"( ! ) Ошибка ввода (необходимо ввести цифры от 1 до {len(mainMenu)}). Попробуйте ещё раз."
errorEmptyList  = "( ! ) Список пуст. Выводить нечего."
errorInputID    = "( ! ) Пустого ID не бывает! "

emptySearch     = "( ! ) Ничего не найдено..."
emptyID         = "( ! ) Контакта с таким ID нет среди найденных"

successOpenFile = "(+) Телефонная книга успешно загружена"
successSaveFile = f"Телефонная книга успешно сохранена в файл {path}."

def successAddContact(name):
    return f"Контакт \"{name}\" успешно ДОБАВЛЕН."

def successRemoveContact(name):
    return f"Контакт \"{name}\" успешно УДАЛЁН."

def successEditContact(name):
    return f"Контакт \"{name}\" успешно ИЗМЕНЁН."

titleID      = "ID"
titleName    = "ИМЯ"
titleComment = "КОММЕНТАРИЙ" 
titlePhone   = "ТЕЛЕФОН"

exitMessage = "ВОТ и ВСЁ! Приходите ещё ^_^"