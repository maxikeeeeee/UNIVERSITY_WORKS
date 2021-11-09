a = []
n = int(input("Укажите размер массива:"))
print("Введите елементы массива")
for i in range(n):
    a.append(int(input()))
print("Массив:")
print(a)
answer = 1

print("Максимальный елемент:")
print(max(a))

import statistics
print("Среднее ар. массива: " + str(statistics.mean(a)))

print("Отрицательные елементы массива: " + str(list(reversed(list(filter(lambda x : x < 0, a))))))

