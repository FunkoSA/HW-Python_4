"""
## 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
Нужно перезаписать файл.
Пример:
* Ангела Меркель 5
* Андрей Валетов 5
* Фредди Меркури 3
* Анастасия Пономарева 4

Программа выдаст:
* АНГЕЛА МЕРКЕЛЬ 5
* АНДРЕЙ ВАЛЕТОВ 5
* Фредди Меркури 3
* Анастасия Пономарева 4
"""

f =  open('Python/HW-PY_4/file_3.1.txt','w')
data = f.write ('Ангела Меркель 5 \n')
data = f.write ('Андрей Валетов 5 \n')
data = f.write ('Фредди Меркури 3 \n')
data = f.write ('Анастасия Пономарева 4 \n')
f.close()

with open('Python/HW-PY_4/file_3.1.txt','r') as f:
    list = [line.strip() for line in f]


f = open('Python/HW-PY_4/file_3.1.txt','w')
for string in list:
    if "5" in string:
        f.write(string.upper() + '\n')
    else:
        f.write(string + '\n')
f.close()
