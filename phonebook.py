# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1) Создать телефонный справочник:     +
# - открыть файл в режиме добавления данных (режим a) +
# 2) Добавить контакт:                  +
# - запросить информацию у пользователя +
# - подготовить нужный формат данных    +
# - открыть файл в режиме добавления данных (режим a)   +
# - добавить контакт в файл             +
# 3) Вывести данные из файла на экран:  +
#  - открыть файл в режиме чтения (r)   +
# - вывести информацию на экран         +
# 4) Поиск данных:
# - запросить вариант поиска            +
# - открыть файл в режиме чтения (r)    +
# - сохранить данные в переменную       +
# - осуществить поиск                   +
# - вывести информацию на экран         +
# 5) User-интерфейс:                    +
# - вывести варианты меню               +
# - получение запроса пользователя      +
# - реализация запроса пользователя     +
# - выход из программы                  +


def input_name():
    return input("Введите имя: => ")


def input_middlename():
    return input("Введите отчество: => ")


def input_surname():
    return input("Введите фамилию: => ")


def input_phone():
    return input("Введите номер телефона: => ")


def input_adress():
    return input("Введите адрес: => ")


def create_contact():
    surname = input_surname()
    name = input_name()
    middlename = input_middlename()
    phone = input_phone()
    adress = input_adress()

    return f"{surname} {name} {middlename} {phone} {adress}\n"


def add_contact(contact):
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(contact)


def print_phonebook():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        list_contacts = file.read().strip().split("\n")
        print("-" * 80)
        print("| № | ",
            "Фамилия".ljust(15),
            "Имя".ljust(15),
            "Отчество".ljust(15),
            "Телефон".ljust(15),
            "Город".ljust(15),
            sep="",
        )
        print("-" * 80)
        dev_list_contacts = [contact.split() for contact in list_contacts]
        for dev_l in dev_list_contacts:
            print("|", dev_list_contacts.index(dev_l) + 1, "|", end=" ")
            for el in dev_l:
                print(el.ljust(15), end='')
            print()
        
        # print(file.read())


def copy_contact():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        list_contacts = file.read().strip().split("\n")
    file_name = (
        input("Введите имя файла, куда будем копировать (например, book_phone) => ")
        .rstrip()
        .strip()
    )
    num_contact = int(input("Введите номер записи для копирования: => "))

    with open(f"{file_name}.txt", "a", encoding="UTF-8") as file:
        file.write(list_contacts[num_contact - 1])
        file.write("\n")
    print("Запись скопирована")


def search_contact():
    var_search = input(
        "Выберите вариант поиска:\n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчеству\n"
        "4. По номеру телефона\n"
        "5. По адресу\n"
        "Выберите пункт меню: => "
    )
    while var_search not in ("1", "2", "3", "4", "5"):
        print("Такого пункта не существует")
        print("-" * 40)
        var_search = input("Выберите пункт меню: => ")
        print("-" * 40)

    index_var = int(var_search)
    search = input("Поиск контакта: => ").lower()
    print("-" * 40)

    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        list_contacts = file.read().strip().split("\n")
        # print(list_contacts)
    for contact_str in list_contacts:
        contact_lst = contact_str.split()
        if search in contact_lst[index_var - 1].lower():
            print(contact_str)


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


interface()
