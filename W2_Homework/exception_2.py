"""
Домашнее задание №1
Перепишите функцию discounted(price, discount, max_discount=20)
из урока про функции так, чтобы она перехватывала исключения, 
когда переданы некорректные аргументы (например, строки вместо чисел).
    
"""
def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
    except(ValueError):
        return "Переданы некорректные параметры"
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

    
print(discounted(2, 100))
print(discounted(2, 2))
print(discounted(3, "3"))
print(discounted("4", "4"))
print(discounted("five", 5))
print(discounted("six", "шесть"))