#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import sys

def rad_linux_amd64(target):
    print("\r\n[+] 使用 rad_linux_amd64 进行扫描")
    cmd = "./rad_linux_amd64 --target {}".format(target,"target-rad.txt")#--http-proxy
    os.system(cmd)

def crawlergo(target):
    print("\r\n[+] 使用 crawlergo 进行扫描")
    cmd = "./crawlergo -c /usr/bin/chromium -t 10 --robots-path --fuzz-path "+target
    os.system(cmd)

def dirsearch(target):
    print("\r\n[+] 使用 dirsearch 进行扫描")
    cmd = "python3 dirsearch/dirsearch.py -u {} ".format(target)
    os.system(cmd)

def jsfinder(target):
    print("\r\n[+] 使用 jsfinder 进行扫描")
    cmd = "python3 JSFinder.py -u {} -d ".format(target)
    os.system(cmd)

def packerfuzzer(target):
    print("\r\n[+] 使用 packerfuzzer 进行扫描")
    cmd = "python3 Packer-Fuzzer/PackerFuzzer.py -l en -u {} -r html".format(target)
    os.system(cmd)

def main():
    target = sys.argv[1]
    print("\r\n即将开启对[ "+ target+ " ]的扫描")
    target = str(target)
    rad_linux_amd64(target)  
    crawlergo(target)
    jsfinder(target)
    packerfuzzer(target)
    dirsearch(target)
    print("\r\n对[ "+ target+ " ]的扫描结束")

if __name__ == "__main__":
    main()
