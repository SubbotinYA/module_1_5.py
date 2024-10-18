#Задайте переменные разных типов данных:
#Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = 1, [2], 'a', True
#Выполните операции вывода кортежа immutable_var на экран.
print(immutable_var)

#Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#immutable_var[0]=2
print(immutable_var)
#TypeError: 'tuple' object does not support item assignment

#Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list=[11,22,33, 'a', False]
#Измените элементы списка mutable_list.
mutable_list[0]=0
mutable_list.insert(2,55)
#Выведите на экран измененный список mutable_list.
mutable_list.remove(22)
print(mutable_list)



