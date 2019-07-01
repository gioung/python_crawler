import ssl
import sys
from urllib.request import Request, urlopen
from datetime import datetime


def crawling(url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn', encoding='utf-8', err=lambda e: print(f'{e} : {datetime.now()}', file=sys.stderr),
            proc1=lambda data: data,
            proc2=lambda data: data):


    try:
        # fetch
        # 접속할 서버의 url을 설정하고 http 연결을 위한 정보를 담고 있는 객체 (only info)
        request = Request(url)

        ssl._create_default_https_context = ssl._create_unverified_context
        # TCP/IP 연결 후 자원을 요청하는 코드
        response = urlopen(request)
        print('urlopen 실행 후')
        receive = response.read()
        print(f'{datetime.now()}: success for request [{url}]')
        results = proc2(proc1(receive.decode(encoding, errors='replace')))

        return results
    except Exception as e:
        err(e)



crawling()
