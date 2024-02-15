from translatepy import Translator

translator = Translator()

text = input("Введите текст на английском: " )

sentences = text.split(". ")

for sentence in sentences:
    print(sentence)
    print(translator.translate(sentence, 'ru'))