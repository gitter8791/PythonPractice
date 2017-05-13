#Use BSoup and request to ecode webpage

from bs4 import BeautifulSoup
import requests


#html class for headlines is class="story-heading"
        #page: https://www.nytimes.com/

url = 'https://www.nytimes.com/'
urlR = requests.get(url)
r_html = urlR.text

soup = BeautifulSoup(r_html, "html.parser")
#titles = soup.findAll('h2', {'class': 'story-heading'})
titles = soup.findAll(class_="story-heading")


for title in titles:
    if title.findAll("a"):
        # .strip() removes leading/trailing whitespace
        print(title.a.text.strip())
    else:
        print(title.text)

#print (titles)
