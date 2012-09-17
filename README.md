
    Copyright (c) 2012 Gotaly (gotawork@gmail.com)
    License: GNU GPLv3

    SniffIt
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.  See the GNU General Public License 
    for more details.

# 介绍
采用Python实现的一个根据给定的字典内容进行推测url并进行下载的小工具
其使用了urllib.retrieve，并创建线程池进行并行下载。
#字典格式
[Keys] 部分内容存放的是文件名，不包含后缀
[Suffix] 部分内容是文件的后缀名
[DirLayer n]是目录的层数，每层包含的目录名，对其进行重新组合形成url。
每部分以空行结束

一个实例：

	[Suffix]
	html	
	htm
	jsp
	php
	asp
	pdf

	[Keys]
	index	
	login
	ebook
	
	[DirLayer 0]
	wordpress
	images

	[DirLayer 1]
	inc
	core
#使用示例
如果我想获取地址www.printhello.org下面的一级目录为wordpress或images，二级目录为
inc或者core，文件名为index , login或ebook，后缀为html ,htm,jsp,php
,asp,pdf的文件,可以使用上述字典文件。然后运行命令

	./sniffit  -r -d test.dict -t 1
可以看到 http://127.0.0.1
目录下符合上述条件的合法且可以访问的url。其中-r选项表示列出可到达(reachable）的url。
-d选项指定了字典文件；-t选项指定判断url是否可用的超时时间。
可以使用-u选项指定根url，默认是127.0.0.1,url无需加上"http://",如探测www.b.com下面的
相同文件，可以在上面的基础上加上 "-u www.b.com"

如果还想将相关的文件下载下来，可以使用-l指定下载保存的根目录。如：

	./sniffit  -u 127.0.0.1 -l ./www -d test.dict  -t 1 


将会把服务器根目录下符合条件的文件下载到./www目录下。

	


	
