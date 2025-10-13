import cv2
import matplotlib.pyplot as plt

import image_util as image_util


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
    image_util.show_image_in_window('ORB特征检测', img_key_points)
    plt.show()

    # 保存图像
    # cv2.imwrite(output_path, img_key_points)


if __name__ == '__main__':
    feature_detection_orb()
