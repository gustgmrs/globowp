import pandas as pd
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


def get_news():
    url = 'https://www.globo.com/'

    # Pegando os elementos HTM
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Separando apenas as TAGs de Link
    news = soup.find_all('a')

    # Classes de Notícias
    target_class1 = 'post__title'
    target_class2 = 'post-multicontent__link--title__text'

    # Montando uma lista de listas de Notícias
    news_list = []
    for new in news:
        if (new.h2 != None) and (new.h2.get('class') != None):
            if target_class1 in new.h2.get('class'):
                link = new.get('href')
                title = new.h2.text
                lista = [title, link]
                news_list.append(lista)
            if target_class2 in new.h2.get('class'):
                link = new.get('href')
                title = new.h2.text
                lista = [title, link]
                news_list.append(lista)

    return news_list


def csv_generator():
    lista = get_news()

    # Gerando o DataFrame
    colunas = ['Título', 'Links']
    news_df = pd.DataFrame(lista, columns=colunas)

    # Gerando o CSV
    news_df.to_csv('news.csv', index=False)


csv_generator()
