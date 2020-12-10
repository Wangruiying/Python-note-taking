'''
使用pymysql连接数据库
'''
# coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='121.36.41.177', port=3306,
                     user='test', passwd='wsx123', db='MyDB_one', charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE if not exists EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)

#单行插入数据，两种方式
sql1 = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
'''
sql1 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
'''
try:
   # 执行sql语句
   cursor.execute(sql1)
   # 执行sql语句,数据库默认为innodb引擎，是支持事物管理的，需要再commit()一下才能插入数据。
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()


#批量插入,与但数据插入不同的地方在于VALUES的，单条为'%s',而多条为%s
sql3 = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES(%s,%s,%s,%s,%s)"
#在参数中注意 空行，对于'NULL'与''，删除方法不同。DELETE FROM EMPLOYEE where  LAST_NAME="NULL"; 或 DELETE FROM EMPLOYEE where  LAST_NAME="";
param = (('ttt','NULL',20, 'M' ,2000),('yyy','',10,'W',2010),('xxx','xyz',10,'W',2010))
try:
    cursor.executemany(sql3,param)
    db.commit()
except:
    db.rollback()
'''
# SQL 插入语句，该遇见与上述批量的数据删除方法也不同：DELETE FROM EMPLOYEE where  LAST_NAME is NULL;
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, AGE, SEX) VALUES (%s,%s,%s)"
# 一个tuple或者list
T = (('xiaoming', 31, ''), ('hong', 22,'' ), ('wang', 90, 'man'))

try:
    # 执行sql语句
    cursor.executemany(sql, T)
    # 提交到数据库执行
    db.commit()
except :
    # 如果发生错误则回滚
    db.rollback()
'''

#查询
#sql4 = "SELECT * FROM EMPLOYEE WHERE FIRST_NAME = 'yyy'"
sql4 = "SELECT * FROM EMPLOYEE WHERE FIRST_NAME = '%s'"  %('yyy')

# 执行SQL语句
cursor.execute(sql4)
db.commit()
# results是个元组对象
results = cursor.fetchone()
# 先判断是否为空
if results is None:
    print("查询为空")
else:
    print(results)

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
