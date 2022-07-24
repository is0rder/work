Не знаю пока как реализовывается прокси сервер, копировать чужой код что бы просто сдать задание не вижу смысла, хочу писать только то что понимаю) 
поэтому прикладываю код в котором я распарсил страницу сайта и модифицировал текст согласно заданию



import requests
from bs4 import BeautifulSoup
# import re

url = 'https://news.ycombinator.com/item?id=13713480'
response = requests.get(url, proxies={'http': 'http://127.0.0.1:8000/item?id=13713480'})
soup = BeautifulSoup(response.text, 'lxml')
comment = soup.find('table', class_='comment-tree').text


mark = '.,'
el = '™'


def replace_elements(val):
    # стандартный список замены - удаление символов
    dict_translate = {x: '' for x in mark}
    # исключение для замены на другой символ
    # dict_translate['/'] = '_'
    # dict_translate['\\'] = '_'
    dict_translate = str.maketrans(dict_translate)
    return val.translate(val.maketrans(dict_translate))


def punctuation_check(elem):
    if elem[-1] in mark:
        elem = elem[:-1] + el + elem[-1]
    else:
        elem += el
    return elem


def text_modification(comment):
    result = []
    for comm in comment.split(' '):
        if len(replace_elements(comm)) == 6 and replace_elements(comm).isalpha():
            result.append(punctuation_check(comm))
        else:
            result.append(comm)
    return ' '.join(result)


print(text_modification(comment))
