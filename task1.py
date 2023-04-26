# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

list_1 = []
list_2 = []
new_list = []
list_1 = (input('Введите через пробел занчения первого списка: ').split())
list_2 = (input('Введите через пробел занчения второго списка: ').split())

for i in list_1:
    if i in list_2 and i not in  new_list:
        new_list.append(i)

print(new_list)

min_index = 0
number_box = 0
for i in range (0, len(new_list)):
    for j in range (i, len(new_list)):
        if new_list[j] < new_list[i]:
            number_box = new_list[i]
            new_list[i] = new_list[j]
            new_list[j] = number_box
            
print('Распределенный: ',new_list)


