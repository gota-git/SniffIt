#!/usr/bin/env python
#_*_ utf-8 _*_

#    Copyright (c) 2012 Gotaly (gotawork@gmail.com)
#    License: GNU GPLv3
#
#    This file is part of SniffIt.
#    
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.  See the GNU General Public License 
#    for more details.
#


import urllib2
import urllib
import Queue
import threading
import os

class PullDataThread(threading.Thread):
    """ The read download thread with urllib
    Use urllib.retrieve to donwload file
    """
    def __init__(self,rootPath,rootUrl,urlsQueue):
        threading.Thread.__init__(self)
        self.rootPath = rootPath
        self.rootUrl = rootUrl
        self.urlsQueue = urlsQueue
        self.perfix = "http://"

        
       
    def getFileName(self,url):
        """ drop off http:// and rootUrl to be filenme with rootPaht """
        filename = url.replace(self.perfix+self.rootUrl,'')
        if self.rootPath[-1:] == '/' :
            self.rootPath = self.rootPath[:-1]
        filename = self.rootPath + filename
        filePath = os.path.dirname(filename)
        if not os.path.exists(filePath):
            try:
                os.makedirs(filePath)
            except WindowsError:
                pass
        return filename
    
    def retrieveCB(self,blockNum,blockSize,fileSize):
        if fileSize == 0:
            schedule = 100
        else:
            schedule =int( (blockNum * blockSize *1.0 /fileSize)*100)
        if schedule>100:
            schedule = 100
        print "Downloading ",self.url, "*" *schedule," Shedule:",str(schedule)+"%"
    
    def run(self):
        while True:
            self.url = self.urlsQueue.get()
            filename = self.getFileName(self.url)
            urllib.urlretrieve(self.url,filename,self.retrieveCB)
            print "Done"
            self.urlsQueue.task_done()

class DownloadData:
    """ Interface of download
    Use a thread pool with queue to download files 
    You can set how many thread to run 
    """
    
    def __init__(self):
        self.urls = []
        self.threadNum =3

        
    def setThreadNum(self,num):
        self.threadNum = num
     
    def reachAble(self,url,timeOut):
        """ Test if url can be reaching in timeOut """
        req = urllib2.Request(url)
        try:
            urllib2.urlopen(url=req,timeout=timeOut)
            return True
        except :
            return False
    
    def getReachAbleUrls(self,urls,timeOut):
        """ return reacheable urls """
        reachAbleUrls = []
        for i in range(len(urls)):
            if  self.reachAble(urls[i],timeOut):
                reachAbleUrls.append(urls[i])
        return reachAbleUrls
    
    def downloadData(self,rootUrl,rootPath,urls,timeOut):        
        urlsQueue= Queue.Queue()
        for i in range(len(urls)):
            if  not self.reachAble(urls[i],timeOut):
                continue
            self.urls.append(urls[i])
        for i in range(self.threadNum):
            t = PullDataThread(rootPath,rootUrl,urlsQueue)
            t.setDaemon(True)
            t.start()
        
        for i in range(len(self.urls)):
            urlsQueue.put(self.urls[i])
            
        urlsQueue.join()    

    
if __name__ == "__main__":
    PD = DownloadData()    
    print PD.getReachAbleUrls(1)
