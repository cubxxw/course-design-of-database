# 数据库管理系统 -- mysql+python+hash

<br>

<details><summary><b>💡 关于（先看❗）</b></summary>
<br>
<p><a href='https://www.facebook.com/profile.php?id=100034435372354'>Facebook</a> | <a href='https://telsacoin.io/'>Website</a> | <a href='http://nsddd.top'>Blog</a> | <a href='https://t.me/smile3293172751'>Telegram</a> | <a href='https://twitter.com/xxw3293172751'>Twitter</a> | <a href='https://www.linkedin.cn/injobs/in/xiongxinwei-xiong-7606a0227'>Linkedin</a> | <a href='https://liberapay.com/xiongxinwei/donate'>Donate</a></p>
<p align='center'>
<a href="https://www.linkedin.cn/injobs/in/xiongxinwei-xiong-7606a0227" target="_blank"><img src="https://img.shields.io/badge/linkedin-xiongxinwei-yellowgreen?logo=linkedin&style=flat-square"></a>
<a href="https://twitter.com/xxw3293172751" target="_blank"><img src="https://img.shields.io/badge/twitter-%40xxw3293172751-informational?logo=twitter&style=flat-square"></a>
<a href="https://www.zhihu.com/people/3293172751" target="_blank"><img src="https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-%E9%93%BE%E5%AD%A6%E8%80%85%E7%A4%BE%E5%8C%BA-blue?logo=zhihu&style=flat-square"></a>
<a href="http://sm.nsddd.top/sm0d220ad72063197b9875379403f6c88.jpg" target="_blank"><img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-smile-brightgreen?logo=wechat&style=flat-square"></a>
<a href="https://space.bilibili.com/1233089591" target="_blank"><img src="https://img.shields.io/badge/b%E7%AB%99-%E6%97%A0%E4%B8%8E%E4%BC%A6%E6%AF%94%E7%9A%84%E5%BE%97%E5%BE%97-red?logo=bilibili&style=flat-square"></a>
</p>
<p align='center'>
<a href="https://weibo.com/u/6248930985" target="_blank"><img src="https://img.shields.io/badge/%E5%BE%AE%E5%8D%9A-%E6%97%A0%E4%B8%8E%E4%BC%A6%E6%AF%94%E7%9A%84%E5%BE%97%E5%BE%97-critical?style=social&logo=Sina%20Weibo"></a>
<a href="https://github.com/3293172751" target="_blank"><img src="https://img.shields.io/badge/Github-xiongxinwei-inactive?style=social&logo=github"></a>
<a href="http://nsddd.top" target="_blank"><img src="https://img.shields.io/badge/%E5%8D%9A%E5%AE%A2-%40xiongxinwei-blue?style=social&logo=Octopus%20Deploy"></a>
</p>
  
<b>如果你需要学习：</b>
 🈺 存在`GitHub`上浏览效果不佳，[Cub链学社](https://github.com/C-UB)推出`CubDoc`文档形式，使用`vuejs`渲染 。使用国内的服务器搭建（速度嘎快:bullettrain_front:) 。目前支持以下的项目🗃️：

+ [x] [:speedboat: Go语言基础-进阶](https://go.nsddd.top)

+ [x] [:speedboat: docker & k8s & 云原生](https://docker.nsddd.top)

<br>
  
</details>

<br>

# 一、数据库课程设计要求与目的

(1) 目的

1. 通过数据库课程设计，来进一加深对数据库开发与应用的了解，掌握sql语句与sql服务的要领，从而达到让我们实践的目的。

2. 首先查阅书籍可以知道数据库课程设计数据库系统开发步骤的要领有：需求分析，概念设计，逻辑结构设计，物理结构设计，数据库实施阶段，由此我们可以展开以下高校学籍管理系统的设计。

<br>

(2) 功能要求

> 实现学生信息、班级、院系、专业等的管理；
>
> 实现课程、学生成绩信息管理；
>
> 实现学生的奖惩信息管理；
>
> 创建规则用于限制性别项只能输入"男"或"女"；
>
> 创建视图查询各个学生的学号、姓名、班级、专业、院系；
>
> 创建存储过程查询指定学生的成绩单；
>
> 创建触发器当增加、删除学生和修改学生班级信息时自动修改相应班级学生人数；
>
> 建立数据库相关表之间的参照完整性约束。

# 二、需求分析

## 2.1 需求分析

学生学籍管理系统，旨在探索一种以互联网为平台的管理模式。这种新的管理模式，使教务管理突破时空限制，实现管理的网络化，提高管理效率和标准化水平。使学校管理者、教师和学生可以在任何时候、任何地点通过网络进行管理与查询，让管理者从繁重的工作中解脱出来，将主要精力转移到创造性的教学改革工作中。本系统主要完成对学生基本信息、教师信息、院系信息、专业信息、课程信息、成绩信息和奖惩信息等多种数据信息的管理，即对数据库中表的录入、修改、删除和查询等功能。

学籍管理系统的功能需求包括管理员、学生和教师对功能的需求的三大部分:

**1. 管理员对功能的需求:** 管理员权限最大，可以对学生、教师、课程进行管理，包括对学生学籍信息的增删改查，对教师信息的增删改查，以及对课程信息的增删改查等。

**2. 学生对功能的需求:** 学生只是利用此系统修改自己的登录密码，查询自己的学籍信息，查询课程信息，进行选课，查询成绩。

**3.教师对功能的需求:**

教师利用该系统可以修改自己的登录密码，查询自己的信息，查询自己的授课信息，还对学生和课程进行管理，录入、修改学生的成绩。

## 2.2 系统功能模块图

其系统功能模块说明如下：

-   学生信息管理模块：该模块主要负责所有在校学生的个人基本信息。学生通过这个模块，可以查询自己在校的学籍信息，以及修改自己的登录密码等。管理员通过这个模块可以增加、删除、更改、查询学生的学籍信息。

-   学生课程管理模块：该模块主要负责管理全校师生的课程信息。主要功能包括增加、删除、更改、查询课程信息，其中只有管理员才具有对课程信息进行维护的权限（增加、删除、更改）。学生课程管理模块是选课管理模块的基础，只有在课程管理中添加选修课的信息，学生才能进行选课。针对选课模块，其功能行使者是学生，学生通过浏览全部的课程信息，选择符合自己要求的课程。

-   学生成绩管理模块：该模块的功能主要由老师所拥有。对于选择自己所教授课程的学生，老师具有给定该学生的专业分数和修改该学生的专业分数的权限，而学生只具有查询自己专业成绩的权限。

-   奖惩信息管理模块：该模块主要负责学生受奖励或受批评的公告信息。由学校管理员负责发布。

-   系统管理员管理模块：该模块由系统管理员全权拥有，负责管理学生、管理教师、管理课程等功能模块。

## 2.3数据字典

数据字典的数据项如下列表所示：

**表 1 院系信息表**

  序号   别名     数据类型   数据长度

------ -------- ---------- ----------

```
  1      院系号   varchar    10
  2      院系名   varchar    10
  3      院长名   varchar    10
```

**表2 专业信息表**

  序号   别名     数据类型   数据长度

------ -------- ---------- ----------

```
  1      专业号   varchar    10
  2      专业名   char       10
```

**表3 学生基本信息表**

  序号   别名       数据类型   数据长度

------ ---------- ---------- ----------

```
  1      学号       varchar    20
  2      姓名       varchar    20
  3      性别       Varchar    2
  4      年龄       Int        4
  5      班级       Varchar    10
  6      入学时间   Datetime   
```

**表4 教师基本信息表**

  序号   别名       数据类型   数据长度

------ ---------- ---------- ----------

```
  1      教工号     varchar    10
  2      姓名       varchar    10
  3      性别       varchar    2
  4      职称       varchar    10
  5      所属院系   varchar    10
  6      联系电话   Varchar    20
```

**表5 课程信息表**

  序号   别名       数据类型   数据长度

------ ---------- ---------- ----------

```
  1      课程号     varchar    10
  2      课程名     char       10
  3      学分       Int        2
  4      学时       Int        2
  5      上课时间   varchar    10
  6      教师号     Varchar    10
  7      教室号     Varchar    10
```

**表6 学生选课信息表**

  序号   别名     数据类型   数据长度

------ -------- ---------- ----------

  

```
  1      学号     varchar    10
  2      课程号   varchar    10
  3      成绩     int        3
```

**表7 教师授课信息表**

  序号   别名     数据类型   数据长度

------ -------- ---------- ----------

```
  1      教工号   varchar    10
  2      课程号   varchar    10
```

**表8用户信息表**

  序号   别名   数据类型   数据长度

------ ------ ---------- ----------

```
  1      用户   varchar    20
  2      密码   varchar    20
```

**表9奖惩情况表**

  序号   别名   数据类型   数据长度

------ ------ ---------- ----------

```
  1      学号   varchar    20
  2      奖励   varchar    100
  3      惩罚   Varchar    100
```



## 2.4 事务

**针对于课程设计出现的可能问题，我使用了事务来解决。**

-   **为数据库操作提供了一个从失败中恢复到正常状态的方法，同时提供了数据库即使在异常状态下仍能保持一致性的方法。**

-   **当多个应用程序在并发访问数据库时，可以在这些应用程序之间提供一个隔离方法，以防止彼此的操作互相干扰。**

为了保持程序的完整性，我在代码中使用了大量的事务来保证数据不会丢失。

![image-20220103131214937](https://s2.loli.net/2022/01/03/Q4yzdiOpAvTuNIt.png)

同时，在python中，为了使数据更加的安全，我使用了单向加密（hash函数)确保一些SQL注入的发生。

![image-20220103131327187](https://s2.loli.net/2022/01/03/XuSrp4wBJfkdscU.png)

![image-20220103131340832](https://s2.loli.net/2022/01/03/YMEZXHsGOBxbmzk.png)

## 2.5 触发器：

在统计人数上面使用了select count(sno) from student;对人数进行统计。同时为了防止增删改查对人数的影响，这样不由得就用到了触发器，在增加人数的同时，对数据进行跟新。

# 三、概念结构设计

## 3. 1 实体与联系

>    **实体 （属性）**
>
>   院系(**<span class="underline">院系号</span>**、院系名、院长名) ；
>
>   专业(**<span class="underline">专业号</span>**、<span class="underline">专业名</span>) ；
>
>   学生(**<span class="underline">学号</span>**、姓名、性别、出生日期、联系电话、入学时间)；
>
>   教师(**<span class="underline">教工号</span>**、姓名、性别、职称、院系号、联系电话)；
>
>   课程（**<span class="underline">课程号</span>**、课程名、学时、学分、上课时间，上课教室)；
>
>   选课（**<span class="underline">学号</span>**、**<span class="underline">课程号</span>**、成绩)。
>
>   用户（<span class="underline">用户</span>，密码）
>
>   奖惩情况（<span class="underline">学号</span>，奖励，惩罚）
>
>   教师授课（<span class="underline">教工号</span>，<span class="underline">课程号</span>）
>
>   **实体间的联系情况与转换规则：**
>
>   院系与教师的联系是工作 对应的联系情况是一对多；
>
>   教师与课程的联系是授课 对应的联系情况是多对多；
>
>   学生与专业的联系是属于 对应的联系情况是一对多；
>
>   学生与选课的联系是报课情况，对应的关系是多对多；



## 3．2 局部E-R图

## 3．3 全局E-R图

# 四、逻辑结构设计

## 4.1关系模式

>   将E-R图转换为关系模型实际上就是要奖实体型、实体的属性和实体型之间的联系转换为关系模式，这种转换一般遵循如下原则：一个实体型转换为一个关系模式。实体的属性就是关系的属性，实体的码就是关系的码。现将概念结构设计阶段设计好的基本
>
>   E-R图转换为关系模型，如下所示：
>
>   院系(**<span class="underline">院系号</span>**、院系名、院长名) ；
>
>   专业(**<span class="underline">专业号</span>**、<span class="underline">专业名</span>) ；
>
>   学生(**<span class="underline">学号</span>**、姓名、性别、出生日期、联系电话、入学时间)；
>
>   教师(**<span class="underline">教工号</span>**、姓名、性别、职称、院系号、联系电话)；
>
>   课程（**<span class="underline">课程号</span>**、课程名、学时、学分、上课时间，上课教室)；
>
>   选课（**<span class="underline">学号</span>**、**<span class="underline">课程号</span>**、成绩)。
>
>   用户（<span class="underline">用户</span>，密码）
>
>   奖惩情况（<span class="underline">学号</span>，奖励，惩罚）
>
>   教师授课（<span class="underline">教工号</span>，<span class="underline">课程号</span>）

## 4.2建表属性与sql代码

**<span class="underline">院系表：</span>**

![image-20220103131657888](https://s2.loli.net/2022/01/03/elPtcIF7oMXw215.png)

```sql
CREATE TABLE \`department\` (

\`dmpno\` varchar(5) NOT NULL,

\`dname\` varchar(10) NOT NULL,

\`dmphead\` varchar(10) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=gbk;
```

**<span class="underline">专业表：</span>**

![image-20220103131720704](https://s2.loli.net/2022/01/03/YOLAQ5Kphd19Gjt.png)

```sql
CREATE TABLE \`major\` (

\`mno\` varchar(5) NOT NULL,

\`mname\` varchar(10) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=gbk;
```

**<span class="underline">学生表：</span>**

![image-20220103131731018](https://s2.loli.net/2022/01/03/L7A6swMrOXWbPGE.png)

```sql
CREATE TABLE \`student\` (

\`sno\` varchar(20) NOT NULL,

\`sname\` varchar(10) NOT NULL,

\`ssex\` varchar(2) NOT NULL,

\`sage\` int(4) NOT NULL,

\`sclass\` varchar(10) NOT NULL,

\`intime\` datetime NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=gbk;
```

**<span class="underline">用户表：</span>**

![image-20220103131758166](https://s2.loli.net/2022/01/03/sARytzdvBpKw3JZ.png)

```sql
CREATE TABLE \`account\` (

\`username\` varchar(20) NOT NULL,

\`passward\` varchar(20) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=gbk;
```

**<span class="underline">课程表：</span>**

![image-20220103131809911](https://s2.loli.net/2022/01/03/tFpMahTzwL8Qi1J.png)

```sql
CREATE TABLE \`course\` (

\`cno\` varchar(10) NOT NULL,

\`cname\` varchar(10) NOT NULL,

\`tno\` varchar(10) NOT NULL,

\`c_period\` varchar(10) NOT NULL,

\`clocation\` varchar(10) NOT NULL,

\`credit\` int(2) NOT NULL,

\`ctime\` int(2) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=gbk;
```

**<span class="underline">教师表：</span>\
![image-20220103131837051](https://s2.loli.net/2022/01/03/RT9bpCQfled5B6E.png)

```sql
CREATE TABLE \`teacher\` (

\`tno\` varchar(20) NOT NULL,

\`tname\` varchar(10) NOT NULL,

\`tsex\` varchar(2) NOT NULL,

\`tphone\` varchar(20) NOT NULL,

\`dmpno\` varchar(10) NOT NULL,

\`profess\` varchar(10) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=gbk;
```

**<span class="underline">教师任课表：</span>**

![image-20220103131857296](https://s2.loli.net/2022/01/03/AC8smZI5xS2qnce.png)

```sql
CREATE TABLE \`teacher_course\` (

\`tno\` varchar(10) NOT NULL,

\`cno\` varchar(10) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=gbk;
```

**<span class="underline">选课表：</span>**

![image-20220103131919631](https://s2.loli.net/2022/01/03/ME6uDCRVpf4JGBs.png)

```sql
CREATE TABLE \`stu_course\` (

\`sno\` varchar(20) NOT NULL,

\`cno\` varchar(10) NOT NULL,

\`grade\` int(3) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=gbk;
```

**<span class="underline">奖惩情况表：</span>**

![image-20220103131934962](https://s2.loli.net/2022/01/03/NP3G7fL6evszdUT.png)

```sql
CREATE TABLE \`stu_reward_punishment\` (

\`sno\` varchar(20) NOT NULL,

\`reward\` varchar(100) DEFAULT NULL,

\`punishment\` varchar(100) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=gbk;
```



## 4.3插入数据的sql代码

\"创建表格插入数据\"

```sql
1.  insert into student values (\'202032120777\', \'张晓梅\', \'女\', 20, \'经管1701\', \'2017-09-01\');

2.  insert into student values (\'201932120778\', \'李晓龙\', \'男\', 21, \'数学1601\', \'2020-09-01\');

3.  insert into student values (\'202132120779\', \'黄飞红\', \'女\', 20, \'英语1801\', \'2018-09-01\');

4.  insert into student values (\'202032120768\', \'李云隆\', \'男\', 21, \'数学1701\', \'2017-09-01\');

5.  insert into student values (\'201932120720\', \'张阿红\', \'女\', 19, \'英语1901\', \'2019-09-01\');

6.  insert into student values (\'201932120711\', \'马晕\', \'男\', 22, \'数学1601\', \'2020-09-01\');

7.  insert into student values (\'202032120762\', \'鲁智深\', \'男\', 21, \'经管1701\', \'2017-09-01\');

8.  insert into student values (\'202132120719\', \'孙文空\', \'女\', 19, \'英语1801\', \'2018-09-01\');

9.  insert into student values (\'201932120710\', \'马花藤\', \'男\', 22, \'数学1601\', \'2020-09-01\');

10.  

11.  insert into course values (\'c001\', \'微观经济学\', \'122118\', \'周四 第10-12节\', \'3-311\', 3, 80);

12.  insert into course values (\'c002\', \'宏观经济学\', \'122124\', \'周五 第10-12节\', \'22-402\', 6, 60);

13.  insert into course values (\'c003\', \'英语名著欣赏\', \'122125\', \'周三 第1-3节\', \'4-301\', 2, 60);

14.  insert into course values (\'c004\', \'数学分析\', \'122110\', \'周二 第1-4节\', \'20-201\', 6, 80);

15.  insert into course values (\'c005\', \'高等数学\', \'122110\', \'周四 第1-4节\', \'3-310\', 6, 80);

16.  insert into course values (\'c006\', \'商务英语写作\', \'122122\', \'周四 第8-9节\', \'5-301\', 4, 80);

17.  

18.  insert into teacher values (\'122118\', \'陈读\', \'男\', \'17398447611\' , \'d001\', \'副教授\');

19.  insert into teacher values (\'122124\', \'韩宏\', \'女\', \'17398440222\' , \'d001\', \'教授\');

20.  insert into teacher values (\'122125\', \'马冬梅\', \'女\', \'17398449118\' , \'d002\', \'副教授\');

21.  insert into teacher values (\'122110\', \'唐伯虎\', \'男\', \'17398443912\' , \'d003\', \'副教授\');

22.  insert into teacher values (\'122122\', \'谭英文\', \'男\', \'17398442121\' , \'d002\', \'副教授\');

23.  

24.  insert into department values (\'d001\', \'经济学院\', \'王元\');  

25.  insert into department values (\'d002\', \'英语学院\', \'张小龙\'); 

26.  insert into department values (\'d003\', \'数学学院\', \'黄飞\'); 

27.  

28.  insert into major values (\'m001\', \'经济学专业\'); 

29.  insert into major values (\'m002\', \'英文专业\');

30.  insert into major values (\'m003\', \'数学专业\');  

31.  

32.  insert into stu_course values (\'202032120777\', \'c001\', null);

33.  insert into stu_course values (\'202032120777\', \'c002\', null);

34.  insert into stu_course values (\'201932120778\', \'c004\', null);

35.  insert into stu_course values (\'201932120778\', \'c005\', null);

36.  insert into stu_course values (\'202132120779\', \'c003\', null);

37.  insert into stu_course values (\'202032120768\', \'c004\', 70);

38.  insert into stu_course values (\'202032120762\', \'c002\', 80);

39.  insert into stu_course values (\'202132120719\', \'c003\', 90);

40.  insert into stu_course values (\'202132120719\', \'c006\', 92);

41.  

42.  insert into teacher_course values (\'122118\', \'c001\');

43.  insert into teacher_course values (\'122124\', \'c002\');

44.  insert into teacher_course values (\'122125\', \'c003\');

45.  insert into teacher_course values (\'122110\', \'c004\');

46.  insert into teacher_course values (\'122110\', \'c005\');

47.  insert into teacher_course values (\'122122\', \'c006\');

48.  

49.  insert into class_stu_num values (\'经管1701\', 2);

50.  insert into class_stu_num values (\'数学1601\', 3);

51.  insert into class_stu_num values (\'数学1701\', 1);

52.  insert into class_stu_num values (\'英语1801\', 2);

53.  insert into class_stu_num values (\'英语1901\', 1);

54.  

55.  insert into stu_reward_punishment(sno, reward) values (\'202032120777\', \'校一等奖学金\');

56.  insert into stu_reward_punishment(sno, punishment) values (\'202032120777\', \'全校通告批评\');

57.  insert into stu_reward_punishment(sno, punishment) values (\'201932120711\', \'校一等奖学金\');

58.  

59.  insert into account values (\'stu\', \'1224\');

60.  insert into account values (\'stu1\', \'1224\');

61.  insert into account values (\'teach\', \'1224\');

62.  insert into account values (\'admin\', \'1224\');  

63.  insert into account values (\'student\', \'1224\');

64.  \"用户的登陆信息表格\"
```



根据用户的需求，需建立三个视图，分别是**查看学生视图、查看课程视图、查询选课视图。**

# 五、物理结构设计

数据库在物理设备上的存储结构与存取方法成为数据库的物理结构，它依赖于选定的数据库管理系统。为一个给定的逻辑数据模型选取一个最适合应用要求的物理结构的过程，就是数据库的物理设计。

 **5.1 、数据库的物理设计：**

1.  确定数据库的物理结构，在关系数据库中主要指存取方法和存储结构；

2.  对物理进行评价，评价的重点是时间和空间效率。

 **5.2、关系数据库物理设计：**

1.  为关系模式选择存取方法；常用的存储方法有索引法（B+树法）、聚簇法和HASH方法。\
    在我的设计中，使用了hash方法，对存储的数据进行单向加密和保护。

2.  设计关系、索引等数据库文件的物理存储结构。

3.  确定数据库物理结构主要指确定数据的存放位置和存储结构，包括：确定关系、索引、聚簇、日志、备份等的存储安排和存储结构，确定系统配置等。

4.  评价屋里数据库的方法完全依赖于所选用的DBMS，主要是从定量估算各种方案的存储空间、存储时间和维护代价入手，对估算结果进行权衡、比较，选择出一个较优的合理的物理结构。

# 六、界面展示



#### **6.1用户界面：(后台使用mysql语句可以显示统计出的学生人数)**

![image-20220103132110793](https://s2.loli.net/2022/01/03/VDwSI65gkBZ7GxE.png)

#### **6.2学生管理界面：（密码11111111）**

![image-20220103132121418](https://s2.loli.net/2022/01/03/JzZjaD9mQdSAH78.png)

![image-20220103132138501](https://s2.loli.net/2022/01/03/mzO1HWfxaGrAkvT.png)

#### **6.3教师界面：（密码22222222）**

a:查询学生信息

![image-20220103132153766](https://s2.loli.net/2022/01/03/O9YNSo7s5Wxa4fR.png)

B:录入学生信息：

![image-20220103132233672](https://s2.loli.net/2022/01/03/nh824X9glOtKDMk.png)

查询，添加成功！

![image-20220103132431418](https://s2.loli.net/2022/01/03/A9fbHsrmKBelQ7u.png)

#### **6.4管理员界面：（密码：00000000）**

界面：

![image-20220103134740363](https://s2.loli.net/2022/01/03/JgvAiOWsD6b4Nq9.png)



F/f查询系统：

![image-20220103134746845](https://s2.loli.net/2022/01/03/mCBotiTzqJpYfk6.png)



查询所有女生：

![image-20220103134755223](https://s2.loli.net/2022/01/03/OiwcqYCWIfAKbDy.png)



查询所有老师信息：

​                                              !![](https://s2.loli.net/2022/01/03/OiwcqYCWIfAKbDy.png)



#### 学生成绩管理系统：

查询和录入学生信息：202006010300

![image-20220103134811910](https://s2.loli.net/2022/01/03/wuGyJhrcn27kFWl.png)

奖惩界面：

![image-20220103132631331](https://s2.loli.net/2022/01/03/ZjaKVFChl48EAT6.png)

# 六、结论

经过这个系统的设计，我不仅仅是融会贯通了书中的知识，更重要的是在学习的过程中，所有的问题要自己去面对，有问题也只有靠自己去解决，在学习和解决这些困难的过程中提高了我学习的能力、解决问题的能力和实际工作的能力，学到了许多书本以外的知识。

在本学期的数据库设计中，通过对高校的学籍管理系统的设计，我学习到独立完成作业的重要性，锻炼了在编写实际运用数据库的实现，深刻感受到计算机学习的实用性和未来工作的巨大信息，但是由于学习效果不佳，在一些问题的处理和考虑的方面存在很大的缺陷和漏洞，希望在进一步的学习中能更好处理好相关问题。这次课题设计不能堪称完美，甚至来说还很不健全，但我会在以后的时间里去尽量的完善它，不断的对它进行升级和完善，解决系统可能会出现的。

