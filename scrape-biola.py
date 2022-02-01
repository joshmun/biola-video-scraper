from bs4 import BeautifulSoup

# update this path accordingly
with open("./html/module4.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

allIframes = soup.find_all('iframe')

def exclude_iframe_error(tag):
    return tag.name == 'iframe' and not tag.has_attr('title')

iframes = soup.find_all(exclude_iframe_error)
srcHtml = list(map(lambda frame: frame['src'], iframes))

def get_video_url(srcHtmlPath):
    with open(f"./html/{srcHtmlPath}") as fp:
        soup = BeautifulSoup(fp, "html.parser")
    
    return soup.find('video')['src']

videoLinks = list(map(get_video_url, srcHtml))

file = open('vidlinks.txt', 'r+')
file.truncate(0)
for link in videoLinks:
    file.write(f"{link}\n")
file.close()
