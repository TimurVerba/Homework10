from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Phone(Field):
    pass


class Name(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []

        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone) -> None:
        self.phones.append(phone)

    def remove_phone(self, phone: Phone) -> None:
        for already_existing_phones in self.phones:
            if phone.value == already_existing_phones:
                self.phones.remove(already_existing_phones)
                break

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find_record(self, value):
        for record in self.data.values():
            if value == record.name.value:
                return record
            for phone in record.phones:
                if value == phone.value:
                    return record
        return None


if __name__ == '__main__':
    name = Name('Eva')
    phone = Phone('380996602558')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Eva'], Record)
    assert isinstance(ab['Eva'].name, Name)
    assert isinstance(ab['Eva'].phones, list)
    assert isinstance(ab['Eva'].phones[0], Phone)
    assert ab['Eva'].phones[0].value == '380996602558'
    found_record = ab.find_record('380996602558')
    assert found_record is rec
    print('Done')
