__author__ = 'liuguohao'
#coding=utf-8
import mysql.connector



#连接网经数据库
config={'host':'127.0.0.1',#默认127.0.0.1
        'user':'mobile',
        'password':'5i5jwireless',
        'port':3306 ,#默认即为3306
        'database':'wireless',
        'charset':'utf8'#默认即为utf8
        }

try:
    cnn=mysql.connector.connect(**config)
    cur=cnn.cursor()
    cur.execute('select * from brokerwork_callpath')
    for (id,callpath,name) in cur:
        print("ID:{}  Callpath:{}  Name:{}".format(id, callpath, name))
    print(cur.fetchall())

except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cnn.close()
