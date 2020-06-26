import pymysql

#1.创建与数据库连接对象
db = pymysql.connect(host='localhost',user='root',
                     password='123456',database='db2',
                     charset='utf8')
#2.利用db方法创建游标对象
cur = db.cursor()

#3.执行ＳＱＬ命令
#在sheng表中插入１条记录，云南省
try:
    sql_insert = 'insert into sheng values\
                 (17,300002,"西藏");'
    cur.execute(sql_insert)
    #把云南省的id号改为666
    sql_update = "update sheng set id=666 where id=16;"
    cur.execute(sql_update)
    #把台湾省在sheng表中删除
    sql_delete = "delete from sheng where S_name='台湾省';"
    cur.execute(sql_delete)
    print("ok")
    db.commit()
except Exception as e:
    db.rollback()
    print("出现错误，已回滚",e)


#5.关闭游标对象
cur.close()
#6.断开数据库连接
db.close()