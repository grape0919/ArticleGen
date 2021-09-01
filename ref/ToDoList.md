- [**TASK**](#task)
  - [**Crawling**](#crawling)
    - [**1. google**](#1-google)
    - [**2. naver**](#2-naver)
      - [**Open API**](#open-api)
  - [**Doc Gen**](#doc-gen)
    - [**1. markovify**](#1-markovify)
- [문의 사항](#문의-사항)

# **TASK**

## **Crawling**

### **1. google**

</br>

### **2. naver**
#### **Open API**
1. 블로그 검색
   - https://developers.naver.com/docs/serviceapi/search/blog/blog.md
   - sample
   ```python 
    # 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
    # 네이버 검색 Open API 예제 - 블로그 검색
    import os
    import sys
    import urllib.request
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    encText = urllib.parse.quote("검색할 단어")
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
   ```
2. 게시물 title url 수집.

3. beautiful soup 으로 `se-text-paragraph` 찾아 article DB 저장

4. DB 구조

 |  index  | title | article |   keyword   |
 | :-----: | :---: | :-----: | :---------: |
 | INT(11) | TEXT  |  TEXT   | VARCHAR(50) |

## **Doc Gen**
### **1. markovify**
1. 현재 상태에서 POSTagger(Mecab 등) 사용하도록 변경
    - [github/markovify](https://github.com/jsvine/markovify#extending-markovifytext)



# 문의 사항
1. db 뭐쓰는지
2. 