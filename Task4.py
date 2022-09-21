alphabet = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
while True:
    print('Введите Ш чтобы зашифровать сообщение, Р чтобы расшифровать и В чтобы выйти')
    menu = input('>>> ').lower()
    if menu == 'в':
        break
    elif not (menu == 'ш' or menu == 'р'):
        continue
    
    if menu == 'ш':
        output = ''
        message = input('Введите строку: ').lower()
        key = int(input('Введите ключ: '))
    if menu == 'р':
        message = output
        output = ''
        key *= -1
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            new_key = (t + key) % len(alphabet)
            output += alphabet[new_key]
        else:
            output += letter
    print('Результат: ' + output)