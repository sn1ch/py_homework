import datetime


class My_open:
    def __init__(self, file_path):
        self.file_path = file_path
        self.start_time = datetime.datetime.now()
        print(f'Начало рабомы: {self.start_time}')

    def __enter__(self):
        self.file = open(self.file_path, 'a')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.finish_time = datetime.datetime.now()
        print(f'Конец работы: {self.finish_time}')
        print(f'Время работы: {self.finish_time - self.start_time}')


def add_contact(name, telephone):
    with My_open('telephone_book.txt') as file:
        file.write(f'{name} {telephone} \n')
    return


def main():
    while True:
        input_name = input('Введите имя и фамилию контакта: ')
        input_telephone = input('Введите номер телефона: ')
        add_contact(input_name, input_telephone)


main()
