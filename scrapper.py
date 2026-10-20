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

jobs = []

for li in lis:
    try:
        company = li.find("a", class_="cpname").text
        title = li.find("div", class_="cell_mid").find("a").text
        location = li.find("div", class_="cl_md").find_all("span")[0].text
        link = li.find("div", class_="cell_mid").find("a").get("href") #외부창 get
        #print(company)
        #print(title)
        #print(location)
        #print(link)

        job_data = {
            "company" : company,
            "title" : title,
            "location" : location,
            "link" : link
        }

        jobs.append(job_data)

    except:
        pass

print(jobs)
print(len(jobs))