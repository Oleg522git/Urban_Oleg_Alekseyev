#Практическое задание по теме: "Словари и множества"
#2. Работа со словарями:
my_dict = {'Olesya': 1997, 'Vahctanga': 1997, 'Mic': 2020, 'Laura': 2002}
print('Словарь:', my_dict)
print('Значение по ключу "Mic":' , my_dict['Mic'])
print('Значение по несуществующему ключу "Micle":' , my_dict.get('Micle'))
my_dict.update({'Serg': 1999,
                'Bon': 1998})
print('Значение по удалённому ключу "Mic":' , my_dict.pop('Mic'))
print('В словарь добавлены две новых пары и одна удалена' , my_dict)
print()

#3. Работа с множествами:
my_list = [0, 2, 3, 4, 5, 0, 2, 3, 4, 5, 'srting',
           True, (1,2,3), True, (3,2,1), (1,2,3)]
my_set = set(my_list)
print('Список:' , my_list)
print('Множество из списка:' , my_set)
my_set.update(('NEW_ELEMENT', 'ELEMENT=100'))
print('Добавлены два элемента в множество' , my_set)
my_set.discard((3, 2 , 1))
print('Удалён один элемент множества:' , my_set)