"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

qa = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Как тебя зовут?": "Алиса"}

def ask_user():
    """
    Замените pass на ваш код
    """

    while True:
        try:
            user_say = input('Спроси меня о чем-нибудь: ')
            if user_say in qa.keys():
                rep_user = qa[user_say]
                print(rep_user)
                #break
            else:
                print("Попробуем в следующий раз")
                break
        except(KeyboardInterrupt):
            print("Пока!")
            break

if __name__ == "__main__":
    ask_user()