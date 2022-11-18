import requests
from bs4 import BeautifulSoup

def scrapping_indeed (url):
    r_indeed = requests.get (url)
    html_indeed = r_indeed.text
    soup = BeautifulSoup (html_indeed, 'html.parser')
    cards = soup.find_all ('div', class_="result")
    jobs = []
    for card in cards:
        job = {
            'title': card.find('a').find('span').get('title'),
            'company': card.find('span', class_='companyName').get_text(),
            'location': card.find('div', class_='companyLocation').string,
            'how_old': card.find('span', class_='date').get_text(),
            'link': f"https://br.indeed.com{card.find('a').get('href')}"
        }
        jobs.append(job)
    return jobs

print (scrapping_indeed("https://br.indeed.com/empregos+de+python"))