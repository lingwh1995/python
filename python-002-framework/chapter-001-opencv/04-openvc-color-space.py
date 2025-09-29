import cv2
import numpy as np


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


def opencv_color_01():
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


def opencv_color_02():
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
    show_image_in_window('提取到的图像中的红色区域......', red_objects)

    # 保存图像
    cv2.imwrite(output_path, red_objects)


def main():
    # opencv_color_01()
    opencv_color_02()


if __name__ == "__main__":
    main()
