''' Функции-редуцеры для списков: Напишите функцию-редуктор,
 которая принимает список строк и возвращает строку, 
состоящую из объединенных элементов списка через запятую.
 Например, для списка ["apple", "banana", "cherry"] 
 результат должен быть "apple, banana, cherry". '''

fruits = ["apple", "banana", "cherry"]

result = ", ".join(fruits)


print(result)
