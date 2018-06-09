#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding：utf-8 -*-
import requests
import base64
import json
import time
import re
import cv2


headers = {

    'Cookie': 'ai_user=uut7K|2017-10-16T14:16:02.566Z; ARRAffinity=971565e831284c472c09655716ccf45d6d577de23b2633987894fb6dce28ce0b; cpid=YDNcNiAzPzJdSlZKfjHXMDK0aE0aNl5KIE1GSFlPVEpOAA; salt=81248E5E9CEED490A0CD58A326784414; ai_session=prA/E|1508165302518|1508165316640.13',
    'Host': 'kan.msxiaobing.com',
    'Origin': 'https://kan.msxiaobing.com',
    'Referer': 'https://kan.msxiaobing.com/ImageGame/Portal?task=yanzhi&feid=07df05287adb22e58c13232a9e4ffcae',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
proxies = {
    "http":"http://27.40.128.35:61234",
"http":"http://182.110.222.172:61234",
"http":"http://121.196.218.197:3128",
"http":"http://122.114.31.177:808",
"http":"http://119.10.67.144:808",
"http":"http://61.135.217.7:80",
"http":"http://115.28.90.79:9001",
"http":"http://123.57.207.2:3128",
"http":"http://111.121.193.214:3128",
"http":"http://123.57.217.208:3128",
"http":"http://114.212.12.4:3128",
"http":"http://218.14.115.211:3128",
"http":"http://114.215.95.188:3128",

}


def get_face():
    face_patterns = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    sample_image = cv2.imread('girl.jpg')
    faces = face_patterns.detectMultiScale(sample_image,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100))
    if len(faces) >= 1:
        for (x, y, w, h) in faces:
            # cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # 提取人脸位置
            crop = sample_image[y:y+h, x:x+w]
            cv2.imwrite('find.jpg', crop)
        # cv2.imwrite('find.jpg', sample_image)

        f = open('find.jpg', 'rb')
        ls_f = base64.b64encode(f.read())
        url = 'http://kan.msxiaobing.com/Api/Image/UploadBase64'
        data = ls_f
        find = requests.post(url, data=data)
        j = json.loads(find.content)
        imgur = j['Host'] + j['Url']
        url2 = 'https://kan.msxiaobing.com/Api/ImageAnalyze/Process?service=yanzhi&tid=05a171e52cc74f2294345fcb5c5c464b'
        data = {
            'Content[imageUrl]': imgur,
            'CreateTime': time.time(),
        }
        finds = requests.post(url2, headers=headers, data=data, proxies=proxies)
        try:
            js = json.loads(finds.text)
            ttx = js['content']['text']
            nums = re.sub(r'\D', "", ttx)
            print([ttx, nums])
            time.sleep(2)
            if int(nums) >= 70:
                return 1
            else:
                return 0
        except:
            return 3
    else:
        print('没有发现人脸！！')
        return 8




if __name__ == '__main__':
    get_face()


