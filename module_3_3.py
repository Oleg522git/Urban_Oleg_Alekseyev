def print_params(a=1, b ='строка', c =True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

value_list = [13, 'asdf', True]
value_dict = {'a': 1, 'b': 'строка' , 'c': False }
print_params(*value_list)
print_params(**value_dict)

values_list_2 = ['wert', ['q', 45]]
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)