## DOWNLOAD SCRIPT ##
import urllib2
from urllib2 import Request, urlopen, URLError
# # '''import requests
# # response = requests.get("ftp://results.cal.ci.spirentcom.com/smt/SCMSmartTest/9.90/BLL0523_IL0523/STR-RTP-Weekend-Scaling-SYS-MultiSpeed%20-%202017.10.15@3.32.13/fx3-apo-25g-t-2/TC3--TH_B2B_DataCenter_Port_Scal.tcl/")
# #
# # temp = response.content
# #
# # print ("Details:", temp)'''
#
import urllib
import os
from bs4 import BeautifulSoup
import zipfile,fnmatch,os

import os, shutil, re, glob
from os.path import isfile, join
from os import walk
import shutil
from flask import session
# import socket
# # socket.getaddrinfo('localhost', 8080)
#
#
from py1 import pvalue



def running_script(rootPath):
 os.chdir("E:")
 cwd= os.getcwd()
 print(cwd)
 #name = session['uname']
 newdir = cwd + "\\mahalakshmi"
 pvalue = 10
 #newdir = cwd+session['uname']
 print "The current Working directory is " + cwd
 if(os.path.exists(newdir)):
     shutil.rmtree(newdir,True)
 os.mkdir(newdir);
 print "Created new directory " + newdir
 newfile = open(newdir+'\\zipfilelinks.txt','w')
 print newfile


 print "Running script.. "

 url = "http://10.66.237.55:8080"
 page = urllib2.urlopen(rootPath).read()
 extension = ".tcl"

 soup = BeautifulSoup(page, "html5lib")
 soup.prettify()


 for anchor in soup.findAll('a', href=True):
     links =  anchor['href']
     if links.endswith(extension):
        newfile.write(links+ '\n')
 newfile.close()

 pvalue = 40
 newfile = open(newdir+'\\zipfilelinks.txt', 'r')
 for line in newfile:
     print line + '/n'
 newfile.close()


 with open(newdir+'\\zipfilelinks.txt', 'r') as url:
     for line in url:
         if line:

             try:
                ziplink = line.replace('.tcl','.tcl\\'+((line.split('\\')[-1]).replace('.tcl','.tcl.zip')))
                zipfiles = ziplink.rsplit('\\',1)[1]
                print(zipfiles)
                zipfile2 = zipfiles.rsplit('.',1)[0]
                print(zipfile2)
                print "Trying to reach " + ziplink
                # ziplink='ftp:///\results.cal.ci.spirentcom.com\smt\SCMSmartTest\9.90\BLL0523_IL0523\STR-RTP-Weekend-Scaling-SYS-MultiSpeed - 2017.10.15@3.32.13\fx3-apo-25g-t-2\TC3--TH_B2B_DataCenter_Port_Scal.tcl'

                response = urllib2.urlopen(ziplink)
             except URLError as e:

                    print  'failed to reach a server.'+ziplink
                    if hasattr(e, 'reason'):
                      print 'Reason: ', e.reason
                      continue
                    elif hasattr(e, 'code'):
                      print 'The server couldnt fulfill the request.'
                    print 'Error code: ', e.code
                    continue
             else:
                zipcontent = response.read()
                completeName = os.path.join(newdir,zipfile2+".zip")
                print(completeName)
                with open (completeName, 'wb') as f:
                    print "downloading.. " + zipfiles
                    f.write(zipcontent)
                    f.close()
                    print "Script completed"

 cwd = os.getcwd()
 print(cwd)
 pvalue = 70
 # uname = session['uname']
 # rootPath = cwd + uname
 rootPath = cwd + "\\mahalakshmi"
 pattern = '*.zip'
 for root, dirs, files in os.walk(rootPath):
     for filename in fnmatch.filter(files, pattern):
         print(os.path.join(root, filename))
         zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))

     os.chdir(rootPath)
     for file in glob.glob(pattern):
         temp = file.rsplit(".", 1)[0]
         # print (">>>", temp)
         f = open((file.rsplit(".", 1)[0]) + "_ANA.txt", "w")

         f.close()

 ##here folder output
 mypath = rootPath
 newpath = os.path.expanduser(rootPath)
 # filenam = "1.txt"

 f = []
 path = ''
 path1 = []

 for (dirpath, dirnames, filenames) in walk(mypath):
     if isfile(join(mypath, dirpath)):
         path1.extend(join(mypath, dirpath))
     if os.path.isdir(join(mypath, dirpath)):
         for f in filenames:
             path1.append(str(join(mypath, dirpath, f)))

 # newf = open(os.path.join(newpath, filenam ), "w+")

 myarray = {"ERROR", "error"}
 for element in myarray:
     elementstring = ''.join(element)

 for f in path1:
     openfile = open(os.path.join(path, f), "r")
     t1 = re.match(".*(TC(\d)+.*)\\\\.*", f)
     if t1 is not None:
         l1 = t1.group(0).split('\\')
         of = open(l1[3] + "_ANA.txt", "a+")
         of.write("*****" + f + "*****" + "\n")
         for line in openfile:
             if elementstring in line:
                 of.write(line)
         of.write("\n\n\n")
         of.close()
     else:
         print "regex not matched"
     openfile.close()
     print "Completed Runscript..."
     # analyze(url)
 status = True
 ret = status
 print ("runscript>", ret)
 pvalue = 100
 return ret


