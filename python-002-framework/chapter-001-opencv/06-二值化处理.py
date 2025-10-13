import cv2

import image_util as image_util

"""
    图像二值化处理
        图像二值化处理的基本概念
            图像二值化处理是将灰度图像转换为只有两个值（通常是0和255）的图像，用于突出图像中的物体或区域。二值化处理之前，通常需要进行灰度化处理。
        图像二值化处理函数
            函数声明    
                cv2.threshold(src, thresh, maxval, type[, dst]) -> retval, dst
            参数说明
                src: 输入图像，通常为单通道灰度图像
                thresh: 阈值
                maxval: 最大值，当像素值超过阈值时设置的值
                type: 阈值类型，常见选项包括：
                    cv2.THRESH_BINARY: 普通二值化
                    cv2.THRESH_BINARY_INV: 反向二值化
                    cv2.THRESH_TRUNC: 截断阈值化
                    cv2.THRESH_TOZERO: 阈值化为0
                    cv2.THRESH_TOZERO_INV: 反向阈值化为0
                    cv2.THRESH_OTSU: OTSU算法自动计算阈值
            返回值说明
                retval: 计算得到的阈值（当使用OTSU等自动阈值方法时）
                dst: 二值化后的图像
"""


def opencv_binary_detection():
    """
        二值化处理
        1.将图像转换为灰度图
        2.二值化处理
    """
    input_path = 'd://opencv//national_day.jpg'

    # 加载图像并检查是否成功
    image = cv2.imread(input_path)
    if image is None:
        print(f"错误：无法加载图像 '{input_path}'")
        return

    # 1.将图像转换为灰度图
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image_util.show_image_in_window("灰度处理后的图片", image)

    # 2.二值化处理，用于将灰度图像转换为二值图像
    retval, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    image_util.show_image_in_window("二值化处理后的图片", image)


if __name__ == '__main__':
    opencv_binary_detection()
