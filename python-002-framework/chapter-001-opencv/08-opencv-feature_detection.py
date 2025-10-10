import cv2
import matplotlib.pyplot as plt

"""
    特征检测
        特征检测的基本概念
            在图像处理和计算机视觉领域，特征检测是一个关键步骤，它帮助我们识别图像中的显著点或区域，对于图像匹配、图像拼接、目标跟踪、三维重建等任
            务至关重要。
        特征检测的定义
            特征检测旨在从图像中提取有用的、可区分的信息。这些信息通常是图像中的特定点或区域，它们可以是角点、边缘、纹理或其他视觉显著性较高的元素。
        特征检测的目的
            通过特征检测，计算机可以识别和匹配图像中的相似对象，即使这些对象的外观因光照、遮挡或视角变化而有所不同。
        常见的特征检测算法
            SIFT（尺度不变特征变换）
                SIFT算法通过在不同尺度空间进行关键点检测，并为每个关键点赋予方向和尺度信息，使其对图像的尺度和旋转变化具有不变性。SIFT描述子对光
                照变化和视角变化也具有良好的稳定性。
            SURF（加速鲁棒特征）
                SURF是SIFT的改进版本，它使用了盒子滤波和积分图来加快计算速度，同时保持了SIFT的尺度和旋转不变性。SURF通常在检测速度和性能之间取
                得了较好的平衡。
            ORB（面向旋转不变特征的ORB）
                ORB结合了FAST关键点检测和BRIEF描述子，并对其进行了旋转调整，使其具有旋转不变性。ORB的关键点检测速度快，且描述子具有良好的区分度。
"""


def feature_detection_sift():
    """
        特征检测算法-sift
    """
    input_path = 'd://opencv//character_wheel.bmp'
    # 加载图像
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    # 初始化SIFT检测器
    sift = cv2.SIFT_create()
    # 检测关键点和描述符
    key_points, descriptors = sift.detectAndCompute(image, None)

    # 绘制关键点
    img_key_points = cv2.drawKeypoints(image, key_points, None)
    # 显示图像
    plt.imshow(img_key_points)
    plt.show()


def feature_detection_orb():
    """
        特征检测算法-orb
    """
    input_path = 'd://opencv//character_wheel.bmp'

    # 加载图像
    image = cv2.imread(input_path, 0)
    if image is None:
        print('图像加载失败')
        return

    # 初始化ORB检测器
    orb = cv2.ORB_create()
    # 检测关键点和描述符
    key_points, descriptors = orb.detectAndCompute(image, None)

    # 绘制关键点
    img_key_points = cv2.drawKeypoints(image, key_points, None)
    # 显示图像
    plt.imshow(img_key_points)
    plt.show()


if __name__ == '__main__':
    # feature_detection_sift()
    feature_detection_orb()



