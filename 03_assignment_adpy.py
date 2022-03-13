import requests
import bs4

# формат вывода - <дата> - <заголовок> - <ссылка>
# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Cookie': '_ym_uid=1608814327377895934; _ga=GA1.2.2048908147.1614428729; _ym_d=1631450667; hl=ru; fl=ru; habr_web_home=ARTICLES_LIST_ALL; feature_streaming_comments=true; visited_articles=110731; _gid=GA1.2.1701021973.1647076865; habr_web_home_feed=/all/; _ym_isad=2; _gat=1',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.31'
}
base_url = 'https://habr.com/'
url = base_url + 'ru/all/'

response = requests.get(url, headers=HEADERS)
response.raise_for_status()

text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
# print(articles)
for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item")
    hubs = [hub.text.strip().lower() for hub in hubs]
    data = article.find(class_="tm-article-snippet__datetime-published").find('time')['title'][:10]
    title = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").find('span').text
    href_end = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").find('a').get('href')
    href = url + href_end
    for keyword in KEYWORDS:
        if keyword in hubs or keyword + ' *' in hubs:
            meta_article = f'<{data}> - <{title}> - <{href}>'
            print(meta_article)


