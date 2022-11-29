
"use student"
create table if not exists user (
    username varchar(20) primary key,
    passward varchar(20) not null );

insert into user values('student','11111111');

insert into user values('张三','11111111');

insert into user values('李四','11111111');

insert into user values('王五','11111111');
