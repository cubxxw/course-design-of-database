-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2021-12-14 18:02:44
-- 服务器版本： 5.7.34-log
-- PHP 版本： 7.4.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `python`
--

-- --------------------------------------------------------

--
-- 表的结构 `account`
--

CREATE TABLE `account` (
  `username` varchar(20) NOT NULL,
  `passward` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `account`
--

INSERT INTO `account` (`username`, `passward`) VALUES
('admin', '1234'),
('stu', '1234'),
('student', '1234'),
('teacher', '1234');

-- --------------------------------------------------------

--
-- 表的结构 `class_stu_num`
--

CREATE TABLE `class_stu_num` (
  `class` varchar(10) NOT NULL,
  `stu_num` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `class_stu_num`
--

INSERT INTO `class_stu_num` (`class`, `stu_num`) VALUES
('经管1701', 2),
('数学1601', 3),
('数学1701', 1),
('英语1801', 2),
('英语1901', 1);

-- --------------------------------------------------------

--
-- 表的结构 `course`
--

CREATE TABLE `course` (
  `cno` varchar(10) NOT NULL,
  `cname` varchar(10) NOT NULL,
  `tno` varchar(10) NOT NULL,
  `c_period` varchar(10) NOT NULL,
  `clocation` varchar(10) NOT NULL,
  `credit` int(2) NOT NULL,
  `ctime` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `course`
--

INSERT INTO `course` (`cno`, `cname`, `tno`, `c_period`, `clocation`, `credit`, `ctime`) VALUES
('c001', '微观经济学', '123123', '周四 第10-12节', '25-101', 3, 80),
('c002', '宏观经济学', '123124', '周五 第10-12节', '22-402', 6, 60),
('c003', '英语名著欣赏', '123125', '周三 第1-3节', '16-301', 2, 60),
('c004', '数学分析', '123110', '周二 第1-4节', '20-201', 6, 80),
('c005', '高等数学', '123110', '周四 第1-4节', '20-301', 6, 80),
('c006', '商务英语写作', '123122', '周四 第8-9节', '15-201', 4, 80);

-- --------------------------------------------------------

--
-- 表的结构 `department`
--

CREATE TABLE `department` (
  `dmpno` varchar(5) NOT NULL,
  `dname` varchar(10) NOT NULL,
  `dmphead` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `department`
--

INSERT INTO `department` (`dmpno`, `dname`, `dmphead`) VALUES
('d001', '经济学院', '王元'),
('d002', '英语学院', '张小龙'),
('d003', '数学学院', '黄飞');

-- --------------------------------------------------------

--
-- 替换视图以便查看 `jxj`
-- （参见下面的实际视图）
--
CREATE TABLE `jxj` (
`sno` varchar(20)
,`sname` varchar(10)
,`ssex` varchar(2)
,`reward` varchar(100)
,`punishment` varchar(100)
);

-- --------------------------------------------------------

--
-- 替换视图以便查看 `jxjf`
-- （参见下面的实际视图）
--
CREATE TABLE `jxjf` (
`sno` varchar(20)
,`sname` varchar(10)
,`ssex` varchar(2)
,`reward` varchar(100)
,`punishment` varchar(100)
);

-- --------------------------------------------------------

--
-- 替换视图以便查看 `jxjm`
-- （参见下面的实际视图）
--
CREATE TABLE `jxjm` (
`sno` varchar(20)
,`sname` varchar(10)
,`ssex` varchar(2)
,`reward` varchar(100)
,`punishment` varchar(100)
);

-- --------------------------------------------------------

--
-- 表的结构 `major`
--

CREATE TABLE `major` (
  `mno` varchar(5) NOT NULL,
  `mname` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `major`
--

INSERT INTO `major` (`mno`, `mname`) VALUES
('m001', '经济学专业'),
('m002', '英文专业'),
('m003', '数学专业');

-- --------------------------------------------------------

--
-- 表的结构 `student`
--

CREATE TABLE `student` (
  `sno` varchar(20) NOT NULL,
  `sname` varchar(10) NOT NULL,
  `ssex` varchar(2) NOT NULL,
  `sage` int(4) NOT NULL,
  `sclass` varchar(10) NOT NULL,
  `intime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `student`
--

INSERT INTO `student` (`sno`, `sname`, `ssex`, `sage`, `sclass`, `intime`) VALUES
('201632120710', '马花藤', '男', 23, '数学1601', '2016-09-01 00:00:00'),
('201632120711', '马晕', '男', 23, '数学1601', '2016-09-01 00:00:00'),
('201632120778', '李晓龙', '男', 21, '数学1601', '2016-09-01 00:00:00'),
('201732120762', '鲁智深', '男', 21, '经管1701', '2017-09-01 00:00:00'),
('201732120768', '李云隆', '男', 21, '数学1701', '2017-09-01 00:00:00'),
('201732120777', '张晓梅', '女', 20, '经管1701', '2017-09-01 00:00:00'),
('201832120719', '孙文空', '女', 19, '英语1801', '2018-09-01 00:00:00'),
('201832120779', '黄飞红', '女', 20, '英语1801', '2018-09-01 00:00:00'),
('201932120720', '张阿红', '女', 19, '英语1901', '2019-09-01 00:00:00'),
('202005', 'smile', '男', 19, '计科三班', '2006-04-30 00:00:00'),
('202006', 'xion', '男', 19, '夹克', '1002-03-04 00:00:00'),
('202006010300', 'zhangsan', '男', 19, '计科三班', '2001-01-01 00:00:00'),
('张三s', '2022320', '男', 20, '计科三班', '2020-01-03 00:00:00');

-- --------------------------------------------------------

--
-- 替换视图以便查看 `student_view`
-- （参见下面的实际视图）
--
CREATE TABLE `student_view` (
`username` varchar(20)
,`passward` varchar(20)
);

-- --------------------------------------------------------

--
-- 表的结构 `stu_course`
--

CREATE TABLE `stu_course` (
  `sno` varchar(20) NOT NULL,
  `cno` varchar(10) NOT NULL,
  `grade` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `stu_course`
--

INSERT INTO `stu_course` (`sno`, `cno`, `grade`) VALUES
('201632120778', 'c004', NULL),
('201632120778', 'c005', NULL),
('201732120762', 'c002', 80),
('201732120768', 'c004', 70),
('201732120777', 'c001', NULL),
('201732120777', 'c002', NULL),
('201832120719', 'c003', 90),
('201832120719', 'c006', 92),
('201832120779', 'c003', NULL),
('202006010300', 'c002', 100);

-- --------------------------------------------------------

--
-- 表的结构 `stu_reward_punishment`
--

CREATE TABLE `stu_reward_punishment` (
  `sno` varchar(20) NOT NULL,
  `reward` varchar(100) DEFAULT NULL,
  `punishment` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `stu_reward_punishment`
--

INSERT INTO `stu_reward_punishment` (`sno`, `reward`, `punishment`) VALUES
('201732120777', '校一等奖学金', NULL),
('201732120777', NULL, '全校通告批评'),
('201632120711', NULL, '校一等奖学金'),
('202006010328', 'student good', 'lose off'),
('202006010300', '', 'shi拾金不昧'),
('202006010300', '拾金不昧，乐于助人', ''),
('q', '', '');

-- --------------------------------------------------------

--
-- 表的结构 `teacher`
--

CREATE TABLE `teacher` (
  `tno` varchar(20) NOT NULL,
  `tname` varchar(10) NOT NULL,
  `tsex` varchar(2) NOT NULL,
  `tphone` varchar(20) NOT NULL,
  `dmpno` varchar(10) NOT NULL,
  `profess` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `teacher`
--

INSERT INTO `teacher` (`tno`, `tname`, `tsex`, `tphone`, `dmpno`, `profess`) VALUES
('123110', '唐伯虎', '男', '17398443912', 'd003', '副教授'),
('123122', '谭英文', '男', '17398442121', 'd002', '副教授'),
('123123', '陈读', '男', '17398447611', 'd001', '副教授'),
('123124', '韩宏', '女', '17398440222', 'd001', '教授'),
('123125', '马冬梅', '女', '17398449123', 'd002', '副教授');

-- --------------------------------------------------------

--
-- 表的结构 `teacher_course`
--

CREATE TABLE `teacher_course` (
  `tno` varchar(10) NOT NULL,
  `cno` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `teacher_course`
--

INSERT INTO `teacher_course` (`tno`, `cno`) VALUES
('123110', 'c004'),
('123110', 'c005'),
('123122', 'c006'),
('123123', 'c001'),
('123124', 'c002'),
('123125', 'c003');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `sno` varchar(30) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `datetime` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`sno`, `passwd`, `datetime`) VALUES
('123', '100194f21335f4e54702743200efbc4f', '2021-12-14 16:57:38'),
('admin', '9b5baf50301fee45547921e1fc391a94', '2021-12-12 22:21:34'),
('ali', '100194f21335f4e54702743200efbc4f', '2021-12-14 11:51:12'),
('asd', '100194f21335f4e54702743200efbc4f', '2021-12-14 17:16:40'),
('dsa', '100194f21335f4e54702743200efbc4f', '2021-12-14 17:11:27'),
('fsad', '100194f21335f4e54702743200efbc4f', '2021-12-14 17:00:08'),
('huangjialong', 'c4a92efe42cbe3b2ea0fb45619532404', '2021-12-14 10:22:08'),
('lisa', '904c3ce001f043a6ee3d3b83c52fa377', '2021-12-14 11:44:54'),
('qwer', '74887795913449bf15cd5fa1ce5bda8f', '2021-12-13 21:45:32'),
('sd', '100194f21335f4e54702743200efbc4f', '2021-12-14 12:34:21'),
('sda', '2ae7a2005507312383f0a2872827b91b', '2021-12-14 16:41:12'),
('smiel', 'e08809ae9a4b1d5e0e953c3b256a806d', '2021-12-13 23:25:48'),
('smil', '100194f21335f4e54702743200efbc4f', '2021-12-14 16:55:37'),
('smile', 'eb2568407f7a9e22a03eba7c4261a142', '2021-12-12 22:13:50'),
('smkle', '100194f21335f4e54702743200efbc4f', '2021-12-14 11:52:00'),
('studen', '9b5baf50301fee45547921e1fc391a94', '2021-12-14 11:56:40'),
('student', '11111111', '2021-12-12 22:11:59'),
('wuyunl', '904c3ce001f043a6ee3d3b83c52fa377', '2021-12-14 00:19:22'),
('xion', '100194f21335f4e54702743200efbc4f', '2021-12-13 10:57:26'),
('xiong', '28b40207ddd95cca27d450ad8752f9b7', '2021-12-12 22:44:29');

-- --------------------------------------------------------

--
-- 视图结构 `jxj`
--
DROP TABLE IF EXISTS `jxj`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `jxj`  AS SELECT `a`.`sno` AS `sno`, `a`.`sname` AS `sname`, `a`.`ssex` AS `ssex`, `b`.`reward` AS `reward`, `b`.`punishment` AS `punishment` FROM (`student` `a` join `stu_reward_punishment` `b` on((`a`.`sno` = `b`.`sno`))) ;

-- --------------------------------------------------------

--
-- 视图结构 `jxjf`
--
DROP TABLE IF EXISTS `jxjf`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `jxjf`  AS SELECT `a`.`sno` AS `sno`, `a`.`sname` AS `sname`, `a`.`ssex` AS `ssex`, `b`.`reward` AS `reward`, `b`.`punishment` AS `punishment` FROM (`student` `a` join `stu_reward_punishment` `b` on((`a`.`sno` = `b`.`sno`))) WHERE (`a`.`ssex` = '女') ;

-- --------------------------------------------------------

--
-- 视图结构 `jxjm`
--
DROP TABLE IF EXISTS `jxjm`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `jxjm`  AS SELECT `a`.`sno` AS `sno`, `a`.`sname` AS `sname`, `a`.`ssex` AS `ssex`, `b`.`reward` AS `reward`, `b`.`punishment` AS `punishment` FROM (`student` `a` join `stu_reward_punishment` `b` on((`a`.`sno` = `b`.`sno`))) WHERE (`a`.`ssex` = '男') ;

-- --------------------------------------------------------

--
-- 视图结构 `student_view`
--
DROP TABLE IF EXISTS `student_view`;

CREATE ALGORITHM=UNDEFINED DEFINER=`smile`@`%` SQL SECURITY DEFINER VIEW `student_view`  AS SELECT `account`.`username` AS `username`, `account`.`passward` AS `passward` FROM `account` ;

--
-- 转储表的索引
--

--
-- 表的索引 `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`username`);

--
-- 表的索引 `class_stu_num`
--
ALTER TABLE `class_stu_num`
  ADD PRIMARY KEY (`class`);

--
-- 表的索引 `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`cno`);

--
-- 表的索引 `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`dmpno`);

--
-- 表的索引 `major`
--
ALTER TABLE `major`
  ADD PRIMARY KEY (`mno`,`mname`);

--
-- 表的索引 `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`sno`);

--
-- 表的索引 `stu_course`
--
ALTER TABLE `stu_course`
  ADD PRIMARY KEY (`sno`,`cno`);

--
-- 表的索引 `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`tno`);

--
-- 表的索引 `teacher_course`
--
ALTER TABLE `teacher_course`
  ADD PRIMARY KEY (`tno`,`cno`);

--
-- 表的索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`sno`),
  ADD UNIQUE KEY `sno` (`sno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
