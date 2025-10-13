import cv2

import image_util as image_util


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
