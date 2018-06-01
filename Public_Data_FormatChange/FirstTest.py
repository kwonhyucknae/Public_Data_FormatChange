#Commit test
#retest
#test
def Test(a,b):
    return a+b

# loc =="2013년_전년대비_시간대별_교통사고_사망자_현황.csv"
# 문제점 1. encodig 형식이 맞지 않을 수 있다.

def readCSV(loc):
    f = open(loc, 'r', encoding="utf-8")
    datas = [] # 리스트 생성
    line = f.readline()
    if not line:
        exit(0)
    line = line.strip().replace(" ", "") # 양 끝의 공백, 중간의 공백 제거
    keys = line.split(",") # 각 줄을 컴마로 구분하여 자름
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip().replace(" ", "")
        values = line.split(",")
        for key in keys:
            d = dict(zip(keys, values)) # 키와 값을 별도로 선언 후 합침
            print(d)
    f.close()

import sys
path = sys.argv[0].rsplit("\\",1)
readCSV(path[0]+"/2013년_전년대비_시간대별_교통사고_사망자_현황.csv")

