import random
import requests
from basic_word import BasicWord


def load_random_word(path):
    """ Формирование случайного слова. Функция:
        - получает список слов с внешнего ресурса,
        - выбирает случайное слово,
        - создает экземпляр класса "BasicWord",
        - возвращает созданный экземпляр.
    """
    response = requests.get(path)
    word_list = response.json()

    random.shuffle(word_list)
    word = word_list[0]

    words = BasicWord(word['word'], word['subwords'])
    return words
