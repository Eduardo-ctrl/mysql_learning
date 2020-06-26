import pymysql

#1.创建与数据库连接对象
db = pymysql.connect(host='localhost',user='root',
                     password='123456',database='db2',
                     charset='utf8')
#2.利用db方法创建游标对象
cur = db.cursor()

try:
    sql_select = "select * from sheng;"
    cur.execute(sql_select)

    data1 = cur.fetchone()
    print(data1)
    print("**************")

    data2 = cur.fetchmany(3)
    for x in data2:
        print(x)
    print("**************")

    data3 = cur.fetchall()
    for x in data3:
        print(x)
    print("**************")

    db.commit()
except Exception as e:
    print(e)

cur.close()
db.close()