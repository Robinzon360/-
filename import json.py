from json import dump

cat = {'cat': 'Сугроб'}
employee = {'employee': ('Петя', 'Foxford')}

with open("data.json", 'w') as file:
    dump([cat, employee], file, ensure_ascii=False)
