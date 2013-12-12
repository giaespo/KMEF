#!/usr/bin/python3
import sys
import os

def GetAppPath():
    DIR_APPS = 'archiflowKM'        # Correct the folder name if necessary!
    app_path = ''
    path_list = sys.path
    for d in path_list:
        idx = d.rfind(DIR_APPS)
        if idx != -1:
            app_path = d[:idx+len(DIR_APPS)] + '/'
    return app_path


    
appFolder=GetAppPath()#"/archiflowKM/"
#appFolder="/var/www/cgi-bin/datas3/archiflowKM/"


tmpFolder="app/tmp/"

