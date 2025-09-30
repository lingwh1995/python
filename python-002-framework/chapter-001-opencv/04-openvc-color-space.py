import cv2
import numpy as np

"""
    颜色空间
        颜色空间的基本概念
            颜色空间是用于以数值方式表示颜色的一种方法。它是图像处理、显示和打印的基础。不同的颜色空间有不同的定义和使用场景。理解它们对于进行有效的图像处理至关重要。  
        颜色空间的定义
            颜色空间的定义通常涉及色彩的感知、表示和物理设备的限制。例如，在RGB颜色空间中，色彩由红色、绿色、蓝色三种光的强度组合来表示，这直接对应于大多数显示器和
            相机如何捕捉和显示颜色。另一种常见的是HSV（色调、饱和度、亮度）颜色空间，它更符合人类对颜色的直观理解。
        颜色空间的类型    
            颜色空间的类型繁多，除了RGB和HSV之外，还包括YUV、CMYK、Lab等。每种颜色空间都具有特定的优势，适用于不同的图像处理任务。例如，YUV颜色空间常用于视频压
            缩和传输，因为它的亮度（Y）和色度（UV）分量是分离的，这使得对亮度信号的处理比彩色信号容易得多。
        颜色空间的转换方法
            颜色空间转换是将图像从一种颜色空间转换到另一种颜色空间的过程。常见的转换方法包括线性变换和非线性变换。线性变换通过矩阵乘法来实现颜色空间的转换，而非线性变
            换则可能涉及色彩校正、伽马校正等步骤。
        颜色空间的应用场景
            应用场景方面，图像处理中常见的如在色彩校正和颜色空间压缩时使用YUV空间；在进行颜色分析和识别时可能会转换到HSV空间；而Lab颜色空间则由于其与设备无关的特性，
            通常用于颜色的通用比较。 
"""


def show_image_in_window(title, image):
    """
        显示图像函数
        param：
            image：要显示的图像
        return：
            无
    """
    cv2.imshow(title, image)
    cv2.waitKey(0)  # 等待按键
    cv2.destroyAllWindows()  # 关闭所有窗口


def opencv_color_space_01():
    """
        使用opencv将RGB图像转换为灰度图像（颜色空间的转换之单通道和多通道图像的颜色空间的转换）

        cv2.imread() 用于读取图像
        cv2.cvtColor() 用于转换颜色空间
        cv2.imshow() 用于显示图像
    """
    input_path = 'd://opencv//national_day.jpg'
    output_path = 'd://opencv//national_day_gray.jpg'
    # 读取RGB格式图像
    image_rgb = cv2.imread(input_path)

    # 转换为灰度图像
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

    # 显示转换后的灰度图像
    cv2.imshow('Grayscale Image', image_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存图像
    cv2.imwrite(output_path, image_gray)


def opencv_color_space_02():
    # 读取RGB格式图像
    input_path = 'd://opencv//national_day.jpg'
    output_path = 'd://opencv//national_day_red.jpg'

    # 读取BGR格式图像
    image_bgr = cv2.imread(input_path)

    # 将图像从BGR转换到HSV空间
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

    # 定义红色在HSV空间中的范围
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # 创建一个掩码，以便只提取红色
    mask = cv2.inRange(image_hsv, lower_red, upper_red)

    # 将掩码和原图像进行位运算，提取红色区域
    red_objects = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)

    # 显示图像
    show_image_in_window('提取到的图像中的红色区域', red_objects)

    # 保存图像
    cv2.imwrite(output_path, red_objects)


def main():
    # opencv_color_space_01()
    opencv_color_space_02()


if __name__ == "__main__":
    main()
