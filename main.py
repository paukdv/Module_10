from collections import UserDict

"""
Батьківський клас 'Field' для всіх полів, який буде містити логіку для всіх полів
"""
class Field:
    def __init__(self, value):
        self.value = value

"""
Клас 'Name', має обовʼязкове поле з імʼям
"""
class Name(Field):
    pass

"""
Клас 'Phone', необовʼязкове поле з телефоном та таких один запис (Record) може містити декілька
"""
class Phone(Field):
    pass

class Birthday(Field):
    pass      

"""
Клас 'Record' відповідає за логіку додавання, видалення, редагування необовʼязкових полів
та зберігання обовʼязкового поля 'Name' . Має необовʼязкові поля 'phone', 'birthday'
"""
class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.birthday = birthday
        if phone:
            self.phones = []
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                
"""
Клас 'AddressBook' наслідується від UserDict. Записи Record в AddressBook зберігаються як значення у словнику. 
Як ключі використовується значення Record.name.value. Record зберігає об'єкт Name в окремому атрибуті. 
"""
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record