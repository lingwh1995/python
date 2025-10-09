import cv2

"""
    1.opencv架构与功能模块
        opencv被组织成多个模块，每个模块都关注计算机视觉的特定方面。核心模块包括：

        core ：包含了数据结构和基本功能，如数组操作、绘图函数、矩阵操作等
        imgproc ：提供了图像处理相关的函数，包括图像滤波、几何变换、颜色空间转换等
        highgui ：是一个高级GUI组件，支持视频、图像和键盘鼠标事件的交互
        video ：提供了视频处理相关功能，如背景减除、对象追踪等
        objdetect ：包含了对象检测相关算法，如Haar特征分类器、级联分类器等
        calib3d ：用于解决3D计算机视觉问题，如单目、双目和多目摄像机的标定

    2.搭建opencv环境
        pip install opencv-python
        # 如果需要进行图像和视频界面交互，可以安装额外的库
        # pip install opencv-python-headless
        编写测试代码
           import cv2
           print(cv2.__version__)
"""


print(cv2.__version__)
