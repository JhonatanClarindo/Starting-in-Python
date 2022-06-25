from bs4 import BeautifulSoup
import requests

print("News about vulnerability search recent")
html_text = requests.get('https://thehackernews.com/search/label/Vulnerability').text
soup = BeautifulSoup(html_text, 'lxml')
news = soup.find_all('div', class_ = 'body-post clear')


for new in news:
    published_date = new.find('div', class_ = 'item-label').text
    title_new = new.find('h2', class_ = 'home-title').text
    moreInfo = new.find('div', class_ = 'home-desc').text
    link = new.a['href']
    
    print(f'''
    Title News: {title_new}

    Descrition: {moreInfo}

    Link for more info: {link}
    ''')

    print('')


