"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
rating = [{'school_class': '1a', 'scores': [3,4,4,5,2]}, 
            {'school_class': '2a', 'scores': [3,4,4,5,5]}, 
            {'school_class': '3a', 'scores': [5,4,4,5,4]},
            {'school_class': '4a', 'scores': [3,4,3,5,3]},
            {'school_class': '5a', 'scores': [5,4,5,5,4]},
            {'school_class': '6a', 'scores': [3,4,3,5,2]},
            {'school_class': '7a', 'scores': [3,4,4,5,3]},
            {'school_class': '8a', 'scores': [4,4,5,5,4]},
            {'school_class': '9a', 'scores': [4,4,4,5,5]}]

def main(array):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    scores_sum = 0
    scores_sum_class = 0
    for id_dict in array[0:len(array)]:
        for score in id_dict['scores']:
            scores_sum += score
            scores_sum_class += score
        scores_avg_class = scores_sum_class / len(id_dict['scores'])
        print(f"Средний балл по {id_dict['school_class']} классу: {scores_avg_class}")
        scores_sum_class = 0
    scores_avg = scores_sum / len(array)
    return f"Средний балл по школе: {scores_avg}"

print(main(rating))
    