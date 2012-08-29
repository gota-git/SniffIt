#
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

import re
import sys
import os

class Dictionary:
    """ Read your dictionary.Produce urls
        Read suffix,dirctions,key valuse in dictionary file
        combine them into a url 
    """
    def __init__(self):
        self.config = {}
        self.dicPath = None
        self.pathes = []
        self.urls = []
        self.maxDeep = 0
        self.prefix = "http://"
     
    def setPrefix(self,prefix):
        self.prefix=prefix
    
  
    def getCategory(self,sourceStr):
        """ Get category form dictinary file """
        dicConfKey = r"\[(( *Keys *)|( *Suffix *)|( *DirLayer *[0-9]* *))\]"
        pat = re.compile(dicConfKey)
        matchObj = re.match(pat,sourceStr)
        if not matchObj:
            return None
        return re.sub(r" +",' ',matchObj.string[1:-1].strip())
     
    def readConf(self,confFile):
        """ Read dictinary file to produce config dictionary """
        inCategory = False 
        if not os.path.exists(confFile):
            print "Error,Please check your dictionary file"
            sys.exit(-1)  
        fd = open(confFile,'r')
        
        category = None
        while True:
            line = fd.readline()
            if not line :
                break
            line = line.strip()
            if not inCategory:
                category = self.getCategory(line)
                if not category:
                    continue
                if self.config.has_key(category):
                        pass
                else:
                    self.config[category] = []
                inCategory = True
                continue
            if not line:
                inCategory = False
                continue
            self.config[category].append(line)
            
        self.maxDeep = len(self.config) -3 
    
    def getKeys(self,numOfX):
        pass
      
    def getPathes(self,path,deep):
        """ Use a tail recursion to combine path in different dirction layers """
        k = "DirLayer "+str(deep)

        for i in range(len(self.config[k])):
            tmpPath = path + '/' +self.config[k][i]
            self.pathes.append(tmpPath)
            if deep<self.maxDeep:
                self.getPathes(tmpPath,deep+1)
       

    def getUrls(self,rootUrl):
        """ combine path ,key values,suffix to a url """
        
        if '/' == rootUrl[-1:]:
            rootUrl = rootUrl[:-1]
        
        self.pathes.append("")
        for i in range(len(self.pathes)):
            for j in range(len(self.config["Keys"])):
                for k in range(len(self.config["Suffix"])):
                    self.urls.append(self.prefix+rootUrl+self.pathes[i]+'/'+self.config["Keys"][j]+'.'+self.config["Suffix"][k])

                    
    def readUrls(self,dictFile,rootUrl):
        """ Return all urls with root path "rootPath" produced by dictionary file"""
        self.readConf(dictFile)        
        self.getPathes('',0)
        self.getUrls(rootUrl) 
        return self.urls  
        
    def info(self):
        self.readConf("config")
        print self.config  
        self.getPathes('',0)
        self.getUrls("www.baidu.com")   
        print self.pathes    
        print self.urls
        

if __name__  == "__main__" :         
    dic = Dictionary()
    dic.info()