# 自动搜寻抖音漂亮小姐姐

![](https://ws3.sinaimg.cn/large/6f8a2832gy1fk0t83ezlnj21jk111dt4.jpg)

# 一.安装依赖库

	pip install opencv-python
1.就是opencv库的啦，安装失败百度就OK，主要是把它用来提取人脸，减少对腾讯优图的调用次数，haarcascade_frontalface_default.xml这个是人脸提取的数据集，记得放在当前工作目录。

2.安装腾讯优图

	git clone https://github.com/Tencent-YouTu/Python_sdk.git
	cd Python_sdk
	python setup.py install

3.在http://open.youtu.qq.com创建应用，得到下面的参数，详情看Ai文件。

# 二.adb配置

* 将adb这个文件夹加入变量环境，百度就有

# 三.手机连接电脑，打开手机开发者调试模式,每个手机操作不同，百度吧

# 四.打开抖音首页界面，python douyin.py运行代码就开始工作了。

![](http://chuantu.biz/t6/327/1528539426x-1404775485.jpg)
