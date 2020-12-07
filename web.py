import sys,os,requests,base64,json,logging,time,pymysql
import pandas as pd
import csv

host =  ""
port = 3306
username = ""
password = ""
database = "test"

conn = pymysql.connect(host=host,port=port,user=username,passwd=password,db=database,charset='utf8')
curs=conn.cursor()
sql="insert into test.rank(id,score) values(%s,%s);"
#user_id=cy2
#user_score=0
curs.execute(sql,[user_id,user_score])
conn.commit()
conn.close()
