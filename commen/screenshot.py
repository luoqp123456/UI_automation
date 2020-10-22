# -*- coding:utf-8 -*-
import os
import time
import traceback
from config.config import prj_path, picture_path


def currentdate():
    '''生成当前日期字符串'''
    date = time.localtime()
    return '-'.join([str(date.tm_year), str(date.tm_mon), str(date.tm_mday)])


def currenttime():
    '''生成当前时间字符串'''
    date = time.localtime()
    return '-'.join([str(date.tm_hour), str(date.tm_min), str(date.tm_sec)])


def createdir():
    '''创建当前日期和当前时间目录'''
    path = os.path.dirname(os.path.abspath(__file__))
    datedir = os.path.join(path, currentdate())
    # 如果当前日期目录不存的话就创建
    if not os.path.exists(datedir):
        os.mkdir(datedir)
    timedir = os.path.join(datedir, createdir())
    # 如果当前时间目录不存的话就创建
    if not os.path.exists(timedir):
        os.mkdir(timedir)
    return timedir


def takescreenshot(driver, picture_name):
    picture = os.path.join(picture_path, picture_name + '.png')
    try:
        driver.get_screenshot_as_file(picture)
    except Exception as e:
        print(traceback.print_exc())

