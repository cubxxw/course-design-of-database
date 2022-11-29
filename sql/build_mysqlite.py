# coding=utf-8
#!/use/bin/env python3
##########################################################################
"""1.管理员对功能的需求:
管理员权限最大，可以对学生、教师、课程进行管理，
包括对学生学籍信息的增删改查，对教师信息的增删改查，
以及对课程信息的增删改查等。
2.学生对功能的需求:
学生只是利用此系统修改自己的登录密码，查
询自己的学籍信息，查询课程信息，进行选课，查询成绩。
3.教师对功能的需求:
教师利用该系统可以修改自己的登录密码，查询自己的信息，查询自己的授课信息，
还对学生和课程进行管理，录入、修改学生的成绩。
"""
##########################################################################
import pymysql

try:                            
    conn = pymysql.connect(     
        host = '127.0.0.1',     
        user='root',            
        passwd='1234',          
        db='python',            
        port= 3306,      #端口号       
        charset='utf8'   #字符数
        )                       
    print("连接成功")           
except pymysql.Error as e:      
    print("数据库连接失败",e)  
    #e：打印数据库的错误原因

curs = conn.cursor()

def create_tables():
    with open('build_tables.sql', encoding='utf-8', mode='r') as f:
        sql_list = f.read().split(';')[:-1]
        for x in sql_list:
            curs.execute(x)
    conn.commit()
    print("table created.")

def insert_data():
    with open('insert_data.sql', encoding='utf-8', mode='r') as f:
        sql_list = f.read().split(';')[:-1]
        for x in sql_list:
            curs.execute(x)
    conn.commit()
    print("date has inserted.")

# create_tables()
# insert_data()
# result = curs.execute('select * from pymysql_master where type = "table"')
# for i in result:
#     print(i)

sql = 'select * from stu_course'
curs.execute(sql)
list = curs.fetchall()
for rec in list:
    print(rec)
