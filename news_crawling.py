from bs4 import BeautifulSoup
from urllib import request

file = open("news_crawling.txt", "w", encoding= 'utf-8' )
url = 'https://news.daum.net'
result = request.urlopen(url)
soup = BeautifulSoup(result, 'html.parser')
lst = soup.select("strong.tit_g")
# print(lst)

for l in lst :
    a = l.select_one("a")
    file.write("Link : " + a.get('href')+"\n")
    title = a.string
    file.write("Title : " + title+"\n")

file.close()

# txt 파일까지는 생성이 되는데.. pyinstaller 로 실행파일(exe) 생성이 안됨 ㅠㅠ
'''
Syntax error in C:\Users\dltmf\PycharmProjects\python-repository\news_crawling.txt
  File "C:\Users\dltmf\PycharmProjects\python-repository\news_crawling.txt", line 1
     링크 - [https://v.daum.net/v/20220209213603584]
                ^
 SyntaxError: invalid syntax
'''
