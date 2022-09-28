# Задача: Создать информационную систему позволяющую работать с сотрудниками некой
# компании \ студентами вуза \ учениками школы.
#
# https://docs.python.org/3/library/json.html
# https://docs.python.org/3/library/sqlite3.html
# https://docs-python.ru/standart-library/modul-sqlite3-python/

# # json_write.py
# import json
# from pprint import pprint
#
# data = {}
# data['employers'] = []
# data['employers'].append({
#     'name': 'Иванов',
#     'position': 'Директор',
#     'salary': 1000
# })
# data['employers'].append({
#     'name': 'Петров',
#     'position': 'Главный инженер',
#     'salary': 800
# })
# data['employers'].append({
#     'name': 'Сидоров',
#     'position': 'бухгалтер',
#     'salary': 800
# })
# # pprint(data)
# # print(data['employers'][1]['position'])
# with open('employers.json', 'w', encoding='utf-8') as outfile:
#     json.dump(data, outfile)
#
# # json_read.py
# import json
#
# with open('employers.json') as json_file:
#     data = json.load(json_file)
#     print(data)
#     for p in data['employers']:
#         print(f'Name: {p["name"]}')
#         print(f'position: {p["position"]}')
#         print(f'salary: {p["salary"]}')
#         print('')

import controller as c

c.main()

