from mysqlpythony import Mysqlpython

#创建数据库连接对象
sqlh = Mysqlpython("db2") 

sql_update = "update sheng set s_name='辽宁省'\
              where s_name='云南省';"
sqlh.zhixing(sql_update) 