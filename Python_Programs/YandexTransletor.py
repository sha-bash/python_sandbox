import requests


url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20240213T115259Z.406daeb35df4e791.d7050188538058b3c8950c73c86845ce58884a59'

def translate_word(word):
    param = {'key': token, 'lang': 'ru-en', 'text': word, 'ui': 'ru'}
    trans_words = []
    response = requests.get(url=url, params=param).json()
    #data = response.json()
    if 'def' in response:
        translation = response['def'][0]['tr'][0]['text']
        return translation
    else:
        return 'Перевод не найден'
