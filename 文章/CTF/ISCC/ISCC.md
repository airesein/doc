```
adb devices #列出当前连接的所有设备。
adb connect 127.0.0.1:16384
adb install <path_to_apk> #将指定的APK文件安装到设备上。
adb shell #进入设备或模拟器的Linux shell环境，可以执行各种Linux命令。

adb push <本机路径> <模拟器路径> #把电脑上的文件传到模拟器上。
adb pull <模拟器路径> <本机路径> #把模拟器上的文件下载到电脑上。

adb push example.txt /sdcard/ #把当前目录的example.txt传到/sdcard/目录下。
```

```
直接启动：./frida-server
启动到后台：./frida-server -D

cd /data/local/tmp
frida -U -f "com.example.mobile01" -l .\frida.py
```

