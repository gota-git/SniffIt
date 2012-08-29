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

import args
import sys

import dictionary
import downloadData

def main(argv):
    args.parse.parse_args(argv,args.Args)
    dic = dictionary.Dictionary()
    urls = dic.readUrls(args.Args.dictionary, args.Args.url)
    downloading = downloadData.DownloadData()
    if args.Args.reachAble:
        reachAbleUrls = downloading.getReachAbleUrls(urls, args.Args.timeOut)
        print "reachable URLs :"
        for i in range(len(reachAbleUrls)):
            print reachAbleUrls[i]
    else:
        downloading.setThreadNum(args.Args.threadNum)
        downloading.downloadData(args.Args.url,args.Args.location,urls,args.Args.timeOut)

if __name__ == "__main__":
    main(sys.argv[1:])
    #main("-u 127.0.0.1 -l ./D -d config -t 1 -T 2".split())
    #main("-r -d config ".split())