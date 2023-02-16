import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


headers = Headers(os= 'win', browser='chrome')
HABR = 'https://habr.com'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

def get_page(url):
    return requests.get(url, headers=headers.generate())

def main():
    main_html = get_page('https://habr.com/ru/all/').text
    soup = BeautifulSoup(main_html, features="html5lib")
    articles = soup.find_all('article')
    for article in articles:
        article_pars = article.find_all(class_="tm-article-snippet")
        article_pars = " ".join([article_pars.text.strip() for article_pars in article_pars])
        time = article.find('time')['title']
        title_tag = article.find('h2')
        title = title_tag.find('span').text
        link = title_tag.find('a')['href']
        link = f'{HABR}{link}'
        for i in KEYWORDS:
            if i in article_pars:
                print(f" date: {time}, title: {title}, link: {link}")

if __name__ == '__main__':
    main()


