#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

searchdir = sys.argv[1]

currentdir = os.getcwd()

dirs = {
    'photos' : {
        'jpg' : ['jpg', 'jpeg'],
        'png' : ['png'],
        'gif' : ['gif', 'giff'],
        'bmp' : ['bmp'],
        'tif' : ['tif', 'tiff'],
        'ico' : ['ico'],
    },
    'videos' : {
        'mp4' : ['mp4'],
        'mpg' : ['mpg'],
        'mov' : ['mov'],
        '3gp' : ['3gp'],
        'avi' : ['avi'],
        'mkv' : ['mkv'],
        'wmv' : ['wmv'],
    },
    'sounds' : {
        'mp3' : ['mp3'],
        'wma' : ['wma'],
        'ogg' : ['ogg'],
        'wav' : ['wav'],
        'flac' : ['flac'],
    },
    'documents' : {
        'pdf' : ['pdf'],
        'txt' : ['txt'],
        'doc' : ['doc', 'docx'],
        'rtf' : ['rtf'],
        'xls' : ['xls', 'xlsx'],
        'ppt' : ['ppt', 'pptx'],
    },
    'compressed' : {
        'zip' : ['zip'],
    },
}

# mappaszerkezet létrehozása dirs tömb alapján az aktuális mappában ahonnan elindítottuk a programot
for maindir in sorted(dirs):
    for subdir in sorted(dirs[maindir]):
        actdir = "./" + maindir + "/" + subdir
        if not os.path.exists(actdir):
            os.makedirs(actdir)

# az argumentumban megadott mappában kikeressük a fájltípusokat és berakjuk a mappájukba a tömb alapján
for maindir in sorted(dirs):
    print "=================================================="
    for subdir in sorted(dirs[maindir]):
        actdir = currentdir + "/" + maindir + "/" + subdir
        print actdir
        print "--------------------------------------------------"
        for extension in sorted(dirs[maindir][subdir]):
            print searchdir + ": " + extension
            runcommand = "find " + searchdir + " -type f -iname \"*." + extension + "\" -exec mv -t " + actdir + " {} +"
            subprocess.call(runcommand, shell=True)
        print "=================================================="

# üres mappák törlése a cél helyen
runcommand = "find " + currentdir + " -type d -empty -exec rmdir {} +"
subprocess.call(runcommand, shell=True)

# üres mappák törlése a forrás helyen
runcommand = "find " + searchdir + " -type d -empty -exec rmdir {} +"
subprocess.call(runcommand, shell=True)

# jpeg és jpg fájlok átnevezése exiv információk alapján
runcommand = "find " + currentdir + " -type f -iname \"*.jpg\" -exec exiv2 -F rename {} +"
subprocess.call(runcommand, shell=True)
runcommand = "find " + currentdir + " -type f -iname \"*.jpeg\" -exec exiv2 -F rename {} +"
subprocess.call(runcommand, shell=True)
