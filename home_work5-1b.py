documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def move_units(directories_dict, document_number, place):
    directories_copy = directories_dict.copy()
    for i in directories_copy:
        if document_number in directories_copy[i]:
            move_document = directories_dict[i].pop(directories_dict[i].index(document_number))
            directories_dict.setdefault(place, [])
            directories_dict[place].append(move_document)
            return directories_dict
    print('Документ c номером {} не найден'.format(document_number))


def del_units(documents_list, directories_dict, document_number):
    documents_list_copy = documents_list.copy()
    for i in range(len(documents_list_copy)):
        if document_number in documents_list_copy[i]['number']:
            documents_list.pop(i)
    for k in directories_dict:
        if document_number in directories_dict[k]:
            directories_dict[k].pop(directories_dict[k].index(document_number))
            return directories_dict, documents_list
    print('Документ c номером {} не найден'.format(document_number))


def find_people(data, document_number):
    for i in data:
        if i['number'] == document_number:
            return i['name']


def full_documents_list(data):
    for i in data:
        print(i['type'], '"' + (i['number']) + '"', '"' + (i['name']) + '"')
    return


def storage_place(data, document_number):
    for i in data:
        if document_number in data[i]:
            return i


def add_unit(documents_list, directories_dict):
    user_input_type = input('Введите вид документа: ')
    user_input_number = input('Введите номер документа: ')
    user_input_name = input('Введите имя владельца: ')
    user_input_storage_place = input('Введите номер полки для хранения документа: ')
    documents_list.append({"type": user_input_type, 'number': user_input_number, 'name': user_input_name})
    directories_dict.setdefault(user_input_storage_place, [])
    directories_dict[user_input_storage_place].append(user_input_number)
    return documents_list, directories_dict


# В функции объеденил 'add'  и 'add shelf' ибо зачем нам создавать новую полку если мы не собираемся туда ничего класть.


def main():
    while True:
        user_input = input(
            '\nВведите команду:\np - чтобы найти человека по номеру документа\n'
            'l - чтобы вывести весь список\n'
            's - чтобы найти место хранения по номеру документа\n'
            'a - чтобы добавить новый документ\n'
            'd - чтобы удалить документ из списка и из перечня полок\n'
            'm - чтобы переместить документ на другую полку')
        if user_input.lower() == 'p':
            doc_number_input = input('Введите номер документа: ')
            print('Документ с номером {} принадлежит: {}'.format(doc_number_input,
                                                                 find_people(documents, doc_number_input)))
        elif user_input.lower() == 'l':
            full_documents_list(documents)
        elif user_input.lower() == 's':
            doc_number_input = input('Введите номер документа: ')
            print('Документ хранится на полке номер: {}'.format(storage_place(directories, doc_number_input)))
        elif user_input.lower() == 'a':
            add_unit(documents, directories)
        elif user_input.lower() == 'd':
            doc_number_input = input('Введите номер документа который хотите удалить: ')
            del_units(documents, directories, doc_number_input)
        elif user_input.lower() == 'm':
            doc_number_input = input('Введите номер документа: ')
            place_input = input('Введи номер полку на которую хотите переложить документ: ')
            move_units(directories, doc_number_input, place_input)


main()
