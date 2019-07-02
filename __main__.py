import os
import ssl
import sys
import time
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from collection import crawler


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# crawling_pelicana()를 확장해서 naver처럼 처리해보기
def crawling_pelicana():
    results = []
    for page in count(start=1):
        url = 'https://pelicana.co.kr/store/stroe_search.html?page={}&branch_name=&gu=&si='.format(page)
        html = crawler.crawling(url)

        bs = BeautifulSoup(html, 'lxml')
        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break


        for tag_tr in tags_tr:
            # print(list(tag_tr))
            strings = list(tag_tr.strings)
            # print(strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            t = (name, address) + tuple(sidogu)
            results.append(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/pelicana.csv', encoding='utf-8', mode='w', index=True)
    # print(table)

    for result in results:
         print(result)





def crawling_nene():

    results = []
    before_info = ''
    for page in count(start=48):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?page={}&ex_select=1&ex_select2=&IndexSword=&GUBUN=C'.format(page)
        html = crawler.crawling(url)

        bs = BeautifulSoup(html, 'lxml')
        tag_div = bs.find('div', attrs={'class': 'shopWrap'})
        # print(tag_div.__dict__)

        # print(tag_div.div.__dict__)

        tags_div_shopName = tag_div.findAll('div', attrs={'class': 'shopName'})
        tags_div_shopAdd = tag_div.findAll('div', attrs={'class': 'shopAdd'})
        print(len(list(tags_div_shopName)), len(list(tags_div_shopAdd)))
        tags_div_shopName = list(tags_div_shopName)
        tags_div_shopAdd = list(tags_div_shopAdd)


        # 끝 검출
        i = 0
        present_info = tags_div_shopName[0].text


        # print('present_info = ' + present_info)
        if present_info == before_info:
            break
        for num in range(0, len(tags_div_shopAdd)):
            # print('i = ' + str(i))
            if i == 0:
                before_info = tags_div_shopName[num].text
            strings = list(tags_div_shopName[num]) + list(tags_div_shopAdd[num])
            i += 1
            # name = strings[1]
            # address = strings[3]
            # sidogu = address.split()[:2]
            #
            # t = (name, address) + tuple(sidogu)
            results.append(tuple(strings))
    #
    # store
    table = pd.DataFrame(results, columns=['name', 'address'])
    table.to_csv('/root/crawling-results/nene.csv', encoding='utf-8', mode='w', index=True)
    print(table)

    # for result in results:
    #     print(result)


def crawling_kyochon():
    results = []
    for sido1 in range(1, 18):
        for sido2 in count(1):
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1={}&sido2={}'.format(sido1, sido2)
            html = crawler.crawling(url)

            # 끝 검출
            if html is None:
                break
            bs = BeautifulSoup(html, 'lxml')
            tag_ul = bs.find('ul', attrs={'class':'list'})
            tags_span = tag_ul.findAll('span', attrs={'class':'store_item'})


            for tag_span in tags_span:
                strings = list(tag_span.strings)
                name = strings[1]
                address = strings[3].strip()
                sidogu = address.split()[:2]

                t = (name, address) + tuple(sidogu)
                results.append(t)

        # store
        table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
        table.to_csv('__results__/kyochon.csv', encoding='utf-8', mode='w', index=True)

        for result in results:
             print(result)

def crawling_goobne():

    url = 'http://www.goobne.co.kr/store/search_store.jsp'
    wd = webdriver.Chrome('/cafe24/chromedriver/chromedriver.exe')
    wd.get(url)
    time.sleep(5)
    results = []
    for page in count(start=1):
        script = 'store.getList(%d)' % page
        wd.execute_script(script)
        print(f'{datetime.now()}: success for request [{script}]')
        time.sleep(3)

        # 실행결과 html(동적으로 렌더링 된 html) 가져오기
        html = wd.page_source

        # parsing with bs4
        bs = BeautifulSoup(html, 'lxml')
        tag_tbody = bs.find('tbody', attrs={'id': 'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        # detect last page
        if tags_tr[0].get('class') is None:
            break


        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            # print(strings)
            name = strings[1]
            address = strings[6]
            sidogu = address.split()[:2]

            results.append((name, address) + tuple(sidogu))

        # store
        table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
        table.to_csv('__results__/goobne.csv', encoding='utf-8', mode='w', index=True)


    wd.quit()
    for result in results:
        print(result)

if __name__ == '__main__':
    # pelicana
    #  crawling_pelicana()

    # nene 과제
    crawling_nene()

    # kychon
    # crawling_kyochon()

    # goobne
    # crawling_goobne()