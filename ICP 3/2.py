from bs4 import BeautifulSoup
import requests

def wiki_scrap():
    html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")   #Passing url to get the content of html
    soup = BeautifulSoup(html.content, "html.parser")                        #Parsing through soup parser
    print("Title of the web page is ",soup.title.string)

#returning the results with href and printing out with it
    for r in soup.find_all('a'):
        print(r.get('href'))
wiki_scrap()