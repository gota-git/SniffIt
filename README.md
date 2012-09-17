
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

