import cv2

import image_util as image_util

"""
    轮廓的绘制函数
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
"""

# 缩放比例
scale = 1


def filter_number_contours(contours, conditions):
    """
        过滤出可能是数字的轮廓
        :param contours: 轮廓列表
        :return: 过滤后的数字轮廓列表
    """
    min_area = conditions['min_area'] * scale
    max_area = conditions['max_area'] * scale
    min_width = conditions['min_width'] * scale
    max_width = conditions['max_width'] * scale
    min_height = conditions['min_height'] * scale
    max_height = conditions['max_height'] * scale

    number_contours = []
    for contour in contours:
        # 计算轮廓的边界矩形
        x, y, w, h = cv2.boundingRect(contour)
        # 计算轮廓面积
        area = cv2.contourArea(contour)

        # 应用过滤条件
        if (min_area <= area <= max_area and
                min_width <= w <= max_width and
                min_height <= h <= max_height):
            number_contours.append((contour, (x, y, w, h)))
    # 按x坐标排序，使数字按从左到右顺序排列
    number_contours.sort(key=lambda c: c[1][0])
    return number_contours


def contour_detection(conditions):
    """
        轮廓检测
    """
    input_path = 'd://opencv//character_wheel.bmp'

    # 加载图像并检查是否成功
    image = cv2.imread(input_path)
    if image is None:
        print(f"错误：无法加载图像 '{input_path}'")
        return

    # 放大图片1倍
    image = cv2.resize(image, (image.shape[1] * scale, image.shape[0] * scale))
    # image_util.show_image_in_window('放大一倍后的图片', image)

    # 创建原始图像的彩色副本用于显示
    original_image = image.copy()

    # 1.中值滤波去噪
    image = cv2.medianBlur(image, 3)
    # image_util.show_image_in_window("中值滤波后的图片", image)

    # 2.将图像转换为灰度图
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image_util.show_image_in_window("灰度处理后的图片", image)

    # 3.二值化处理，用于将灰度图像转换为二值图像
    retval, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # image_util.show_image_in_window("二值化处理后的图片", image)

    # 4.进行形态学操作，改善图像质量
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 先进行闭运算连接断裂的轮廓
    # image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=1)
    # 再进行开运算去除噪声点
    # image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)
    # image_util.show_image_in_window("形态学处理后的图片", image)

    # 5. 边缘检测（轮廓查找）
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 6.过滤数字轮廓
    number_contours_with_rect = filter_number_contours(contours, conditions)

    # 7.绘制过滤后的数字轮廓
    number_contours_image = original_image.copy()
    for contour, rect in number_contours_with_rect:
        x, y, w, h = rect
        # 绘制轮廓
        # cv2.drawContours(number_contours_image, [contour], -1, (0, 0, 255), 1)
        # 绘制边界矩形
        cv2.rectangle(number_contours_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 8.绘制所有轮廓
    all_contours_image = original_image.copy()
    cv2.drawContours(all_contours_image, contours, -1, (0, 255, 0), 2)

    # 8.显示结果
    # image_util.show_image_in_window("所有轮廓", all_contours_image)
    image_util.show_image_in_window("数字矩形轮廓", number_contours_image)

    # 显示检测到的数字数量
    print(f"检测到 {len(number_contours_with_rect)} 个可能的数字轮廓")


if __name__ == '__main__':
    conditions = {'min_area': 50, 'max_area': 800, 'min_width': 5, 'max_width': 32, 'min_height': 18.0,
                  'max_height': 40}
    contour_detection(conditions)
