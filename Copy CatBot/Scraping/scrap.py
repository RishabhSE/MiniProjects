import requests
import html.parser
from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen

file=open('F:\\tdemo\\Desktop\\nm_code.txt','r')
page1=file.read()
file.close()

#Parsering the html code
soup=BeautifulSoup(page1,'html.parser')
#print(soup.prettify())

title=list()
links=list()
content=list()
subcontent=list()
for div in soup.find_all('div',class_='speechesItemLink left_class '):
	#content.append(div.get_text())

	for anch in div.find_all('a',class_='left_class'):
		title.append(anch.get_text())
		links.append(anch.get('href'))
#''.join(content)
'''
print(title)
print(len(title))
print(links)
print(len(links))
'''

#for url in links:
#file1=open('datas.csv','w')
for i in range(900,945):
        page = Request(links[i], headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(page).read()
	#page=requests.get(links[i])
        soup1=BeautifulSoup(web_byte,'html.parser')
        print(page)
        print(web_byte)
        print(soup1)
        #for article in soup1.find_all('article',class_='articleBody main_article_content'):
        article=soup1.find('article',class_='articleBody main_article_content')
        for para in article.find_all('p'):
                subcontent.append(para.get_text())
                #' '.join(subcontent)
        content.append(subcontent)
        #file1.write(subcontent)
#print(subcontent)
print(content)
