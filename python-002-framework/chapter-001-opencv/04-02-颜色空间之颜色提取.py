import cv2
import numpy as np

import image_util as image_util


def opencv_color_space_operation():
    # 读取RGB格式图像
    input_path = 'd://opencv//national_day.jpg'
    output_path = 'd://opencv//national_day_red.jpg'

    # 读取BGR格式图像
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    # 将图像从BGR转换到HSV空间
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义红色在HSV空间中的范围
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # 创建一个掩码，以便只提取红色
    mask = cv2.inRange(image_hsv, lower_red, upper_red)

    # 将掩码和原图像进行位运算，提取红色区域
    image_red_area = cv2.bitwise_and(image, image, mask=mask)

    # 显示图像
    image_util.show_image_in_window('提取到的图像中的红色区域', image_red_area)

    # 保存图像
    # cv2.imwrite(output_path, image_red_area)


if __name__ == "__main__":
    opencv_color_space_operation()
