#!/usr/bin/env python
# -*- coding: utf-8 -*-
import TencentYoutuyun
import cv2
'''
必看：
1.安装腾讯优图
git clone https://github.com/Tencent-YouTu/Python_sdk.git
cd Python_sdk
python setup.py install
2.在http://open.youtu.qq.com/创建应用，得到下面的参数
'''

# 这是我申请的，可能次数会用完，建议自己申请一个
appid = '10102833'
secret_id = 'AKIDb2GNFrSJ9j8HAn8JBtLegV6SZR8a5oa6'
secret_key = 'PYk8HBqKZZNxIOEqCI7gzGH2XnnW0EJC'
userid = '44'


def meizi():
    # 处理图片是否含有人脸
    face_patterns = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    sample_image = cv2.imread('girl.jpg')
    faces = face_patterns.detectMultiScale(sample_image,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100))
    if len(faces) >= 1:
        for (x, y, w, h) in faces:
            # cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # 提取人脸位置
            crop = sample_image[y:y+h, x:x+w]
            cv2.imwrite('find.jpg', crop)

        # 对人脸颜值进行打分
        end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
        youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
        ret = youtu.DetectFace('find.jpg', mode=0,data_type=0)
        for j in ret["face"]:
            if j["gender"] > 50:
                print("性别:男")
                print("滚，下一个")
            else:
                print("性别:女")
                print("妹子的年龄:",j["age"])
                print("妹子的颜值:",j["beauty"])
                fen = j["beauty"]
				# 这个看你需求调啦
                if fen >= 70:
                    return 1
    else:
        return 0
