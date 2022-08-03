import keyword
from urllib import response
import requests
import json
from openpyxl import *

keyword= input("검색어 : ")
count = input('갯수 : ')

# url 입력
url = "https://www.juso.go.kr/addrlink/addrLinkApi.do?confmKey=U01TX0FVVEgyMDIwMDYwNDExMzEwOTEwOTgyODk=&currentPage=1&countPerPage="+count+"&keyword="+keyword+"&resultType=json"

# url 불러오기
response = requests.get(url)

# 데이터 값 출력해보기
contents = response.text

# 문자열을 json으로 변경
json_ob = json.loads(contents)
#print(json_ob)
#print(type(json_ob))

# 필요한 내용만 꺼내기
body = json_ob['results']['juso']
#print(body)

# for num in body:
#      print(num['roadAddr'])

# Workbook 객체생성
wb = Workbook()
# 기존 시트 삭제
del wb['Sheet']
# 새로운 시트 생성
ws = wb.create_sheet("해당 주소")
# 표 머리말 작성
ws.append(['전체 도로명주소','지번주소','행정구역코드','도로명코드','건물관리번호','상세건물명','건물명','시도명','시군구명','읍면동명','법정리명','도로명','건물본번','건물부번'])

for data in body:
    ws.append([data['roadAddr'],data['jibunAddr'],data['admCd'],data['rnMgtSn'],data['bdMgtSn'],data['detBdNmList'],data['bdNm'],data['siNm'],data['sggNm'],data['emdNm'],data['liNm'],data['rn'],data['buldMnnm'],data['buldSlno']])

# 파일 저장
wb.save('주소.xlsx')