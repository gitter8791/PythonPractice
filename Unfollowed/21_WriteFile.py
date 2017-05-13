#Use BSoup and request to ecode webpage. write to file

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

def strip_code(titles):
    stripped_titles = ""
    for title in titles:
        if title.findAll("a"):
            # .strip() removes leading/trailing whitespace
            stripped_titles += (title.a.text.strip())

        else:
            stripped_titles += (title.text)
    return stripped_titles

#print titles in a file
with open('FileToWrite21.txt', 'w') as open_file_variable:
    open_file_variable.write(strip_code(titles))