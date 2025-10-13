import cv2
import numpy as np

import image_util as image_util


def opencv_image_operation():
    """
        形态学操作（腐蚀、膨胀、开运算、闭运算）
            形态学操作的基本概念
                形态学操作是一种基于图像结构的处理方法，用于改变图像的形状、大小或结构。它通常用于图像预处理、特征提取和图像分割等任务。
            形态学操作函数
                函数声明
                    cv2.morphologyEx(src, op, kernel, iterations) -> dst
                参数说明
                    src: 输入的二值图像，这是要进行形态学处理的源图像
                    op: 形态学操作类型
                        cv2.MORPH_OPEN: 开运算（先腐蚀后膨胀）- 去除小噪声，保持主要目标物体的形状和大小基本不变，分离粘连的物体边缘
                        cv2.MORPH_CLOSE: 闭运算（先膨胀后腐蚀）- 填充小孔洞
                        cv2.MORPH_ERODE: 腐蚀
                        cv2.MORPH_DILATE: 膨胀
                    kernel: 结构元素，用于定义操作的形状和大小，在代码中通过 cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) 创建了一个3×3的矩形结构元素
                    iterations: 迭代次数为1，iterations=1，即只执行一次开运算
                返回值说明
                    dst: 形态学处理后的图像

    """
    input_path = 'd://opencv//character_wheel.bmp'
    output_path = 'd://opencv//character_wheel_new.bmp'

    # 加载图像
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    '''
        通常先对图片进行降噪处理（均值滤波、中值滤波、高斯滤波等），再将降噪后的图片进行灰度处理，最后进行二值化处理
    '''
    # 1.中值滤波降噪
    kernel_size = 3
    image_median_blur = cv2.medianBlur(image, kernel_size)
    image_util.show_image_in_window('中值滤波处理后的图像', image_median_blur)  # 显示图像
    # 2.灰度处理
    image_gray = cv2.cvtColor(image_median_blur, cv2.COLOR_BGR2GRAY)
    # image_util.show_image_in_window('灰度处理后的图像', image_median_blur)    # 显示图像
    # 3.二值化处理，此处图片不用进行二值化处理，因为原始图像就是二值图像了
    # retval, image_binary = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # image_util.show_image_in_window('二值化处理后的图像', image_median_blur)   # 显示图像

    # 定义结构元素（内核）
    kernel = np.ones((2, 2), np.uint8)
    # 腐蚀（消除细小边界）
    image_erosion = cv2.erode(image_gray, kernel, iterations=1)
    # image_util.show_image_in_window('形态学操作-腐蚀后的图像', image_erosion)  # 显示图像

    # 膨胀（扩大边界）
    image_dilation = cv2.dilate(image_gray, kernel, iterations=1)
    # image_util.show_image_in_window('形态学操作-膨胀后的图像', image_dilation)  # 显示图像

    # 开运算（先腐蚀后膨胀，去除小物体）
    image_opening = cv2.morphologyEx(image_gray, cv2.MORPH_OPEN, kernel)
    # image_util.show_image_in_window('形态学操作-开运算后的图像', image_opening)  # 显示图像

    # 闭运算（先膨胀后腐蚀，填充小孔洞）
    image_closing = cv2.morphologyEx(image_gray, cv2.MORPH_CLOSE, kernel)
    # image_util.show_image_in_window('形态学操作-闭运算后的图像', image_closing)  # 显示图像

    # 保存图像
    # cv2.imwrite(output_path, image)


if __name__ == "__main__":
    opencv_image_operation()