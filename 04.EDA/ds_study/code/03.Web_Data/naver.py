import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://finance.naver.com/marketindex/"

### requests 모듈을 이용해 url 요청
response = requests.get(url)

### 데이터 확인
soup = BeautifulSoup(response.text, "html.parser")
exchangeList = soup.select("#exchangeList > li")


### 데이터 수집
exchange_data = []
baseUrl = "https://finance.naver.com"

for i in exchangeList :
    data = {
        "title" : i.select_one(".h_lst").text,
        "exchange" : i.select_one(".value").text,
        "change" : i.select_one(".change").text,
        "updown" : i.select_one("div.head_info.point_dn > .blind").text,
        "link" : baseUrl + i.select_one("a")["href"]
    }
    exchange_data.append(data)


### 데이터 프레임 및 엑셀로 변환
df = pd.DataFrame(exchange_data)
df.to_excel("../../data/03.Web_Data/naverfinance.xlsx")