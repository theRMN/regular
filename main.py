import csv
import re

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)

l_dict = {}

for i in contacts_list[1:]:
    fio = re.findall(r'(\w+)', ' '.join(i[:3]))
    fio = fio[:2]
    if tuple(fio) not in l_dict.keys():
        l_dict[tuple(fio)] = i
    else:
        l_dict[tuple(fio)] = i + l_dict[tuple(fio)]

prom_contacts_list = [contacts_list[0]]
new_contacts_list = []

for i in l_dict.values():
    patter_1 = re.compile('([А-ЯЁ][а-яА-ЯёЁ]+[цвхинна])(\W?)([А-ЯЁ][а-яА-ЯёЁ]+)'
                          '(\W?)([А-ЯЁ][а-яА-ЯёЁ]+[вична])(\W+)([а-яА-ЯёЁ]+)'
                          '(\W{0,2})([–\D\s]*)(\,*)?((\+7|8)?(\s*)(\()(\d+)(\))(\s*)(\d+)([-\s*])'
                          '(\d+)([-\s*])(\d+)(\W)|(\+7|8)?(\s*)(\d+)(-)(\d+)(-)(\d{2})(\d{2})(\W)|(\+7|8)?'
                          '(\d{3})(\d{3})(\d{2})(\d{2})(\W))((\()?(доб.)(\W+)'
                          '(\d{4})(\))?(\W*))?([.a-zA-Z\d+]+@[a-zA-Z.]+)?')

    i = ' '.join(i)
    new = patter_1.sub(r'\1,\3,\5,\7,\9,+7(\15\26\34)\18\28\35-\20\30\36-\22\31\37 \41\43,\46', i).split(',')
    prom_contacts_list.append(new)

for i in prom_contacts_list:
    patter_2 = re.compile('(^(\w)+\s\w+\s+)([.a-zA-Z\d+]+@[a-zA-Z.]+)'
                          '(\s)([\w\s\d\W]+)|((\s+)Мартиняхин(\s)([\s\w]*))')

    i = ', '.join(i)
    new = patter_2.sub(r'\5\3', i).split(',')
    new_contacts_list.append(new)
    print(new)

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
