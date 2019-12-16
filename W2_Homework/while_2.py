"""
Домашнее задание №1
Цикл while: ask_user со словарём
* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:
    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
qa = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Как тебя зовут?": "Алиса"}

def ask_user():
    """
    Замените pass на ваш код
    """

    while True:
        user_say = input('Спроси меня о чем-нибудь: ')
        if user_say in qa.keys():
            rep_user = qa[user_say]
            print(rep_user)
            #break
        else:
            print("Попробуем в следующий раз")
            break
    
if __name__ == "__main__":
    ask_user()