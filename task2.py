# Видимо, нужно найти максимальную сумму ягод с трех,
# стоящих рядом кустов

list_1 = input('Введите через пробел количество ягод на кустах в порядке их роста на грядке: ').split()

max_sum = 0
summa = 0
for i in range(1, len(list_1)-1):
    summa = int(list_1[i-1])+int(list_1[i])+int(list_1[i+1])
    if summa > max_sum:
        max_sum = summa

print('Максимальное количество ягод: ', max_sum)
