import cv2

import image_util as image_util


def opencv_threshold_operation():
    """
        使用opencv对图像进行阈值分割
            阈值处理将图像转换为二值图像，用于分割。
    """
    input_path = 'd://opencv//character_wheel.bmp'
    output_path = 'd://opencv//dial.bmp_new.jpg'

    # 加载图像
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    # 自适应阈值 (适用于光照不均的图像)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_thresh_adaptive = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # 显示图像
    image_util.show_image_in_window('阈值分割之自适应阈值', image_thresh_adaptive)

    # 保存图像
    # cv2.imwrite(output_path, image)


if __name__ == "__main__":
    opencv_threshold_operation()
