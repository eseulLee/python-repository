# 카페 > 파이썬 > 외부모듈

import urllib.request

# 다운로드할 이미지 경로
url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"

# 저장할 파일 경로 및 이름
imgName = "C://Users/dltmf/Desktop/google.png"

# 파일 다운로드
# urlretrieve(URL, 저장할_파일_경로)
urllib.request.urlretrieve(url, imgName)

print('저장 완료!')

# 외부 모듈 다운받기!
# 다른 사람들이 만들어서 배포하는 모듈
# - 웹 서버 개발(Django, Flask)
# - 인공지능 개발(scikit-learn, tensorflow)
# - 데이터 분석(pandas, matplotlib)
# - 크롤러 개발(BeautifulSoup, requests)

# beautifulSoup4 install
# html 페이지 분석 후 내가 원하는 결과만 가져올 수 있음

from bs4 import BeautifulSoup

html = """
    <html>
        <head>
            <title>파이썬 웹 크롤링</title>
        </head>
        <body>
            <h1 id="title">안녕하세요</h1>
            <p id="name">정수아입니다</p>
        </body>
    </html>
"""

# html 태그 분석
# BeautifulSoup( [html 데이터] , '파서종류' )
soup = BeautifulSoup(html, 'html.parser')

# 데이터 위치 찾는 방법
h1 = soup.html.body.h1      # <h1>안녕하세요</h1>
p = soup.html.body.p        # <p>정수아입니다</p>

print("h1 : ", h1.string)
print("p : ", p.string)

# html 태그 구성
'''
# <시작태그>  </종료태그>
# <html>  </html>
# <head>  </head> , <body>  </body>   -> html 의 자식은 무조건 두개!

<h1>  : just h1 태그
<h1 id = "title" >  -> id : 속성, "title" : 속성값  : id가 title인 h1 태그 (좀 더 세분화, 구체화된 태그)
'''

# find() 함수
# 원하는 태그 찾아서 반환
# soup.find(찾아낼_태그)  <- 태그의 이름, 속성, 속성 값을 이용하여 찾을 수 있음
print()
title = soup.find(id = "title")
name = soup.find(id = "name")

print("title : ", title.string)
print("name : ", name.string)
print()

# find_all() 함수
# 특정 태그로 둘러싸인 요소를 다 찾아내 리스트로 반환
# soup.find_all(찾아낼_태그)

html1 = """
    <html>
    <head><title>find_all()</title></head>
    <body>
        <ul>
            <li>
                <a href="http://www.naver.com">네이버</a>
            </li>
            <li>
                <a href="http://www.google.com">구글</a>
            </li>
        </ul>
    </body>
    </html>
"""

soup1 = BeautifulSoup(html1, 'html.parser')
soup1Lst = soup1.find_all("a")

print(soup1Lst[0])
print(soup1Lst[1])

print('''
# 태그 안 텍스트(데이터) 추출''')
for a in soup1Lst :
    text = a.string
    print(text)

# <태그이름 속성="속성값"> 데이터 </태그이름>
# a.string -> 네이버(데이터) return
# 속성값 을 찾고싶다면?  a.attrs["속성이름"]

print('''
# 속성값 추출''')
for a in soup1Lst :
    href = a.attrs["href"]
    print(href)
print()

# BeautifulSoup을 이용한 데이터 추출

import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 웹사이트 분석 단계
'''
1. 웹사이트 접속 -> req.urlopen(웹사이트 주소) -> 결과 : HTML 데이터 
2. 웹사이트 분석 -> 데이터를 가져와야 함!
    BeautifulSoup(html 데이터, "파서종류-> html.parser")
3. 원하는 태그 찾기
    <title>기상청 육상 중기예보</title>
    find(태그이름)
'''
# 1. url 열기 (웹사이트 접속)
result = req.urlopen(url)

# 2. 데이터 분석하기
soup = BeautifulSoup(result, 'html.parser')

# 3. title 추출
title = soup.find('title').string

print('result - ', title)
print()
# CSS 선택자(selector)로 태그 찾기
'''
find_all() = select()
find() = select_one()
'''
# 기상청 날씨 정보 출력해보기
from urllib import request
# 1. urlopen() 함수로 기상청의 전국 날씨 가져오기
target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

# 2. BeautifulSoup을 사용해 웹 페이지 분석
# BeautifulSoup(HTML문자열, 'html.parser')
soup = BeautifulSoup(target, 'html.parser')

# 3. location 태그를 찾는다. + 규칙찾기   -> 규칙은 개발자인 내가 찾는다!
'''
<location>
    <city>서울</city>
    <wf>맑음</wf>
    <tmn>-1</tmn>
    <tmx>9</tmx>
</location>
'''
for l in soup.select("location") :
    # 내부의 city, wf, tmn, tmx 태그 찾아서 출력
    print('도시 : ', l.select_one("city").string)
    print('날씨 : ', l.select_one("wf").string)
    print('최저기온 : ', l.select_one("tmn").string)
    print('최고기온 : ', l.select_one("tmx").string)
    print('*' * 50)

# 뉴스 기사 크롤링
'''
출력형식
링크 : 
제목 :
<strong class="tit_g">
    <a href = "url">"data"</a>
'''

result = request.urlopen("https://news.daum.net/")
soup = BeautifulSoup(result, 'html.parser')
lst = soup.select("strong.tit_g")   # .tit_g : 클래스의 속성값이 tit_g 인 것
# print(lst)

for i in lst:
    a = i.select_one("a")
    print("링크 : ", a.attrs['href'])

    title = a.string
    print("제목 : " + title.strip())

# 강사님 sol
# 규칙 찾기
# 1. a > 너무 많아! > 부모 찾기 > <strong class="tit_g"> 태그 찾기
#   select(태그이름.속성값)
#   select("strong.tit_g")
# 2. 자식태그 찾기(<a href="링크주소">기사 제목</a>)
#   a.string  -> 기사 제목만 추출

# 파일입출력
'''
파일 : 텍스트 파일 / 바이너리 파일
파일처리 과정 : 파일 열기(open) > 파일 읽기(read) > 파일 쓰기(write) > 파일 닫기(close)
1. 파일 열기 - open() 함수
파일_객체(변수) = open("파일_경로", "모드")
                                     ㄴ모드    w : write (새로 쓰기 모드)
                                               a : append (뒤에 이어서 쓰기 모드)
                                               r : read (읽기 모드) 
2. 작업 (읽기, 쓰기)
파일_객체(변수).write("쓰고_싶은_내용")
write 안에서는 print 처럼 자동 엔터가 되지 않기 때문에 다 붙어서 나온다!
그래서 뒤에 '\n' 붙여줘야 함!

3. 파일 닫기 - close() 함수
파일_객체(변수).close()
'''
# 01. 파일 open
# file = open("basic.txt", "w")
# # 02. 내용 writing
# file.write("Hello Python Programming...!")
# # 03. file close
# file.close()

# 위의 실습 파일로 저장하기 (뉴스 스크래핑)
# file = open("news.txt", "w")
# url = "https://news.daum.net/"
# result = req.urlopen(url)
# soup = BeautifulSoup(result, "html.parser")
#
# news = soup.select("strong.tit_g")

file = open("news.txt", "w", encoding= 'utf-8')
url = "https://news.daum.net/"
result = request.urlopen(url)
soup = BeautifulSoup(result, 'html.parser')
lst = soup.select("strong.tit_g")
# print(lst)


for i in lst:
    a = i.select_one("a")
    # print("link : ", a.attrs['href'])
    file.write('link : ' + a.attrs['href'] + '\n')
    title = a.string
    # print("title : " + title.strip())
    file.write('title : ' + title.strip() + '\n')

file.close()


# 실행 파일로 만들기
# cmd 에 pyinstaller --onefile 파일명 입력

