import cv2

import image_util as image_util

"""
    滤波操作
        滤波操作的基本概念
            在数字图像处理中，滤波是一种常用的技术，用来消除图像中的噪声或者执行边缘保留等操作。
        滤波操作的定义
            滤波操作是一种在频域内对图像进行处理的方法，主要目的是减少图像中的噪声，或改变图像的特征以突出某些特定的信息。滤波可以分为线性滤波和非
            线性滤波两大类。线性滤波通过将图像与一个滤波器核（kernel）进行卷积实现，而非线性滤波可能依赖于图像中像素的排序或其他统计属性。
        常见的滤波操作和应用场景
            常见的线性滤波器包括均值滤波器（用于去除噪声）、高斯滤波器（用于模糊和去除高斯噪声）、中值滤波器（用于去除椒盐噪声）等。非线性滤波器包
            括双边滤波器（用于边缘保留的模糊）、形态滤波器（用于消除小对象或填充孔洞）、导向滤波器等。每种滤波器有其特定的应用场景。例如，在图像预
            处理阶段通常会用均值滤波或中值滤波去除噪声；在图像增强过程中，使用高斯模糊可以使图像的边缘模糊，产生一种平滑的视觉效果。
        滤波操作的实施步骤
            选择合适的滤波器核。对于高斯模糊，需要确定核的大小和高斯分布的标准差。
            创建滤波器核。根据核的大小和标准差，计算出二维高斯分布对应的值，形成一个矩阵。
            将滤波器核与图像卷积。遍历图像中的每一个像素点，将滤波器核应用于其邻域像素，进行加权求和操作。
            处理图像边缘。根据需要，可以扩展图像边缘或者忽略边缘像素。
"""


def opencv_blur_operation():
    """
        使用opencv进行中值模糊

        cv2.medianBlur() 函数用于对图像进行中值模糊。

        medianBlur(src, ksize[, dst]) -> dst
        - src ：输入的图像。
        - ksize ：中值滤波核的大小。必须是正的奇数。
        - dst ：输出图像，与输入图像具有相同的尺寸和类型。
    """
    # 读取RGB格式图像
    input_path = 'd://opencv//character_wheel.bmp'
    output_path = 'd://opencv//character_wheel_new.bmp'

    # 读取BGR格式图像
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    # 中值滤波 (对椒盐噪声效果好，内核大小为正奇数)
    kernel_size = 3
    image_median_blur = cv2.medianBlur(image, kernel_size)
    # 显示图像
    image_util.show_image_in_window('中值滤波后的图像', image_median_blur)

    # 保存图像
    # cv2.imwrite(output_path, image_median_blur)


if __name__ == "__main__":
    opencv_blur_operation()
