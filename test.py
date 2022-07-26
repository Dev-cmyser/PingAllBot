import requests
from bs4 import BeautifulSoup





def link_nastya() -> str:
    
    url = 'https://vk.com/topic-106890704_48191467?offset=99'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    p = soup.find_all('a', class_='mr_label medias_link')
    d = ''
    for post in p:
        link = post.get('href')
        d = f'https://vk.com{link}'


        response = requests.get(d)

        soup = BeautifulSoup(response.text, 'lxml')
        page = soup.find('iframe', class_='iframe')
        url = page.get('src')
    return url
    
