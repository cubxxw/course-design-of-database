"""*************************************************************************
    > File Name: h.py
    > Author: smile
    > Mail: 3293172751nss@gmail.com 
    > Created Time: Sat 11 Dec 2021 01:29:53 PM CST
 ************************************************************************"""

# coding=utf-8
#!use/bin/env python3

import pymysql             #使用pymysql板块     
import hashlib
import getpass             #隐藏密码

try:                            
    conn = pymysql.connect(     
        host = '127.0.0.1',     
        user='smile',            
        passwd='1234',          
        db='python',            
        port= 3306,      #端口号       
        charset='utf8'   #字符数
        )                       
    print("-------------python-连接成功------------------------")           

#REVOKE ALL PRIVILEGES ON `python`.* FROM 'smile'@'%';  ---给smile用户访问权限
#GRANT ALL PRIVILEGES ON `python`.* TO 'smile'@'%' WITH GRANT OPTION;
#CREATE USER 'student'@'%' IDENTIFIED WITH mysql_native_password AS '***';   创建student用户
#GRANT ALL PRIVILEGES ON *.* TO 'student'@'%' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;GRANT ALL PRIVILEGES ON `python`.* TO 'student'@'%';
except pymysql.Error as e:      
    print("数据库连接失败",e)  
    #e：打印数据库的错误原因  ,try检测异常
cursor = conn.cursor()   #使用cursor方式创建一个游标
def get_md5(data):          #设置加密密耻
    obj = hashlib.md5("12:;idrsicxwersdfsaersdfsdfresdy54436jgfdsjdxff123ad".encode('utf-8'))
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result                          #使用hash对其加密

name = input("请输入姓名 :")    #实现密码的确认收集
def password_verification():
    pas = getpass.getpass('请输入密码 :')
    match = False   #NULL
    while match is False:
        while len(pas) < 8 or len(pas) > 15:
            pas = getpass.getpass('输入的密码小于8位 - 请重新输入密码，它的长度在8~15位: ')
        pas_1 = getpass.getpass('确认您的密码 : ')
        if pas_1 == pas:  
            print('密码添加成功！')
            match = True  #添加成功后设置成turn退出循环
        else:
            print('密码不匹配')
    return pas

a=password_verification()
pas = a
a=get_md5(pas)   #将a传入

sql = "insert into user(sno, passwd) values ('%s','%s')" % (name,a)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   conn.commit()
except:
   # 如果发生错误则回滚
   conn.rollback()
print("==================================================")
print("当前登陆的用户如下--密码使用非对称加密\n")
cursor.execute("select * from user")
re = cursor.fetchall()
for row in re:
    fname = row[0]
    passwd = row[1]
    date = row[2]
    print("用户: %s --- 密码: %s ---时间: ---'%s'"%\
            (fname,passwd,date))
print("==================================================")


print("==================================================")
print("||||你的姓名是： ",name)
print("||||hash密码是： ",a)
print("==================================================")
#将用户插入到数据表user中

try:                            
    conn1 = pymysql.connect(     
        host = '127.0.0.1',     
        user='student',            
        passwd='11111111',          
        db='student',            
        port= 3306,      #端口号       
        charset='utf8'   #字符数
        )                       
    print("-------------student-连接成功---------------------")           
except pymysql.Error as e:      
    print("student数据库连接失败",e)  
cursor1 = conn1.cursor()   #使用cursor方式创建一个游标

try:                            
    conn2 = pymysql.connect(     
        host = '127.0.0.1',     
        user='teacher',            
        passwd='22222222',          
        db='teacher',            
        port= 3306,      #端口号       
        charset='utf8'   #字符数
        )                       
    print("-------------teacher-连接成功---------------------")           
except pymysql.Error as e:      
    print("teacher数据库连接失败",e)  
cursor2 = conn2.cursor()   #使用cursor方式创建一个游标

try:                            
    conn3 = pymysql.connect(     
        host = '127.0.0.1',     
        user='admin',            
        passwd='00000000',          
        db='admin',            
        port= 3306,      #端口号       
        charset='utf8'   #字符数
        )                       
    print("-------------admin-连接成功-----------------------")           
except pymysql.Error as e:      
    print("admin数据库连接失败",e)  
cursor3 = conn3.cursor()   #使用cursor方式创建一个游标
#cursor.execute("PRAGMA foreign_keys = ON")
#执行函数，强制外键约束
#使用execute方式执行SQL查询
#使用fetchone（）方式获取单条数据

def login_menu():  #admin管理   shudent  :学生账户 passwd1234
    print('\n')
    usage = ('\tA/a: 学生登录',    
             '\tB/b: 教师登录',
             '\tC/c: 管理员登录',
             '\tQ/q: 退出')
    print('Login'.center(20, '='))
    mycount()
    for u in usage:    #设置登陆的页面
       print(u)      # 输出usage

#-----------------------------------------------------------#
def stu_login():        #-学生登陆-
    username = input("输入账号：\t")
    passward = getpass.getpass("输入密码：\t")
    passward=get_md5(passward)
    sql_username = 'select * from user'  #执行查询语句,查询用户信息表，登陆用户
    cursor1.execute(sql_username)  #execute执行sql的查询操作，查出对应账户和密码记录
    username_list = cursor1.fetchall()  
#和fetchone不同的是，fetchone返回单个元组，单挑记录，而fetchall返回多条记录，存入list

    target = None       # 设置为一个空对象，不同于None
    for rec in username_list:    #日常遍历
        if username in rec:   #如果输入符合要求，则退出循环
            target = rec   #相匹配跳出循环
            break

    while True:
        a = str(target[0])
        a = get_md5(a)
        b = str(target[1])
        b = get_md5(b)
        if username == target[0] and passward == b:
            print("hash密码是：",b,"\t登陆成功！")
            break
        else:
            print("账号或密码错误，请重新输入。")
            username = input("输入账号：")
            passward = getpass.getpass("输入密码：")
    conn1.close()

def teach_login():   #设置教师的登陆界面 ，使用的数据库是teacher
    username = input("输入账号：\t")
    passward = getpass.getpass("输入密码：\t")
    passward = get_md5(passward)            #对密码加密
    sql_username = 'select * from user'
    cursor2.execute(sql_username)  #将查询结果保存
    username_list = cursor2.fetchall()  #将返回记录保存在列表

    target = False  # 对应客户的账号密码
    for rec in username_list:
        if username in rec:
            target = rec
            break

    while True:
        a = str(target[0])
        a = get_md5(a)
        b = str(target[1])
        b = get_md5(b)
        if username == target[0] and passward == b:
            print("hash密码是：",b,"登陆成功！")
            break
        else:
            print("账号或密码错误，请重新输入。")
            username = input("输入账号:\t")
            passward = getpass.getpass("输入密码：\t")
            passward = get_md5(passward)
    conn2.close()


def admin_login():    #管理员登陆界面
    username = input("输入账号:\t")
    passward = getpass.getpass("输入密码:\t")
    passward = get_md5(passward)
    sql_username = 'select * from user'
    cursor3.execute(sql_username)
    username_list = cursor3.fetchall()
    target = None  # 对应客户的账号密码
    for rec in username_list:
        if username in rec:
            target = rec
            break

    while True:
        a = str(target[0])
        a = get_md5(a)
        b = str(target[1])
        b = get_md5(b)
        if username == target[0] and passward == b:
            print("hash密码是：",b,"\t登陆成功！")
            break
        else:
            print("账号或密码错误，请重新输入。")
            username = input("输入账号：\t")
            passward = getpass.getpass("输入密码:\t")
            passward = get_md5(passward)
    admin_menu()   #调用admin菜单函数
    conn3.close()

#------------------------------------------------------#
def stu_menu():  #学生student
    stu_usage = ('\tA/a: 学生信息查询',
                 '\tB/b: 学生课程信息查询',
                 '\tC/c: 奖惩信息查询',
                 '\tQ/q: 退出')
    print("学生管理界面".center(20, '='))
    for u in stu_usage:
        print(u)

def teach_menu():
    teach_usage = ('\tA/a: 学生信息管理',
                   '\tQ/q: 退出')
    print("教师管理界面".center(20, '='))
    for u in teach_usage:
        print(u)

def admin_menu():  #管理员界面
    admin_usage = ('\tA/a: 学生信息管理',
                   '\tB/b: 学生成绩（课程）管理',
                   '\tC/c: 奖惩信息管理',
                   '\tD/d: 更改密码',
                   '\tF/f: mysql-查询系统',
                   '\tE/e: 帮助信息',
                   '\tQ/q: 退出')
    print("管理员界面".center(20, '='))
    for u in admin_usage:
        print(u)

#------------------------------------------------------#
def manage_table_stu():  #教师界面
    """学生信息管理"""
    stu_usage = ('\tA/a: 查询学生信息',
                   '\tB/b: 录入学生成绩',
                   '\tC/c: 更改学生成绩',
                   '\tD/d: 删除学生成绩',
                   '\tQ/q: 退出')
    print("管理界面".center(20, '='))
    for u in stu_usage:
        print(u)  #遍历功能
    while True:
        command = input('Please choose a command:\t')
        if command in ('A', 'a'):
            table_stu_select()
        elif command in ('B', 'b'):
            table_stu_insert()
        elif command in ('C', 'c'):
            table_stu_update()
        elif command in ('D', 'd'):
            table_stu_delete()
        elif command in ('Q', 'q'):
            break  #直接退出

def manage_table_stu_course():  #学生选课表的信息查询
    teach_usage = ('\tA/a: 查询学生选课信息',
                   '\tB/b: 录入学生选课信息',
                   '\tC/c: 更改学生选课信息',
                   '\tD/d: 删除学生选课信息',
                   '\tM/m: 查询所有男生信息',
                   '\tF/f: 查询所有女生信息',
                   '\tALL/all: 查询所有学生信息',
                   '\tQ/q: 退出')
    print("管理界面".center(20, '='))
    for u in teach_usage:
        print(u)
    while True:
        command = input('Please choose a command: ')
        if command in ('A', 'a'):
            table_stu_course_select()   #函数调用
        elif command in ('B', 'b'):
            table_stu_course_insert()
        elif command in ('C', 'c'):
            table_stu_course_update()
        elif command in ('D', 'd'):
            table_stu_course_delete()
        elif command in ('Q', 'q'):
            break

#--------------------------------------------------------------
def manage_table_stu_reward_punishment():
    usage = ('\tA/a: 查询奖惩信息',
             '\tB/b: 录入奖惩信息',
             '\tC/c: 更改奖惩信息',
             '\tD/d: 删除奖惩信息',
             '\tQ/q: 退出')
    print("奖惩信息管理界面".center(20, '='))
    for u in usage:
        print(u)
    while True:
        command = input('Please choose a command:')
        if command in ('A', 'a'):
            table_stu_reward_punishment_select()
        elif command in ('B', 'b'):
            table_stu_reward_punishment_insert()
        elif command in ('C', 'c'):
            table_stu_reward_punishment_update()
        elif command in ('D', 'd'):
            table_stu_reward_punishment_delete()
        elif command in ('Q', 'q'):
            break
        else:
            print("请输入合法的选项。")
            input("按下回车以继续: ")

def table_stu_select():
    """查询学生表中指定学生的所有信息"""
    stu_id = input('请输入你的学号：')
    sql = "select * from student where sno = '%s'"% (stu_id) #注意%s需要'%s' ---使用正则表达式
    cursor.execute(sql)   #执行sql语句
    list = cursor.fetchall()           

    if not list:
        print('\tDatabase has no record at this time.')
    else:
        for rec in list:
            print(rec)
    input("按下回车以继续: ")

def table_stu_insert():       
    """往student表中新增数据"""
    while True:
        sno = input('输入学号（输入0以结束）: ')
        if sno == '0':
            break
        sname = input('输入姓名: ')
        ssex = input('输入性别（男/女）: ')        #
        while ssex not in ('男', '女'):
            ssex = input("请输入正确的性别（男/女）：")
        sage = input('输入年龄: ')
        sclass = input('输入班级: ')
        intime = input('输入入学时间--注意格式datebase: ')
        sql = "insert into student values ('%s','%s','%s','%s','%s', '%s')" % (sno, sname, ssex, sage, sclass, intime)
        cursor.execute(sql)
        conn.commit()
        print("添加成功")
        sno = None

def table_stu_update():
    while True:
        sno = input('输入需要修改信息的学生的学号（输入0以结束): ')
        if sno == '0':
            break
        print("修改开始")
        sname = input('输入姓名: ')
        ssex = input('输入性别（男/女）: ')
        while ssex not in ('男', '女'):
            ssex = input("请输入正确的性别（男/女）：")
        sage = input('输入年龄: ')
        sclass = input('输入班级: ')
        intime = input('输入入学时间: ')
        sql = """update student set 
                 sname='%s', ssex='%s', sage=%s, sclass='%s', intime='%s' 
                 where sno=%s""" % (sname, ssex, sage, sclass, intime, sno)
        cursor.execute(sql)
        conn.commit()
        print("修改成功")

def table_stu_delete():
    while True:
        sno = input('输入要删除的信息对应的学号（输入0以结束）: ')
        if sno == '0':
            break
        sql = "delete from student where sno = '%s'" % sno
        cursor.execute(sql)
        conn.commit()
        print("删除成功")

def table_stu_course_select():      #查找学生信息
    stu_id = input('请输入你的学号：')
    sql = 'select cname from course where cno in (select cno from stu_course where sno = %s)' % (stu_id)
    cursor.execute(sql)
    list = cursor.fetchall()

    if not list:
        print('暂无此记录')
        input("按下回车以继续: ")
    else:
        for rec in list:
            print(rec)
    input("按下回车以继续: ")  

def table_stu_course_insert():    #插入课表
    while True:
        sno = input('输入学号（输入0以结束）: ')
        if sno == '0':
            break
        cno = input("输入要选修的课程号")
        list = table_course_select()
        cno_list = []
        for rec in list:
            cno_list.append(rec[0])

        while cno not in cno_list:
            cno = input("没有这门课，请输入正确的课程编号（输入“q”以退出）：")
            if cno == 'q':
                break

        grade = input("输入这位学生该门课程的成绩（若暂无，请输入”n“）：")
        if grade == 'n':
            grade = ''

        sql = "insert into stu_course(sno, cno, grade) values ('%s','%s','%s')" % (
        sno, cno, grade)
        cursor.execute(sql)
        conn.commit()            #提交事务
        print("添加成功")

def table_stu_course_update():
    while True:
        sno = input('输入需要修改信息的学生的学号（输入0以结束): ')
        if sno == '0':
            break
        cno = input('输入该学生所选的课程编号: ')
        print("修改开始")
        grade = input("输入该学生该门课成绩（若暂无，请输入”n“）：")
        if grade == 'n':
            grade = ''
        sql = """update stu_course set grade=%s 
                 where sno='%s' and cno='%s'""" % (grade, sno, cno)
        cursor.execute(sql)
        conn.commit()
        print("修改成功")

def table_stu_course_delete():         # 删除学生的信息
    while True:
        sno = input('输入要删除的学生对应的学号（输入0以结束）: ')
        if sno == '0':
            break
        cno = input('输入该学生所选的课程编号: ')
        sql = "delete from stu_course where sno = '%s' and cno = '%s'" % (sno, cno)
        cursor.execute(sql)
        conn.commit()         #提交修改,事务，提交
        print("删除成功")

def table_stu_reward_punishment_select():   #学生的奖惩
    cursor = conn.cursor()
    stu_id = input('请输入学号：')     #查询奖赏的表
    sql = "select * from stu_reward_punishment where sno ='%s'" % (stu_id)
    cursor.execute(sql)
    list = cursor.fetchall()

    if not list:
        print('该学生暂无奖惩记录')
        input("按下回车以继续: ")
    else:
        reward = []
        punishment = []
        for rec in list:
            if rec[2] != None:
                reward.append(rec[2])
            if rec[3] != None:
                punishment.append(rec[3])
    if reward:      #将空的列表来接收添加的数据，添加的数据判断
        print('奖项: ', reward)
    if punishment:
        print('惩罚: ', punishment)
    input("按下回车回到管理界面: ")

def table_stu_reward_punishment_insert():
    while True:
        sno = input('输入学号（输入0以结束）: ')
        if sno == '0':
            break
        reward = input("请输入该学生的奖励信息（若无，请输入”n“）：")
        punishment = input("请输入该学生的惩罚信息（若无，请输入”n“）：")
        if reward == 'n':
            reward = ''
        if punishment == 'n':
            punishment = ''
        sql = "insert into stu_reward_punishment(sno, reward, punishment) values ('%s','%s','%s')" % (sno, reward, punishment)
        cursor.execute(sql)
        conn.commit()
        print("添加成功")

def table_stu_reward_punishment_update():
    while True:
        sno = input('输入需要修改信息的学生的学号（输入0以结束): ')
        if sno == '0':
            break
        print("修改开始")
        reward = input("请输入该学生的奖励信息（若无，请输入”n“）：")
        punishment = input("请输入该学生的惩罚信息（若无，请输入”n“）：")
        if reward == 'n':
            reward = ''
        if punishment == 'n':
            punishment = ''
        sql = """update stu_reward_punishment set 
                 reward = '%s', punishment = '%s'
                 where sno = '%s'""" % (reward, punishment, sno)
        cursor.execute(sql)
        conn.commit()
        print("修改成功")

def table_stu_reward_punishment_delete():
    while True:
        sno = input('输入要删除的信息对应的学号（输入0以结束）: ')
        if sno == '0':
            break
        flag = input("请输入要删除奖励（输入”1“）还是惩罚（输入”2“）？: ")
        if flag == '1': 
            sql = "delete from stu_reward_punishment where reward is not null and sno = %s" % sno
        if flag == '2':  
            sql = "delete from stu_reward_punishment where punishment is not null and sno = %s" % sno
        else:
            while flag not in ('1', '2'):
                flag = input("请输入合法的选项：")
        cursor.execute(sql)
        conn.commit()
        print("删除成功")

def table_course_select():
    sql = 'select * from course'
    cursor.execute(sql)
    list = cursor.fetchall()

    return list

def table_account_update():
    while True:
        username = input('输入需要修改的账号（输入0以结束): ')
        if username == '0':
            break
        print("修改开始")
        passward = input('输入新密码: ')
        sql = """update account set passward=%s 
                 where username='%s'""" % (passward, username)
        cursor.execute(sql)
        conn.commit()
        print("修改成功")

def update_passward():  #管理员用户修改密码
    while True:
        usage = ('\tA/a: 修改密码',
                 '\tQ/q: 退出')
        print("更改密码".center(20, '='))
        for u in usage:
            print(u)
        command = input('Please choose a command:\t')
        if command in ('A', 'a'):
            table_account_update()
            input("按下回车回到管理界面: ")
        elif command in ('Q', 'q'):
            break
        else:
            print("请输入合法的选项。")
            input("按下回车以继续: ")

def find_admin():    #针对管理员的查询系统
    while True:
        usage = ('\tM/m: 查询所有男生信息',
                '\tF/f: 查询所有女生信息',
                '\tA/a: 查询所有学生信息',
                '\tT/t: 查询所有老师的信息',
                '\tQ/q: 退出查询')
        print("学生信息查询系统".center(20,'='))
        for u in usage:
            print(u)
        command = input('Please choose a command:\t')
        if command in ('T', 't'):
            sql = 'select distinct teacher.tno,teacher_course.cno,teacher.tsex,\
            teacher.tphone,teacher.dmpno,teacher.profess\
            from teacher join teacher_course where teacher_course.tno = teacher.tno'
            #查询老师信息，跨数据库查询，且distinct显示教师号唯一
            cursor.execute(sql)
            print("="*20)
            print("当前的教师信息如下：\n")
            re = cursor.fetchall()
            for row in re:
                tno = row[0]  #姓名
                cno = row[1]
                tsex = row[2]
                tphone = row[3]
                dmpon = row[4]
                prosess = row[5]
                print("教师编号：%s --,教授课程: %s --,性别：%s --,电话号码：%s --,dmpno: %s --,职称：%s "%\
                        (tno,cno,tsex,tphone,dmpon,prosess))
            input("按下回车回到管理界面: ")
        elif command in ('M', 'm'):
            sql = 'select * from jxjm'
            #创建视图jxj create view jxj as select a.sno,a.sname,a.ssex,b.reward,b.punishment 
            #from student a join stu_reward_punishment b on a.sno = b.sno while a.ssex = '男';

            #查询所有男生信息信息，跨数据库查询
            cursor.execute(sql)
            print("="*20)
            print("当前的男生信息如下：\n")
            re = cursor.fetchall()
            for row in re:
                tno = row[0]  #姓名
                cno = row[1]
                tsex = row[2]
                tphone = row[3]
                dmpon = row[4]
                print("学号：%s --,姓名: %s --,性别：%s --,奖励：%s --,惩罚: %s"%\
                        (tno,cno,tsex,tphone,dmpon))
            input("按下回车回到管理界面: ")

        elif command in ('F', 'f'):
            sql = 'select * from jxjf'
            #创建视图jxj create view jxj as select a.sno,a.sname,a.ssex,b.reward,b.punishment 
            #from student a join stu_reward_punishment b on a.sno = b.sno while a.ssex = '女';

            #查询所有男生信息信息，跨数据库查询
            cursor.execute(sql)
            print("="*20)
            print("当前的女生信息如下：\n")
            re = cursor.fetchall()
            for row in re:
                tno = row[0]  #姓名
                cno = row[1]
                tsex = row[2]
                tphone = row[3]
                dmpon = row[4]
                print("学号：%s --,姓名: %s --,性别：%s --,奖励：%s --,惩罚: %s"%\
                        (tno,cno,tsex,tphone,dmpon))
            input("按下回车回到管理界面: ")


        elif command in ('A', 'a'):
            sql = 'select * from jxj'
            #创建视图jxj create view jxj as select a.sno,a.sname,a.ssex,b.reward,b.punishment 
            #from student a join stu_reward_punishment b on a.sno = b.sno;

            #查询所有信息，跨数据库查询
            cursor.execute(sql)
            print("="*20)
            print("当前的所有学生信息如下：\n")
            re = cursor.fetchall()
            for row in re:
                tno = row[0]  #姓名
                cno = row[1]
                tsex = row[2]
                tphone = row[3]
                dmpon = row[4]
                print("学号：%s --,姓名: %s --,性别：%s --,奖励：%s --,惩罚: %s"%\
                        (tno,cno,tsex,tphone,dmpon))
            input("按下回车回到管理界面: ")
        elif command in ('Q', 'q'):
            break
        else:
            print("="*20)
            print("请输入合法的选项。")
            input("按下回车以继续: ")

#统计学生人数功能：
def mycount():
    sql = 'select count(sno) from student'
    cursor.execute(sql)
    count = cursor.fetchall()   #取一条数据
    count = count[0]
    print("当前学生人数： %s"%count)


#主函数运行函数
def main():
    while True:
        login_menu() # 运行登录界面
        command = input('Please choose a command:')
        if command in ('A', 'a'):
            """以学生身份登录"""
            stu_login()
            while True:
                stu_menu()
                command1 = input('Please choose a command:\t')
                if command1 in ('A', 'a'):
                    table_stu_select()
                elif command1 in ('B', 'b'):
                    table_stu_course_select()
                elif command1 in ('C', 'c'):
                    table_stu_reward_punishment_select()
                elif command1 in ('Q', 'q'):
                    break
                else:
                    print("请输入合法的选项。")
                    input("按下回车以继续: ")
        elif command in ('B', 'b'):
            #以老师身份登陆
            teach_login()
            while True:
                teach_menu()
                command4 = input('Please choose a command:')
                if command4 in ('A', 'a'):
                    manage_table_stu()
                elif command4 in ('Q', 'q'):
                    break
                else:
                    print("请输入合法的选项。")
                    input("按下回车以继续: ")
        elif command in ('C', 'c'):
            #以管理员身份登陆
            admin_login()
            while True:
                command2 = input('Please choose a command:')
                if command2 in ('A', 'a'): #
                    manage_table_stu()
                elif command2 in ('B', 'b'):
                    manage_table_stu_course()
                elif command2 in ('C', 'c'):
                    manage_table_stu_reward_punishment()
                elif command2 in ('D', 'd'):
                    update_passward()
                elif command2 in ('F','f'):
                    #统计学生人数
                    find_admin()
                elif command2 in ('E', 'e'):
                    print("请访问百度查找问题！")
                elif command2 in ('Q', 'q'):
                    break
                else:
                    print("请输入合法的选项。")
                    input("按下回车以继续: ")
        elif command in ('Q', 'q'):
            print("good bey!")
            #关闭游标
            cursor.close()             
            #关闭连接
            conn.close()         
            break
        else:
            print("请输入合法的选项。")
            input("按下回车以继续: ")


main()    
