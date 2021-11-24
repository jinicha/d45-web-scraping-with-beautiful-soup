import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.findAll(name="h3", class_="title")
title_list = [title.get_text() for title in titles]

# print(title_list)
