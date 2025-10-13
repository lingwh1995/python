import cv2

import image_util as image_util


def opencv_image_operation():
    """
        使用opencv加载、裁剪、缩放、旋转图像

        opencv 常用库函数第二部分

        image[y:y+h, x:x+w] 是使用NumPy的切片来裁剪图像。
        cv2.resize() 函数用于缩放图像。
        cv2.getRotationMatrix2D() 函数用于生成旋转矩阵。
        cv2.warpAffine() 函数应用仿射变换，用于旋转图像。
    """
    input_path = 'd://opencv//national_day.jpg'
    output_path = 'd://opencv//national_day_new.jpg'

    # 加载图像，返回一个 NumPy 数组
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    # 图像裁剪
    x, y, w, h = 0, 0, 600, 600  # 裁剪区域的坐标和尺寸
    cropped = image[y:y + h, x:x + w]
    # 显示图像
    image_util.show_image_in_window('裁剪后的图像', cropped)

    # 图像缩放
    scale_percent = 50  # 缩放百分比
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    # 缩放至指定尺寸
    resized = cv2.resize(image, (width, height))
    # 按比例缩放 (例如缩小一半)
    # resized = cv2.resize(img, None, fx=0.5, fy=0.5)
    # 显示图像
    image_util.show_image_in_window('缩放后的图像', resized)

    # 图像旋转
    (h, w) = image.shape[:2]
    # // 取整除法(地板除)
    center = (w // 2, h // 2)
    # 顺时针旋转45度，第二个参数-45，逆时针旋转45度，第二个参数45
    M = cv2.getRotationMatrix2D(center, -45, 1.0)   # 获取旋转矩阵
    rotated = cv2.warpAffine(image, M, (w, h))  # 执行仿射变换
    # 显示图像
    image_util.show_image_in_window('旋转后的图像', rotated)

    # 保存图像
    # cv2.imwrite(output_path, image)


if __name__ == "__main__":
    opencv_image_operation()
