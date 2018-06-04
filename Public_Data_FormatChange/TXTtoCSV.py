import sys
import csv
from readCSV import readCSV
from collections import defaultdict

# init
datas = defaultdict(list)
slash = "/"

# get path
path = sys.argv[0].rsplit(slash,2) 

# enter the filename and encoding 
encoding = 'euc-kr'
fileName = "entrc_test.txt" # http://www.juso.go.kr/addrlink/addressBuildDevNew.do?menu=geodata
filePath = path[0]+slash+fileName

def TXTtoCSV(loc, encoding):
    try :
        # with ~ as (auto file close)
        with open(loc, 'r', encoding=encoding) as in_file:
            stripped = (line.strip() for line in in_file)
            lines = (line.split("|") for line in stripped if line)
            with open((fileName.rsplit(".",1))[0]+'.csv', 'w') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(('sidocode', 'enterNo', 'bCod', 'sido','gu','dong','dCod','d','bf','aaa','bbb','ccc','ddd','eee','fff','ggg','X','Y'))
                writer.writerows(lines)
    except UnicodeDecodeError as e:
        # 어떻게 해야, 자동으로 인코딩 방식을 변경해 줄 수 있을까?
        print("인코딩 방식 "+encoding+"이(가) 맞지 않습니다.")
        print(e)
    except FileNotFoundError:
        # slash = "\\"
        # filePath = path[0]+slash+fileName
        print("파일 "+filePath+"이(가) 없습니다.")

# .txt --> .csv
TXTtoCSV(filePath, encoding)
filePath = filePath.replace('.txt', '.csv')
# Test readCSV
readCSV(filePath, encoding)

