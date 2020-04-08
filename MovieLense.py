import numpy as np
import pandas as pd

"""
1) 사용자별 평균평점을 산출하여 제일 높은 사용자와, 제일 낮은 사용자 id 출력

1. 최고평점 : 사용자ID (복수일 경우 사용자ID1, 사용자ID2, .....)
1. 최저평점 : 사용자ID (복수일 경우 사용자ID1, 사용자ID2, .....)

2. 영화별 평균평점을 산출하여 제일 높은 영화와 제일 낮은 영화의 제목을 출력

2. 최고평점 : Dracula: Dead and Loving It (1995)  (복수일 경우 , 로 이어서 출력)
2. 최저평점 : Now and Then (1995) (복수일 경우 , 로 이어서 출력)

3. 범죄스릴러(Crime, Thriller) 장르에서 최고 평점을 얻은 영화의 제목을 출력 :  
3. 범죄스릴러 장르 최고평점 : Kiss of Death (1995)
"""
#link.csv : movieId,imdbId,tmdbId
#movie.csv : movieId,title,genres
#rating_csv : userId,movieId,rating,timestamp
#tags.csv : userId,movieId,tag, timestamp

#1번
sample1 = pd.read_csv("./ml-latest-small/ratings.csv")
#print(sample1.head(10)) #상위 10개 데이터 보기
#print(sample1.tail(10)) #하위 10개 데이터 보기
#print(sample1.info()) #data-type 확인
#1번방식) userId를 불러오기 위해 index여부를 X 설정
sample1 = sample1.groupby('userId',as_index=False).mean()
#2번방식) reset_index() 사용
#sample1 = sample1.reset_index()
#print(sample1)


max_rating1 = sample1['rating'].max()
min_rating1 = sample1['rating'].min()
print("1-1)최고평점 : 사용자ID")
print(sample1[sample1['rating']==max_rating1]['userId'].values) #최고평점
print("1-2)최저평점 : 사용자ID")
print(sample1[sample1['rating']==min_rating1]['userId'].values) #최저평점
#sort방식을 사용할 수 있지만 안좋은 소스인듯보임.
#rank1 = sample1.sort_values(['rating'], ascending=False)['rating'].iloc[0]
#result = []

#2번
sample2 = pd.read_csv("./ml-latest-small/ratings.csv")
sample3 = pd.read_csv("./ml-latest-small/movies.csv")

#print(sample2.head(10)) #상위 10개 데이터 보기
#print(sample2.tail(10)) #하위 10개 데이터 보기
#print(sample2.info()) #data-type 확인
sample2 = sample2.groupby('movieId',as_index=False).mean() #movieId를 불러오기 위해 index여부를 X 설정
#print(sample2)

max_rating2 = sample2['rating'].max()
min_rating2 = sample2['rating'].min()
#print(min_rating2)
merge1 = pd.merge(sample2,sample3) #먼저 값을 계산후 merge
#print(merge1.info())
print("2-1)영화별 최고평점 제목")
print(merge1[merge1['rating']==max_rating2]['title'].values) #최고평점(rating대신 title을 넣으면 답)
print("2-2)영화별 최저평점 제목")
print(merge1[merge1['rating']==min_rating2]['title'].values) #최저평점(rating대신 title을 넣으면 답)

#3번
sample4 = pd.read_csv("./ml-latest-small/ratings.csv")
sample5 = pd.read_csv("./ml-latest-small/movies.csv")
#Crime장르와 Thriller장르 공통분모 찾기
dup_drop = sample5[sample5['genres'].str.contains("Crime") & sample5['genres'].str.contains("Thriller")]
#print(dup_drop)

sample4 = pd.merge(sample4,dup_drop)
sample4 = sample4.groupby('movieId',as_index=False).mean() #movieId를 불러오기 위해 index여부를 X 설정
#print(sample4)
max_rating3 = sample4['rating'].max()
#print(max_rating3)
merge2 = pd.merge(sample4,sample5)
#print(merge2)
print("3)범죄스릴러 장르 최고평점")
print(merge2[merge2.rating==max_rating3]['title'].values) #최고평점(rating대신 title을 넣으면 답)
