print('Домашнее задание 2.3.: Исключения. Группа PY-21. Подготовил Казаков Сергей.\n')
print('Задание №1.\n')


def polska():
    print('Добро пожаловать в программу Польский калькулятор!\n')

    calc_line = input(
        'Cначала введите действие: + -> сложение, - -> вычитание, * -> умножение, / -> деление, потом после введите 2 положительные цифры через пробел для расчета, пробел должен быть введен и перед первой цифрой после знака действия. ример правильного ввода: + 2 2. Если Вы в точности не исполните эти инструкции, программа остановится и ее надо будет перезапустить.\n\nВведите действие:\n')

    try:
        len(calc_line) == 5
        calc_list = calc_line.split()
        action_sign = calc_list.pop(0)
        calc_list_ints = [int(i) for i in calc_list]
    except TypeError:
        print(
            'Вы неправильно ввели условия для решения. Проверьте, правильно ли введены символы операций, цифровые символы, проставлены ли пробелы. Пример правильного ввода: + 2 2.')

    if action_sign == '+':
        print('Результат = {}'.format(sum(calc_list_ints)))
    elif action_sign == '-':
        print('Результат = {}'.format(calc_list_ints[0] - calc_list_ints[-1]))
    elif action_sign == '*':
        print('Результат = {}'.format(calc_list_ints[0] * calc_list_ints[-1]))
    elif action_sign == '/':
        try:
            print('Результат = {}'.format(calc_list_ints[0] / calc_list_ints[-1]))
        except ZeroDivisionError:
            print('Был введен 0. На ноль делить нельзя.')
            print('Результат = 0')
    else:
        print(
            'Вы неправильно ввели условия для решения. Проверьте, правильно ли проставлены пробелы. Пример правильного ввода: + 2 2.')


polska()

# !/usr/bin/python

print('\nЗадание №2.\n')


def doc_number():
    '''
    Функция обработки имени владельца документа и вызова его номера
    '''
    documents = [
        {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Пупкин'},
        {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
        {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
    ]

    name_input = input('Введите имя владельца документа: ')
    doc_shelf = list()
    found = False
    for document in documents:
        try:
            if name_input == document['name']:
                doc_shelf.append(document['number'])
                print(f'Номер документа: ', *doc_shelf)
                found = True
                break
            if not found:
                print(document['key'])
        except BaseException:
            print(f'Данные отсутствуют или такого документа в нашем хранилище нет.')


doc_number()