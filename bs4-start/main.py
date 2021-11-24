from bs4 import BeautifulSoup

with open("website.html") as file:
    text = file.read()

soup = BeautifulSoup(text, "html.parser")

title = soup.title
web_url = soup.select("p a")
first_heading = soup.h3
headings = soup.findAll(class_="heading")
print(first_heading)
