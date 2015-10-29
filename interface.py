#!/usr/amin/python
import os
import runpy
import sys
import time
import tempfile

cwd = os.getcwd()
tempdir = tempfile.gettempdir()
localtime = time.localtime(time.time())
fname = time.strftime("%Y%m%d_%H%M%S",localtime)

args = sys.argv

try:
        if sys.argv.isgetdata:
                while 1:
                        try:
                                runpy.run_module("src/epoc_sensor")
                        except:
                                break
                os.system("killall -v gnuplot_x11")
                os.system("cp %s/epoc_data %s/EPOC_%s" %(tempdir,cwd,fname))
                os.remove("%s/epoc_data"%tempdir)
                for foo in args.tempfiles:
                        os.remove(foo)
except Exception,e:
        print "error executing function ..."
        print "error message: %s ..."%e
