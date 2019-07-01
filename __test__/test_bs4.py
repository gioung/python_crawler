from bs4 import BeautifulSoup

html = '''<td class="title">
<div class="tit3" id="my-div">
<a href="/movie/bi/mi/basic.nhn?code=161967" title="기생충">기생충</a>
</div>
</td>'''


# 1. tag 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)
    # print(type(bs))

    # tag = bs.td
    # print(tag)
    # print(type(tag))

    # tag = bs.a
    # print(tag)
    # print(type(tag))
    #
    # tag = bs.td.div
    # print(tag)
    # print(type(tag))



# 2. attribute값 가져오기
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])

    tag = bs.div
    print(tag['id'])
    #에러

    tag = bs.div
    print(tag.attrs)


# 3. attribute로 태그 조회하기
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('td', attrs={'class': 'title'})
    # print(tag)
    # print(type(tag))

    tag = bs.find(attrs={'class': 'tit3'})
    print(tag)


if __name__ == '__main__':
    ex3()