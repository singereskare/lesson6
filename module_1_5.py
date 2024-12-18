# Создание неизменяемой переменной с кортежем
immutable_var = (1, 2, 'a', 'b')

# Как работает программа:
# Создается переменная immutable_var, которая содержит кортеж с несколькими элементами разных типов данных.

# Вывод кортежа на экран
print("Immutable tuple:", immutable_var)

# Как работает программа:
# Кортеж выводится на экран.

# Попытка изменить элементы кортежа
try:
    immutable_var[0] = 10  # Это вызовет ошибку, так как кортежи неизменяемы
except TypeError as e:
    print("Ошибка при попытке изменить элемент кортежа:", e)

# Как работает программа:
# Программа пытается изменить первый элемент кортежа, что приводит к ошибке TypeError, так как кортежи в Python неизменяемы. Ошибка перехватывается и выводится сообщение.

# Объяснение, почему нельзя изменить значения элементов кортежа
print("Кортежи в Python являются неизменяемыми объектами, поэтому после их создания их элементы нельзя изменять.")

# Как работает программа:
# Приводится объяснение, что кортежи являются неизменяемыми объектами, и их элементы нельзя изменять.

# Создание изменяемой переменной со списком
mutable_list = [1, 2, 'a', 'b']

# Как работает программа:
# Создается переменная mutable_list, которая содержит список с несколькими элементами.

# Изменение элементов списка
mutable_list[0] = 10  # Изменяем первый элемент
mutable_list.append('Modified')  # Добавляем новый элемент

# Как работает программа:
# Программа изменяет первый элемент списка и добавляет новый элемент с помощью метода append().

# Вывод измененного списка на экран
print("Mutable list:", mutable_list)

# Как работает программа:
# Измененный список выводится на экран.
