## 闪的好快

![image-20250606233936091](assets/image-20250606233936091.png)

打开后是一个不断变换的git动图，高度好像也缺了

![image-20250606234045442](assets/image-20250606234045442.png)

对git图片进行分解

![image-20250606235638918](assets/image-20250606235638918.png)

写个脚本，对二维码进行逐帧扫描，最后合并

```python
import imageio
from PIL import Image
from pyzbar.pyzbar import decode

def extract_qr_data_from_gif(gif_path):
    gif = imageio.get_reader(gif_path)
    qr_data_list = []

    for frame in gif:
        pil_image = Image.fromarray(frame)

        decoded_objects = decode(pil_image)
        for obj in decoded_objects:
            qr_data_list.append(obj.data.decode('utf-8'))
    
    unique_qr_data = list(qr_data_list)
    combined_data = ''.join(unique_qr_data)
    
    return combined_data

gif_file_path = 'masterGO.gif'
combined_qr_data = extract_qr_data_from_gif(gif_file_path)
print(combined_qr_data)
```

![image-20250606235628580](assets/image-20250606235628580.png)

## come_game

![image-20250607000232585](assets/image-20250607000232585.png)

一个游戏

![image-20250607000405444](assets/image-20250607000405444.png)

![image-20250607000443933](assets/image-20250607000443933.png)

玩一小会后发现多了几个文件

![image-20250607000608381](assets/image-20250607000608381.png)

发现每通过一关后save1都会更改

![image-20250607001016695](assets/image-20250607001016695.png)

第一关卡为31，第二关为32，不断进行更改，当为35时，游戏到达第5关，出现了flag

![image-20250607001145849](assets/image-20250607001145849.png)

## 神秘的文件

![image-20250607001816079](assets/image-20250607001816079.png)

压缩包里嵌压缩包，且第二个压缩包需要密码，明文攻击

![image-20250607001906366](assets/image-20250607001906366.png)

得到密码q1w2e3r4

docx文件打不开，放入010发现开头是504b0304，后缀改为zip打开

![image-20250607004324971](assets/image-20250607004324971.png)

![image-20250607004331728](assets/image-20250607004331728.png)

在里面找到了flag.txt，ZmxhZ3tkMGNYXzFzX3ppUF9maWxlfQ==

base64解码得flag,flag{d0cX_1s_ziP_file}

## 全球最大交友网站

![image-20250607005142440](assets/image-20250607005142440.png)

![image-20250607005305218](assets/image-20250607005305218.png)

下载a.zip，git log查看历史版本

![image-20250607011920512](assets/image-20250607011920512.png)

```reset --hard 6b21737b59806722a89f33d26658b8508ac009e6```回滚

![image-20250607012249956](assets/image-20250607012249956.png)

![image-20250607012344500](assets/image-20250607012344500.png)

## nextGen 1

![image-20250607012615593](assets/image-20250607012615593.png)

![image-20250607012641867](assets/image-20250607012641867.png)

翻译：这只是我们想要开发的用于监控公司各部门的控制面板的第一个版本

试试直接访问```http://49.232.142.230:11835/flag.txt```

![image-20250607012755102](assets/image-20250607012755102.png)

查看主页的源码，发现main.js

```js
function myFunc(eventObj) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("content").innerHTML = xhttp.responseText;
      }
    };
    xhttp.open("POST", '/request');
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send("service=" + this.attributes.link.value);

  }

  var dep = document.getElementsByClassName('department');
  for (var i = 0; i < dep.length; i++) {
    dep[i].addEventListener('click', myFunc);
  }
```

1. **事件监听**：代码首先选择所有 class 为`department`的元素，并为每个元素添加了点击事件监听器`myFunc`。
2. **异步请求**：当点击任意`.department`元素时，`myFunc`函数会被调用，创建一个 XMLHttpRequest 对象并发送 POST 请求到`/request`路径。
3. **数据处理**：请求的参数是从被点击元素的`link`属性获取的，格式为`service=属性值`。
4. **响应处理**：当请求成功返回（状态码 200 且请求完成）时，将响应内容更新到 id 为`content`的 DOM 元素中。



看一下overview

![image-20250607014513277](assets/image-20250607014513277.png)

![image-20250607014518284](assets/image-20250607014518284.png)

请求的是外链,可能有ssrf，file://试试

![image-20250607014751303](assets/image-20250607014751303.png)
