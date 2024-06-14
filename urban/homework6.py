# 1
my_dict = {'David': 1988, 'Artur': 1987, 'Georgy': 1993}
print('Dict:', my_dict)
print('Existing value:', my_dict['David'])
print('Not existing value:', my_dict.get('Anton'))
my_dict['Misha'] = 1997
my_dict['Masha'] = 2000
a = my_dict.pop('Artur')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

# 2
my_set = {1, 'string', 3, 4, (1, 2, 3), 5, 6, 'string', 1, 2, 3, (1, 2, 3), 4, 5}
print('Set:', my_set)
my_set.update([7, 9])
my_set.remove((1, 2, 3))
print('Modified set:', my_set)
