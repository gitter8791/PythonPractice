#Ojective is to print on one sheet text from:
#http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture

from bs4 import BeautifulSoup
import requests

sURL = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
sURL_req = requests.get(sURL)
soup_URL = BeautifulSoup(sURL_req.text, "html.parser")

text_URL = soup_URL.find_all('section', {"class:", "content-section"})

for elem in text_URL:
  print(elem.text)