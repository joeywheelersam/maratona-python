import requests
from bs4 import BeautifulSoup

url = "https://br.indeed.com/empregos-de-python?vjk=e584562a7bd71a63"
r = requests.get (url)
html = r.text
soup = BeautifulSoup(html, "html.parser")

cards = soup.find_all("div", class_="job_seen_beacon")
print (r.status_code)