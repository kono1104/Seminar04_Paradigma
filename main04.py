''' Функция-редуктор: Напишите функцию-редуктор (или функцию свертки),
 которая принимает начальное значение и список чисел, 
а затем возвращает произведение всех чисел в списке. 
Используйте эту функцию для вычисления произведения чисел в списке. '''

from functools import reduce

a = [None, 1, 2, 3, 4]
print(reduce(lambda x, y: (x if x else 1) * (y if y else 1), a))
