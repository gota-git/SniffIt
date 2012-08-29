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

# Use argparse instead of optparse

import argparse

class Args:
    pass

parse = argparse.ArgumentParser(description = """
            +*+    Sniff It +*+
                                """
                                ,formatter_class = argparse.RawDescriptionHelpFormatter
                                ,prog = "sniffit"                               
                                )

parse.add_argument("-u","--url"
                   ,default = "127.0.0.1"
                   ,metavar = "url"
                   ,dest = "url"
                   ,help = "url to be sniff .Need not contain 'http://' "
                   )

parse.add_argument("-l","--location"
                   ,default = "./"
                   ,metavar = "location"
                   ,dest = "location"
                   ,help = "location to be store in loccal machine "
                   )

parse.add_argument("-d","--dictionary"
                   ,default = "./config.dict"
                   ,metavar = "dictionary"
                   ,dest = "dictionary"
                   ,help = "location and file name of dictionary "
                   )

parse.add_argument("-t","--time"
                   ,type = int
                   ,default =1
                   ,metavar = "timeOut"
                   ,dest = "timeOut"
                   ,help = "timeOut to connect by seconds "
                   )

parse.add_argument("-T","--threadNum"
                   ,type = int
                   ,default =1
                   ,metavar = "threadNum"
                   ,dest = "threadNum"
                   ,help = "open threadNum thread to donwload "
                   )
parse.add_argument("-r","--reachAble"
                   ,action = "store_true"
                   ,dest = "reachAble"
                   ,help = "Show reachAble urls "
                   )

