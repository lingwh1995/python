import cv2

import image_util as image_util


def opencv_blur_operation():
    """
        使用opencv进行高斯模糊

        cv2.GaussianBlur() 函数用于对图像进行高斯模糊。

        GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
        - src ：输入的图像。
        - ksize ：高斯核的大小。必须是正的奇数。
        - sigmaX ：高斯核在X方向上的标准差。
        - dst ：输出图像，与输入图像具有相同的尺寸和类型。
        - sigmaY ：高斯核在Y方向上的标准差。如果 sigmaY 为零，则设为 sigmaX 的值；如果都为零，则根据 ksize 计算得到。
        - borderType ：边界模式，定义了图像边界外像素的处理方式。
    """
    # 读取RGB格式图像
    input_path = 'd://opencv//character_wheel.bmp'
    output_path = 'd://opencv//character_wheel_new.bmp'

    # 读取BGR格式图像
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    # 设置高斯核的大小，必须是正奇数
    kernel_size = 3
    # 高斯分布的标准差，决定了模糊的程度。较大的 sigma 会产生更强的模糊效果
    sigma = 1.0

    # 高斯滤波 (内核大小需为正奇数，sigmaX为X方向高斯核标准差)
    image_gaussian_blur = cv2.GaussianBlur(image, (kernel_size,kernel_size), sigma)
    # 显示图像
    image_util.show_image_in_window('高斯滤波后的图像', image_gaussian_blur)

    # 保存图像
    # cv2.imwrite(output_path, image_gaussian_blur)


if __name__ == "__main__":
    opencv_blur_operation()
