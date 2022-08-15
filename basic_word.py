class BasicWord:
    # инициализация класса BasicWord
    def __init__(self, word, subwords):
        self.word = word
        self.subword = subwords

    # формирование представления для класса BasicWord
    def __repr__(self):
        return f"Слово {self.word} включает подслова: {', '.join(self.subword)}"

    # проверку введенного слова в списке допустимых подсло в (вернет bool)
    def check_answer_user(self, user_answer):
        if user_answer in self.subword:
            return True

    # подсчет количества подслов (вернет int)
    def count_subwords(self):
        count_subword = len(self.subword)
        return count_subword
