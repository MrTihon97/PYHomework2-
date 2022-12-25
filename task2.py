# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# from random import randint

# arr =[randint(0,10) for i in range(randint(3,5))]
# sum = []
# middle = len(arr)//2 + len(arr)%2
# for i in range(middle):
#         sum.append(arr[i] * arr[len(arr) - i - 1])
# print(arr, '=>', (sum))


arr = [2, 3, 4, 5, 6]
sum = []
middle = len(arr)//2 + len(arr)%2
for i in range(middle):
        sum.append(arr[i] * arr[len(arr) - i - 1])
print(arr, '=>', (sum))


