import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.findAll(name="a", class_="titlelink")
article_title_list = []
article_link_list = []
for article in articles:
    article_title_list.append(article.get_text())
    article_link_list.append(article.get("href"))

upvotes = soup.findAll(name="span", class_="score")
upvote_num_list = [int(upvote.get_text().split()[0]) for upvote in upvotes]

max_value = max(upvote_num_list)
max_index = upvote_num_list.index(max_value)

print(article_title_list[max_index])
print(article_link_list[max_index])
print(upvote_num_list.index(max(upvote_num_list)))


# PRACTICE
# with open("website.html") as file:
#     text = file.read()
#
# soup = BeautifulSoup(text, "html.parser")
#
# title = soup.title
# web_url = soup.select("p a")
# first_heading = soup.h3
# headings = soup.findAll(class_="heading")
# print(first_heading)
