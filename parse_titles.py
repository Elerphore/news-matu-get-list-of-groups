from bs4 import BeautifulSoup
import unicodedata
import requests

urls = [
    "https://newlms.magtu.ru/mod/folder/view.php?id=1223698", # 1
    "https://newlms.magtu.ru/mod/folder/view.php?id=1223699", # 2
    "https://newlms.magtu.ru/mod/folder/view.php?id=1223700", # 3
    "https://newlms.magtu.ru/mod/folder/view.php?id=1223701"  #4
]

#open text file
text_file = open("/home/eler/groups.txt", "w")
 
def find_files(url):
    req = requests.get(url)
    req.encoding = 'UTF-8'
    soup = BeautifulSoup(req.text, 'html5lib')

    hrefs = []

    for a in soup.find_all("span", {"class": "fp-filename"}):
        txt = a.getText()
        if "19" in txt:
            hrefs.append(txt)

    return hrefs


for index, url in enumerate(urls, start = 1):
    list_of_links = find_files(url)

    if list_of_links:
        text_file.write(str(index).join(" \n"))
        for link in list_of_links:
            text_file.write(link.join(" \n"))

text_file.close()