import requests
from bs4 import BeautifulSoup

keyword = "건축기사"
url = f"https://search.incruit.com/list/search.asp?col=all&src=gsw*www&kw={keyword}"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())

lis = soup.find_all("li", class_="c_col")
# print(lis)
# print(len(lis))

for li in lis:
    company = li.find("a", class_="cpname")
    print(company)