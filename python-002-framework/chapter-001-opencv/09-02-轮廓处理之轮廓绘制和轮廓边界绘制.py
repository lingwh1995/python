import cv2

import image_util as image_util

"""
    轮廓绘制函数
        函数声明
            cv2.drawContours(image, contours, contourIdx, color, thickness) -> dst
        参数说明：
            image：输入的图像，可以是灰度图像或彩色图像。
            contours：轮廓信息，可以是通过cv2.findContours()函数得到的轮廓列表。
            contourIdx：轮廓的索引，指定要绘制的轮廓。如果为负数（例如-1），则绘制所有的轮廓。
            color：绘制轮廓的颜色，可以是指定的颜色（例如(0,255,0)表示绿色）或者是使用-1用于绘制填充轮廓。
            thickness：轮廓线的宽度。如果为负数（例如-1），则绘制填充轮廓。默认值为1。
        返回值说明：
            dst：返回的绘制轮廓后的图像。
    
    轮廓矩形边界绘制函数
        函数声明
            cv2.rectangle(image, pt1, pt2, color, thickness) -> dst
        参数说明：
            image：输入的图像，可以是灰度图像或彩色图像。
            pt1：矩形的左上角顶点坐标。
            pt2：矩形的右下角顶点坐标。
            color：矩形的颜色，可以是指定的颜色（例如(0,255,0)表示绿色）。
            thickness：矩形边框的宽度。如果为负数（例如-1），则绘制填充矩形。默认值为1。
        返回值说明：
            dst：返回的绘制矩形边界后的图像。
"""


def filter_number_contours(contours):
    number_contours = []

    for contour in contours:
        # 计算轮廓的边界矩形
        x, y, w, h = cv2.boundingRect(contour)
        # 计算轮廓面积
        area = cv2.contourArea(contour)

        # 应用过滤条件
        if 50 <= area <= 800 and 5 <= w <= 32 and 18 <= h <= 40:
            number_contours.append((contour, (x, y, w, h)))
    # 按x坐标排序，使数字按从左到右顺序排列
    number_contours.sort(key=lambda c: c[1][0])
    return number_contours


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

    image_number_contours = image.copy()

    # 1.将图像转换为灰度图
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image_util.show_image_in_window("灰度处理后的图片", image)

    # 2.二值化处理，用于将灰度图像转换为二值图像
    retval, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # image_util.show_image_in_window("二值化处理后的图片", image)

    # 3.获取所有检测到的轮廓
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 4.过滤出可能是数字的轮廓
    number_contours = filter_number_contours(contours)

    for contour, rect in number_contours:
        # 计算轮廓的边界矩形
        x, y, w, h = rect
        # 绘制轮廓
        cv2.drawContours(image_number_contours, [contour], -1, (0, 0, 255), 1)
        # 绘制边界矩形
        cv2.rectangle(image_number_contours, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示图像
    image_util.show_image_in_window('轮廓绘制后的图片', image_number_contours)

    # 保存图像
    # cv2.imwrite(output_path, image_number_contours)


if __name__ == "__main__":
    opencv_canny_operation()
