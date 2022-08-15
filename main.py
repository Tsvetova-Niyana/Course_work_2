# импорт классов и функций
from player import Player
from utils import load_random_word


def main():
    # формирование переменной для расположения файла json со словами игры
    DATA_SOURCE = 'https://jsonkeeper.com/b/69AP'

    # получение у пользователя его имени
    name_user = (input("Введите имя игрока: "))
    # создание экземпляра класса Player с полученным от пользователя именем
    player = Player(name_user)
    # вызов функции load_random_word() для получения случайного слова
    word = load_random_word(DATA_SOURCE)

    # приветствие пользователя, вывод случайного слова, вывод условий игры
    print(f"Привет, {player.name_user}!")
    print(f"Составьте {word.count_subwords()} слов из слова {word.word.upper()}")
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите 'stop'")
    print("Поехали, ваше первое слово?")

    # формирование цикла: цикл закончится, когда количество угаданных слов будет равно количеству подслов
    while player.get_count_used_word() < word.count_subwords():
        # ввод ответа пользователя
        user_answer = input().strip().lower()

        # если слово 'stop' или 'стоп' - игра заканчивается
        if user_answer == 'stop' or user_answer == 'стоп':
            break
        # если слово менее 3 символов - выводится информация "слишком короткое слово"
        elif len(user_answer) < 3:
            print("слишком короткое слово")
        # если слово не проходит проверку на вхождение в подслова - выводится информация "неверно"
        elif not word.check_answer_user(user_answer):
            print("неверно")
        # если слово ранее использовалось - выводится информация "уже использовано"
        elif player.check_reuse_word(user_answer):
            print("уже использовано")
        # если слово корректное - выводится информация "верно", слово добавляется в список использованных слов
        else:
            player.add_used_list(user_answer)
            print("верно")

    # вывод результатов игры
    if player.get_count_used_word() == 1:
        print(f"Игра завершена, вы угадали {player.get_count_used_word()} слово!")
    elif 1 < player.get_count_used_word() < 5:
        print(f"Игра завершена, вы угадали {player.get_count_used_word()} слова!")
    else:
        print(f"Игра завершена, вы угадали {player.get_count_used_word()} слов!")


if __name__ == '__main__':
    main()
