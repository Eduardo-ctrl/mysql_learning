import pymysql
db = pymysql.connect(host="localhost",user="root",
                      password="123456",database="db2",
                      charset="utf8")

cur = db.cursor()

s_id = input("请输入省编号:")
name = input("请输入省名称:")

try:
    sql_insert = "insert into sheng(s_id,S_name)\
                  values(%s,%s);"
    cur.execute(sql_insert,[s_id,name])
    print("ok")
    db.commit()
except Exception as e:
    print("Failed",e)

cur.close()
db.close()