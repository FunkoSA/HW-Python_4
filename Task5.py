# Perform Run–length encoding (RLE) data compression algorithm on string `str`
def encode(s):
	encoding = "" # stores output string
	i = 0
	while i < len(s):
		# count occurrences of character at index `i`
		count = 1
		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1
		# append current character and its count to the result
		encoding += str(count) + s[i]
		i = i + 1
	return encoding

def unzip(string):
    out_string =''
    multiplier = ''
    for e in string:
        if e.isdigit():
                multiplier +=e
        else:
            out_string+=e*int(multiplier)
            multiplier = ''
    return out_string

with open('Python/HW-PY_4/file_5.1.txt','w') as f:
    f.write ('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool') #Подготовка файла для обработки

while True:
    print('Для вывода на экран выберите Э \n Для вывода в файл выберите Ф \n Для распаковки выберите Р \n Для выхода выберите В')
    menu = input('>>> ').lower()
    if menu == 'в':
        break
    elif not (menu == 'э' or menu == 'ф' or menu == 'р'):
        continue
    if menu == 'э':
        with open('Python/HW-PY_4/file_5.1.txt','r') as file_in:
            data = file_in.read()
        print(f'Результат сжатия (RLE) {data}: \n {encode(data)} \n')
    elif menu == 'ф':
        with open('Python/HW-PY_4/file_5.1.txt','r') as file_in:
            data = file_in.read()
        with open('Python/HW-PY_4/file_5.2.txt','w') as file_out:
            file_out.write(encode(data))
        print(f'Результат сжатия (RLE) {data} записан в файл:file_5.2.txt \n Продолжим?\n')
    else:
        try:
            file_in =  open('Python/HW-PY_4/file_5.2.txt','r')
        except:
            print ('Отсутствует файл для распаковки!')
            break
        data = file_in.read()
        file_in.close()
        with open('Python/HW-PY_4/file_5.3.txt','w') as file_out:
            file_out.write(unzip(data))
        print(f'Результат сжатия (RLE) {data} записан в файл:file_5.3.txt \n Продолжим?\n')

    
