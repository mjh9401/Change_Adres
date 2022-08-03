import keyword
from pprint import pprint
from urllib import response
import requests
import pprint
import json
import openpyxl

keyword= input("검색어 : ")
count = input('갯수 : ')

# url 입력
url = "https://www.juso.go.kr/addrlink/addrLinkApi.do?confmKey=U01TX0FVVEgyMDIwMDYwNDExMzEwOTEwOTgyODk=&currentPage=1&countPerPage="+count+"&keyword="+keyword+"&resultType=json"

# url 불러오기
response = requests.get(url)

# 데이터 값 출력해보기
contents = response.text

# 데이터 결과값 예쁘게 출력해주는 코드
pp = pprint.PrettyPrinter(indent=4)
#print(pp.pprint(contents))

# 문자열을 json으로 변경
json_ob = json.loads(contents)
#print(json_ob)
#print(type(json_ob))

# 필요한 내용만 꺼내기
body = json_ob['results']['juso']
print(body)