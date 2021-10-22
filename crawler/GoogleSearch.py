from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
import requests


def googleSearch(option:str = "TISTORY", num:int = 100):

    link_list = []
    request_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
    baseUrl = 'https://www.google.com/search?q='
    plusUrl = input('무엇을 검색할까요? :')
    url = baseUrl + quote_plus(plusUrl)
    start = 0


    for i in range(num):
        req_url = url + "&start=" + str(start)
        response = requests.get(req_url, headers=request_headers)
        html = response.text
        print("!@#!@# html : ", html)
        soup = BeautifulSoup(html, "html.parser")

        v = soup.select('.yuRUbf')

        for i in v:
            link_list.append(i.a.attrs['href'])

        start += 10

        time.sleep(2)

    wp_link = []
    t_link = []

    print("!@#!@# links : ", link_list)

    cnt = 0

    for link in link_list:
        try:
            response = requests.get(link, timeout=15)
            src = response.text
            if "tt_article_useless_p_margin" in src:
                t_link.append(link)

            elif "wp-content" in src:
                wp_link.append(link)

            cnt += 1
            print("!! cnt : ", cnt)
        except:
            pass

    print("!@#!@# t = ", len(t_link))
    print("!@#!@# wp = ", len(wp_link))


if __name__ == "__main__":
    googleSearch()