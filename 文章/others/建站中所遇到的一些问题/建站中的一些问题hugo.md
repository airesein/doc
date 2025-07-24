---

title: "在建站中遇到的一些问题"

date: 2025-02-11

draft: false

description: "踩过的一些坑"

tags: ["blowfish"]

categories: ["建站"]

---

## zh-cn和zh_cn

 zh-cn和zh_cn平时都大用，一直不知道hugo中还有个标准。对于blowfish主题建议配置和文件名全都用zh-cn，假如在配置中使用了zh_cn，可能会造成无法显示标签、发布时间、主页的“显示更多”。

在此特别感谢[瞳のBlog](https://www.hetong-re4per.com)，当时调试了一天也不知道问题出在哪，后来用他博客的源代码不断试，才发现了这个问题。

## 托管在github上的注意

当把网站发布后会发现有些js会失效，显示`Failed to find a valid digest in the 'integrity' attribute for resource - The resource has been blocked` ，因为git 会对文件进行 `CRLF` 到 `LF` 的转换，导致文件的哈希值变化（好像hugo大都有这个问题）

解决方法：全局禁用

    git config --global core.autocrlf false

## hugo serve的端口bug

在blowfish主题中，在一些特定的条件下（我也不知道咋引起的），使用hugo serve命令查看网页会发现Categories（分类）里面啥都没有，但你把默认端口换一下就有了，换回来又没有了，很神奇！
