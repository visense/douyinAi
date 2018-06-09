#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
# 爬取视频需要用
# from selenium import webdriver
import time
import re
from face import get_face
from Ai import meizi

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


def get_img():
    os.system('adb shell screencap -p /sdcard/girl.jpg')
    os.system('adb pull /sdcard/girl.jpg')


# 获取视频的id
def get_mv_id():
    driver = webdriver.Chrome()
    url = 'https://www.douyin.com/share/user/95535317253/?share_type=link'
    driver.get(url)
    html = driver.page_source
    id_list = re.findall('data-id="(.*?)"', html)[1:]
    for id in id_list:
        get_mv(id)


# 获取视频下载链接
def get_mv(id):
    url = 'https://www.iesdouyin.com/share/video/{}'.format(id)
    html = requests.get(url, headers=headers).text
    video_url = re.findall('playAddr: "(.*?)",', html)[0]
    print(video_url)


# 点赞
def get_zan():
    os.system('adb shell input swipe 971 960 971 960')


# 点击下一页
def get_xia():
    os.system('adb shell input touchscreen swipe 400 1200 500 800')


# 点击关注
def get_zhu():
    os.system('adb shell input swipe 983 812 983 812')


def get_my_face():
    # 微软小冰接口，调用次数有限
    # id = get_face()
    # 腾讯优图接口，详情配置看Ai文件
    id = meizi()
    if id == 1:
        get_zhu()
        get_zan()
        print("小姐姐好漂亮，已经点击关注")
        get_xia()
    else:
        get_xia()


if __name__ == '__main__':
    a = 1
    # 找小姐姐
    while a:
        print('正在检测第{}个视频。'.format(a))
        print(50 * '==')
        get_img()
        get_my_face()
        time.sleep(2)
        print(50 * '==')
        a += 1
    # 爬取视频
    # get_mv_id()
