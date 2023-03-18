use 447_hw2;
set sql_safe_updates = 0;

create table names (
  id integer primary key auto_increment,
  name varchar(255),
  points integer
);