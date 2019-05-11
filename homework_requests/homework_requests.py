import requests
from pprint import pprint

# API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
# создал свой ключ т.к. на выданов был превышен дневной лимит
# код ответ '{"code":404,"message":"Maximum daily translated text volume exceeded"}'
API_KEY = 'trnsl.1.1.20190511T180824Z.c92969a2f8aa0201.0b7285baa81111777e43e55c9b41c65eae007c1d'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(load, safe_as, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    with open(load, encoding='utf8') as file:
        text = file.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang)
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    # pprint(response.text)
    with open(safe_as, 'w', encoding='utf8') as file:
        file.write(''.join(json_['text']))
    return ''.join(json_['text'])


pprint(translate_it('files_requests/FR.txt', 'files_requests/FR-RU.txt', 'fr'))
pprint(translate_it('files_requests/DE.txt', 'files_requests/DE-RU.txt', 'de'))
pprint(translate_it('files_requests/ES.txt', 'files_requests/ES-RU.txt', 'es'))

requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))
