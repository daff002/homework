grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = tuple(sorted(students))  # сортируем students по алфавиту
averages = [sum(sublist) / len(sublist) for sublist in grades]  # получаем среднее арифметическое для grades
average_score = dict(zip(sorted_students, averages))  # создаем словарь из students и averages
print(average_score)
