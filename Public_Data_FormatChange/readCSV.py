import sys
import csv
from collections import defaultdict

# init
datas = defaultdict(list)
slash = "/"

# get path
path = sys.argv[0].rsplit(slash,2) 

# enter the filename and encoding 
encoding = 'euc-kr'
fileName = "AL_11_D005_20180505.csv"
filePath = path[0]+slash+fileName

def readCSV(loc, encoding):
    try :
        # with ~ as (auto file close)
        with open(loc, encoding=encoding) as f:
            reader = csv.DictReader(f)
            for row in reader:
                for(k,v) in row.items():
                    datas[k].append(v)
            print(datas)
    except UnicodeDecodeError as e:
        # 어떻게 해야, 자동으로 인코딩 방식을 변경해 줄 수 있을까?
        print("인코딩 방식 "+encoding+"이(가) 맞지 않습니다.")
    except FileNotFoundError:
        # slash = "\\"
        # filePath = path[0]+slash+fileName
        print("파일 "+filePath+"이(가) 없습니다.")

# readCSV(filePath, encoding)


def readCSV(loc, encoding, *colNames):
    try :
        # with ~ as (auto file close)
        with open(loc, encoding=encoding) as f:
            reader = csv.DictReader(f)
            for row in reader:
                for(k,v) in row.items():
                    datas[k].append(v)
            for col in colNames:
                print(datas[col])
    except UnicodeDecodeError as e:
        # 어떻게 해야, 자동으로 인코딩 방식을 변경해 줄 수 있을까?
        print("인코딩 방식 "+encoding+"이(가) 맞지 않습니다.")
    except FileNotFoundError:
        # slash = "\\"
        # filePath = path[0]+slash+fileName
        print("파일 "+filePath+"이(가) 없습니다.")