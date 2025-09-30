import cv2

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


def show_image_in_window(title, image):
    """
        显示图像函数
        param：
            image：要显示的图像
        return：
            无
    """
    cv2.imshow(title, image)
    cv2.waitKey(0)  # 等待按键
    cv2.destroyAllWindows()  # 关闭所有窗口


def opencv_image_01():
    """
        使用opencv加载、显示、保存图像

        opencv 常用库函数第一部分

        cv2.imread() 用于加载图像
        cv2.imshow() 用于在窗口中显示图像
        cv2.waitKey() 用于等待用户输入，参数是毫秒，0表示无限等待
        cv2.destroyAllWindows() 用于关闭所有OpenCV创建的窗口
    """
    input_path = 'd://opencv//national_day.jpg'
    output_path = 'd://opencv//national_day_new.jpg'
    # 加载图像
    image = cv2.imread(input_path)

    height = image.shape[0]  # 图像原始高度
    width = image.shape[1]  # 图像原始宽度
    channel = image.shape[2]  # 图像原始通道数（BGR）
    print(f'图像高度：{height}')
    print(f'图像宽度：{width}')
    print(f'图像通道数：{channel}')

    # 显示图像
    show_image_in_window('这是我加载的图像', image)

    # 保存图像
    cv2.imwrite(output_path, image)


def opencv_image_02():
    """
        使用opencv加载、裁剪、缩放、旋转图像

        opencv 常用库函数第二部分

        image[y:y+h, x:x+w] 是使用NumPy的切片来裁剪图像。
        cv2.resize() 函数用于缩放图像。
        cv2.getRotationMatrix2D() 函数用于生成旋转矩阵。
        cv2.warpAffine() 函数应用仿射变换，用于旋转图像。
    """
    input_path = 'd://opencv//national_day.jpg'
    # 加载图像
    image = cv2.imread(input_path)

    # 图像裁剪
    x, y, w, h = 0, 0, 600, 600  # 裁剪区域的坐标和尺寸
    cropped = image[y:y + h, x:x + w]
    # 显示图像
    show_image_in_window('裁剪后的图像', cropped)

    # 图像缩放
    scale_percent = 50  # 缩放百分比
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    resized = cv2.resize(image, (width, height))
    # 显示图像
    show_image_in_window('缩放后的图像', resized)

    # 图像旋转
    (h, w) = image.shape[:2]
    # // 取整除法(地板除)
    center = (w // 2, h // 2)
    # 顺时针旋转45度，第二个参数-45，逆时针旋转45度，第二个参数45
    M = cv2.getRotationMatrix2D(center, -45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    # 显示图像
    show_image_in_window('旋转后的图像', rotated)


def main():
    # opencv_image_01()
    opencv_image_02()


if __name__ == "__main__":
    main()
