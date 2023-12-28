from logger import *

def interface():
    with open("phonebook.txt", "a", encoding="UTF-8"):
        pass
    command = "-1"
    while command != "5":
        print("-" * 40)
        print(
            "Меню телефонной книги:\n"
            "1. Добавить контакт\n"
            "2. Показать контакты\n"
            "3. Поиск контакта\n"
            "4. Копировать контакт\n"
            "5. Закрыть телефонную книгу"
        )
        print("-" * 40)
        command = input("Выберите пункт меню: => ")
        print("-" * 40)
        while command not in ("1", "2", "3", "4", "5"):
            print("Такого пункта не существует")
            print("-" * 40)
            command = input("Выберите пункт меню: => ")
            print("-" * 40)

        match command:
            case "1":
                add_contact(create_contact())
            case "2":
                print_phonebook()
            case "3":
                search_contact()
            case "4":
                copy_contact()
            case "5":
                print("Хорошего дня!")