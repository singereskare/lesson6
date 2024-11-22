immutable_var = [1, 2, 'a', 'b', "word"]
print(immutable_var)

#immutable_var[0] = "number"
#Изменить элементы кортежа immutable_var нельзя, потому что кортеж — это
#неизменяемая структура данных в Python.

mutable_list = [1, 2, 'a', 'b', "Modified"]
mutable_list[2] = "letter"
mutable_list[4] = "word"
print(mutable_list)