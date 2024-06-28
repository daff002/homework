def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(55)
print_params(55, 'текст')
print_params(55, 'текст', False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [11, 'string', False]
values_dict = {'a': 2, 'b': 'example', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
