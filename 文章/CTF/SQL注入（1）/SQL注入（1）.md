# mysql

```sql
创建数据库test
CREATE DATABASE test;
显示所有的数据库
SHOW DATABASES;
删除test数据库
DROP DATABASE test;

创建一个表test
CREATE TABLE test(
	id INT,
	NAME VARCHAR(100),
	age int
);
查看test表结构
DESC test;
为test表增加一个email字段
ALTER TABLE test ADD email VARCHAR(50);
为test表删除一个eamli字段
ALTER TABLE test DROP email;
将test表中的NAME字段改名为full_name
ALTER TABLE test RENAME column NAME TO full_name;
将test表中的age字段属性改为SMALLINT
ALTER TABLE test MODIFY COLUMN age SMALLINT;
将test表中的age字段设置默认
ALTER TABLE test MODIFY COLUMN age SMALLINT;
```

