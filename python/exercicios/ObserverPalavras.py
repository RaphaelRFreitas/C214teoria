# Classe Observável
class PhraseObservable:
    def __init__(self):
        self.observers = []
        self.phrase = ""

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_phrase(self, phrase):
        self.phrase = phrase
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.phrase)


# Classe Observadora Base
class PhraseObserver:
    def update(self, phrase):
        pass


# Observador que conta todas as palavras
class AllWordsCounter(PhraseObserver):
    def update(self, phrase):
        word_list = phrase.split()
        word_count = len(word_list)
        print("Contagem de todas as palavras:", word_count)


# Observador que conta palavras com quantidade par de caracteres
class EvenLengthWordsCounter(PhraseObserver):
    def update(self, phrase):
        word_list = phrase.split()
        even_length_words = [word for word in word_list if len(word) % 2 == 0]
        even_length_words_count = len(even_length_words)
        print("Contagem de palavras com quantidade par de caracteres:", even_length_words_count)


# Observador que conta palavras iniciadas com maiúsculas
class CapitalizedWordsCounter(PhraseObserver):
    def update(self, phrase):
        word_list = phrase.split()
        capitalized_words = [word for word in word_list if word[0].isupper()]
        capitalized_words_count = len(capitalized_words)
        print("Contagem de palavras iniciadas com maiúsculas:", capitalized_words_count)


# Função para iniciar o aplicativo
def run_app():
    observable = PhraseObservable()
    all_words_counter = AllWordsCounter()
    even_length_words_counter = EvenLengthWordsCounter()
    capitalized_words_counter = CapitalizedWordsCounter()

    # Para validar o funcionamento é só comentar uma das adicões abaixo
    observable.add_observer(all_words_counter)
    observable.add_observer(even_length_words_counter)
    observable.add_observer(capitalized_words_counter)

    phrase = input("Digite uma frase: ")
    observable.set_phrase(phrase)


# Executar o aplicativo
run_app()
