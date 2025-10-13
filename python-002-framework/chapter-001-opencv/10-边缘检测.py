import cv2

import image_util as image_util

"""
    轮廓的检测
        轮廓检测的基本概念
            轮廓检测（Contour Detection）用于检测图像中的边缘或物体的轮廓。轮廓是图像中连续的、具有相同颜色或灰度值的像素点所组成的曲线。通过
            轮廓检测，可以提取出图像中的对象的形状和结构信息。
        轮廓检测函数
            函数声明    
                cv2.findContours(image, mode, method, offset) -> contours, hierarchy
            参数说明：
                image：输入的二值图像，通常为灰度图像或二值化图像（其中白色像素表示前景，黑色像素表示背景）。图像需要为8位无符号整型。
                mode：轮廓检索模式。有四种模式可选：
                    cv2.RETR_EXTERNAL：只检测外部的轮廓。
                    cv2.RETR_LIST：检测所有的轮廓，不建立轮廓间的层级关系。
                    cv2.RETR_CCOMP：检测所有的轮廓，并将其组织为两层的层级关系。
                    cv2.RETR_TREE：检测所有的轮廓，并将其组织为树状的层级关系。
                method：轮廓近似方法。有三种方法可选：
                    cv2.CHAIN_APPROX_NONE：保存所有的轮廓点。
                    cv2.CHAIN_APPROX_SIMPLE：只保存轮廓的端点。
                    cv2.CHAIN_APPROX_TC89_L1和cv2.CHAIN_APPROX_TC89_KCOS：通过Teh-Chin链码逼近算法进行轮廓近似。
            返回值说明：
                contours：返回的轮廓信息，每个轮廓都是一个由点组成的边界，是一个由多个轮廓组成的列表。
                hierarchy：返回的轮廓层级信息，与轮廓列表对应。每个轮廓对应一个四元组(hierarchy[0], hierarchy[1], hierarchy[2], hierarchy[3])，分
                别为后一个轮廓、前一个轮廓、父轮廓、子轮廓的索引。如果没有则为-1。
"""


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
