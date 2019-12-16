"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""
def main(string1, string2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if type(string1) != str or type(string2) != str: #isinstance(string1, str) and isinstance(string2, str):
        return 0
    elif string1 == string2:
        return 1
    elif string1 != string2 and len(string1) > len(string2) and string2 != 'learn':
        return 2
    elif string1 != string2 and string2 == 'learn':
        return 3
    else:
        return 'No such case'

print(main(666, 'test')) #0
print(main(666, 777)) #0
print(main('test', 777)) #0

print(main('apple', 'orange')) #'No such case'
print(main('orange', 'apple')) #2
print(main('orange', 'learn')) #3