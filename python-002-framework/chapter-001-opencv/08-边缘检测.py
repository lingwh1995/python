import cv2

import image_util as image_util


def opencv_canny_operation():
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

    # 通常先模糊降噪
    image_gaussian_blurred = cv2.GaussianBlur(image, (5, 5), 0)
    # Canny 边缘检测 (阈值1, 阈值2)
    image_canny = cv2.Canny(image_gaussian_blurred, 50, 150)  # 低于阈值1为非边缘，高于阈值2为强边缘，中间为待定

    # 显示图像
    image_util.show_image_in_window('边缘检测', image_canny)

    # 保存图像
    # cv2.imwrite(output_path, image_canny)


if __name__ == "__main__":
    opencv_canny_operation()
