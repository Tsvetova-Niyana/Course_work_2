class Player:
    # инициализация класса Player
    def __init__(self, name_user):
        self.name_user = name_user
        self.words_used_list = []

    # формирование представления для класса Player
    def __repr__(self):
        return f"Игрок - {self.name_user} назвал {', '.join(self.words_used_list)}"

    # получение количества использованных слов (возвращает int);
    def get_count_used_word(self):
        return len(self.words_used_list)

    # добавление слова в использованные слова (ничего не возвращает)
    def add_used_list(self, user_answer):
        self.words_used_list.append(user_answer)

    # проверка использования данного слова до этого (возвращает bool)
    def check_reuse_word(self, user_answer):
        if user_answer in self.words_used_list:
            return True
