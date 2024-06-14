immutable_var = 1, 2, "a", "b", [100, 200]
print('Immutable tuple: ', immutable_var)

# immutable_var[0] = 5
# print(immutable_var)
# получаем ошибку, которая означает, что мы пытаемся изменить значение элемента внутри кортежа, а это невозможно
# неизменность кортежей обусловлена несколькими причинами:
# 1) для оптимизации скорости, тк кортежи занимают меньше места
# 2) для защиты от случайных изменений
# 3) для использования в роли хранилища

mutable_var = 1, 2, 'a', 'b', ['one', 'two']  # в данном примере в кортеже содержится список, который можно изменять
mutable_var[4][0] = 'three'
print('Nested list in tuple: ', mutable_var)

mutable_list = [1, 2, 'a', 'b', 'Unmodified']
mutable_list[4] = 'Modified'
print('Mutable list: ', mutable_list)
