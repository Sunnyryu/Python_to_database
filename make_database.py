import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

# pandas dataframe을 이용하여 SampleData.xlsx 파일을 읽어옴
excel_data = pd.read_excel('./SampleData.xlsx')
# 파일 위치인 /home/sunny/Python_to_database/에 있는 SampleData.xlsx 파일의 내용을 읽어온 것이다.

# 마리아 DB를 사용해서 DB를 만들고 만들어진 DB와 연동한다.
engine = create_engine("mysql+mysqldb://xlsxdb:"+"ghehd11"+"@localhost/xlsx_db", encoding='utf-8')
conn = engine.connect()

# table 만들기 ! (dataframe의 to_sql 이용!)
excel_data.to_sql(name='xlsx_data', con=engine,
if_exists='replace', index = False, 
dtype = {
    'OrderDate':sqlalchemy.types.Date(),
    'Region':sqlalchemy.types.VARCHAR(10),
    'Rep':sqlalchemy.types.VARCHAR(10),
    'Item':sqlalchemy.types.VARCHAR(10),
    'Units':sqlalchemy.types.INTEGER(),
    'Unit Cost':sqlalchemy.types.Float(precision=3),
    'Total':sqlalchemy.types.Float(precision=3)
})
# if_exists는 fail/replace/append가 있는데 fail은 존재할 경우 에러가 나도록 설계하는 것이며, replace는 있다면 기존 것을 drop하고 새로운 것을 추가
# append는 테이븖 명이 존재할 경우 기존 테이블에 추가하는 방식으로 쓰인다.
# index = True 일때 index_label를 이용하여 이름 설계 가능!
# dtype을 설정하지 않으면 전부 text로 들어가게 되며, precision은 정밀도!
# Region이나 Rep, Item의 경우 최대글자가 엑셀 상에는 7글자 지만 10으로 설정 

