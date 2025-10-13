import cv2

import image_util as image_util


def opencv_threshold_operation():
    """
        使用opencv对图像进行阈值分割
            阈值处理将图像转换为二值图像，用于分割。
    """
    input_path = 'd://opencv//character_wheel.bmp'
    output_path = 'd://opencv//character_wheel.bmp_new.jpg'

    # 加载图像
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    # 简单阈值
    ret, image_thresh_simple = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)

    # 显示图像
    image_util.show_image_in_window('阈值分割之简单阈值', image_thresh_simple)

    # 保存图像
    # cv2.imwrite(output_path, image_thresh_simple)


if __name__ == "__main__":
    opencv_threshold_operation()
