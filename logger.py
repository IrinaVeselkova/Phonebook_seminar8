from date_create import *

def create_contact():
    surname = input_surname()
    name = input_name()
    middlename = input_middlename()
    phone = input_phone()
    adress = input_adress()

    return f"{name} {middlename} {surname}\t{phone}\t{adress}\n"


def add_contact(contact):
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(contact)


def print_phonebook():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        list_contacts = file.read().strip().split("\n")
        for contact in enumerate(list_contacts,1):
            print(*contact)
        # print(file.read())
        
def copy_contact():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        list_contacts = file.read().strip().split("\n")
    file_name=input('Введите имя файла, куда будем копировать (например, book_phone) => ').rstrip().strip()
    num_contact = int(input('Введите номер записи для копирования: => '))
        
    with open(f'{file_name}.txt', "a", encoding="UTF-8") as file:
        file.write(list_contacts[num_contact-1])
        file.write('\n')
    print('Запись скопирована')

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