import cv2

import image_util as image_util

"""
    图像处理
        图像处理的基本概念
            图像处理是计算机科学的一个分支，它使用算法来实现图像的获取、存储、传输、显示、分析和理解。图像处理的目标是将图像转换为一种更适合于分析
            的形式。这可能涉及到改善视觉效果以供人类观看，或者为自动图像分析准备图像数据。图像处理技术广泛应用于医疗成像、卫星图像分析、视频监控、
            数字摄影以及许多其他领域。
        图像处理的应用包括但不限于
            增强 ：提高图像的可视效果，例如增加对比度或亮度。
            恢复 ：减少图像中的噪声，修复有损的图像。
            分割 ：将图像分割为多个部分或对象。
            特征提取 ：识别图像中的关键点，如角点、边缘等。
        图像处理的常见任务
            图像的几何变换
            图像压缩
            图像分类
            目标检测
        图像处理的常见应用场景
            医疗成像 ：在X射线、CT、MRI等医疗图像中进行病变检测。
            自动驾驶 ：使用图像处理技术检测行人、车辆以及其他障碍物。
            面部识别 ：在安全和监控领域用于身份验证。
            工业检测 ：在制造业中检测产品缺陷，确保质量控制。
"""


def opencv_image_operation():
    """
        绘图功能
            OpenCV 提供了在图像上绘制几何图形和文字的函数，常用于标记检测结果。
            cv2.rectangle() 函数用于绘制矩形框
            cv2.circle() 函数用于绘制圆形
            cv2.putText() 函数用于添加文字
    """
    input_path = 'd://opencv//national_day.jpg'
    output_path = 'd://opencv//national_day_new.jpg'

    # 加载图像
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    # 绘制一个蓝色矩形框 (从点(50,50)到点(200,200))，线宽为2
    cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 10)
    # 绘制一个实心红色圆形 (圆心(300,300)，半径200)
    cv2.circle(image, (400, 300), 200, (0, 255, 0), -1)  # 线宽-1表示填充
    # 添加文字 "Hello OpenCV"
    cv2.putText(image, 'Hello OpenCV', (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 10)

    # 显示图像
    image_util.show_image_in_window('绘图功能', image)

    # 保存图像
    # cv2.imwrite(output_path, image)


if __name__ == "__main__":
    opencv_image_operation()
