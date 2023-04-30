import requests
from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('main', class_='content')


list_article_title = article.findAll('a', class_='entry-title-link')
list_article_published = article.findAll('time', class_='entry-time')
list_article_author = article.findAll('span', class_='entry-author-name')
list_article_content = article.findAll('div', class_='entry-content')

article_title = [title.text for title in list_article_title]
article_published = [published.text for published in list_article_published]
article_author = [author.text for author in list_article_author]
article_content = [content.text for content in list_article_content]
# headline = article.h2.a.text

print(article_title)
print(article_published)
print(article_author)
print(article_content)
# print(article_title)

# for title in article_title:
#     print(title)

#print(article.prettify())
# print(headline)

# summary = article.find('div', class_='entry-content').p.text
# print(article.prettify())


