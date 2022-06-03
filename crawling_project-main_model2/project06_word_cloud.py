import pandas as pd  # 결과값을 데이터프레임 객체로 저장하기 위해 이용
from wordcloud import WordCloud
import matplotlib.pyplot as plt  # 그래프 그리기
from collections import Counter  # 데이터의 개수를 정리할 수 있는 모듈
from konlpy.tag import Kkma  # 형태소 분석기 호출
from konlpy.utils import pprint  # 유니코드 문자 출력

from selenium import webdriver  # 브라우저 제어


new = pd.read_csv('./crawling_data(2)/wadiz_data(2)_20220530.csv')  # 여기 주소값만 바꿔주세요!

# csv 파일 불러오기 (위치 임의 지정)

kkma = Kkma()
nouns_list = []  # nouns_list생성

for item in new['title'][:100]:  # [ ]안의 숫자에 따라 분석 단어 개수 변화
    sentence_list = kkma.sentences(item)
    for sentence in sentence_list:
        nouns = kkma.pos(sentence)  # sentence의 형태소 분석
        for pos in nouns:
            if pos[1] == 'NNG' or pos[1] == 'NNP':  # 일반 명사와 고유 명사일 경우
                nouns_list += [pos[0]]  # nouns_list에 추가

count = Counter(nouns_list)  # list 내 항목명과 항목별 개수


font_path = '‪C:\Windows\Fonts\HMKMRHD.TTF'  # 글꼴 : 휴먼둥근헤드라인체
wordcloud = WordCloud(width=600, height=600, font_path=font_path)
wordcloud = wordcloud.generate_from_frequencies(count)  # 단어 출현 빈도에 따라 크기 변화
array = wordcloud.to_array()
fig = plt.figure(figsize=(50, 50))
plt.imshow(array, interpolation="bilinear")
plt.show()  # word cloud 도출
