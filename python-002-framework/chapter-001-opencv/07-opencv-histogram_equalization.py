import cv2
import matplotlib.pyplot as plt

"""
    直方图均衡化
        直方图均衡化的基本概念
            直方图均衡化是图像处理中的一种常用技术，用于改善图像的全局对比度，尤其是当图像的有用数据的对比度相当低时。通过直方图均衡化，可以增强图
            像的细节，尤其是当原始图像光照不均匀时。
        直方图均衡化的原理
            直方图均衡化操作基于累积分布函数（CDF），它统计每个强度值之前所有强度值出现的次数。通过将累积分布函数映射回原始直方图，每个强度值被重
            新分配到新的值，从而拉伸直方图。均衡化后的图像具有更均匀的亮度分布，使图像细节更加清晰。
        直方图均衡化的特点
            增强图像对比度：使得图像中暗的区域变得更暗，亮的区域变得更亮。
            适用于低对比度图像：对于因为光照问题导致对比度低的图像特别有效。
            全局处理：对整个图像应用，而不仅仅是局部区域。
        直方图均衡化优点
            全局对比度增强 ：直方图均衡化可以改善整个图像的对比度，特别适用于整体亮度不足的图像。
            适用范围广 ：适用于各种场景的图像，尤其是在光照不均匀的情况下。 
        直方图均衡化缺点
            局部对比度丢失 ：虽然增强了全局对比度，但可能会导致图像的局部细节丢失。
            对噪声敏感 ：对于含有噪声的图像，均衡化可能会增强噪声，影响图像质量。 
        适用场景
            低对比度图像增强 ：在需要提高图像整体亮度和对比度时使用。
            医学图像分析 ：在医学成像中，直方图均衡化可以提高图像的可视性和细节。 
"""


def histogram_equalization():
    input_path = 'd://opencv//character_wheel.bmp'
    # 加载图像
    image = cv2.imread(input_path)

    # 将图像从BGR转换到灰度
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 计算原始图像的直方图
    hist_original = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # 应用直方图均衡化
    equalized_image = cv2.equalizeHist(gray_image)

    # 计算均衡化后图像的直方图
    hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

    # 显示原始图像和均衡化后的图像
    cv2.imshow('原始图像', gray_image)
    cv2.imshow('直方图均衡化后的图像', equalized_image)

    # 显示直方图
    plt.figure()
    plt.subplot(221), plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB), cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.plot(hist_original)
    plt.title('Histogram for Original Image')

    plt.subplot(223), plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2RGB), cmap='gray')
    plt.title('Equalized Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.plot(hist_equalized)
    plt.title('Histogram for Equalized Image')

    # 自动调整子图间距
    plt.tight_layout()
    # 显示最终的图表窗口
    plt.show()

    # 等待按键后关闭所有窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    histogram_equalization()
