# 1
example = 'Топинамбурsasas'

# 2
print(example[0])

# 3
print(example[-1])

# 4 тут все неоднозначно, если мы знаем значение переменной example, то решение такое
print(example[5:])

# если значение переменой всегда разное, то нужно определить четное или нечетное количество символов в строке

if len(example) % 2 == 0:                # если остаток от деления 0 (четное)
    start_index = len(example) // 2      # то делим на 2
else:                                    # в других случаях
    start_index = len(example) // 2 + 1  # делим на 2 и прибавляем 1

second_half = example[start_index:]

print(second_half)

# 5
print(example[::-1])

# 6
print(example[1::2])
