import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")

def translate(text):
    return translator.translate(text, dest="ru").text

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_ru = translate(word)
        word_definition = word_dict.get("word_definition")
        word_definition_ru = translate(word_definition)

        # Начинаем игру
        print(f"[Значение слова EN - {word_definition}]")
        print(f" Значение слова RU - {word_definition_ru}")
        user = input("Что это за слово (ru)? ")
        if user == word_ru:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word_ru} [{word}]")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? ('Enter' - да, 'н' - нет) ")
        if play_again == "н":
            print("Спасибо за игру!")
            break

word_game()