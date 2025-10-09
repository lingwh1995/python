import cv2
import image_util as image_util

"""
    图像二值化处理
        图像二值化处理的基本概念
            图像二值化处理是将灰度图像转换为只有两个值（通常是0和255）的图像，用于突出图像中的物体或区域。
        图像二值化处理函数：cv2.threshold()
            参数说明：
                src: 输入图像，通常为单通道灰度图像
                thresh: 阈值
                maxval: 最大值，当像素值超过阈值时设置的值
                type: 阈值类型，常见选项包括：
                    cv2.THRESH_BINARY: 普通二值化
                    cv2.THRESH_BINARY_INV: 反向二值化
                    cv2.THRESH_TRUNC: 截断阈值化
                    cv2.THRESH_TOZERO: 阈值化为0
                    cv2.THRESH_TOZERO_INV: 反向阈值化为0
                    cv2.THRESH_OTSU: OTSU算法自动计算阈值
            返回值说明：
                retval: 计算得到的阈值（当使用OTSU等自动阈值方法时）
                dst: 二值化后的图像
            函数声明：        
                cv2.threshold(src, thresh, maxval, type[, dst]) -> retval, dst

    
    轮廓的检测
        轮廓检测的基本概念
            轮廓检测（Contour Detection）用于检测图像中的边缘或物体的轮廓。轮廓是图像中连续的、具有相同颜色或灰度值的像素点所组成的曲线。通过
            轮廓检测，可以提取出图像中的对象的形状和结构信息。
        轮廓检测函数：cv2.findContours()
            函数声明    
                contours, hierarchy = cv2.findContours(image, mode, method, offset)
            函数说明
                cv2.findContours() 函数是用于查找图像中的轮廓的。它的输入参数是一个二值化图像，其中白色像素表示前景，黑色像素表示背景。
                函数返回的是一个包含轮廓的列表，每个轮廓都是一个由点组成的边界。
            参数说明：
                image：输入的二值图像，通常为灰度图像或二值化图像。图像需要为8位无符号整型。
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
                contours：返回的轮廓信息，是一个由多个轮廓组成的列表。
                hierarchy：返回的轮廓层级信息，与轮廓列表对应。每个轮廓对应一个四元组(hierarchy[0], hierarchy[1], hierarchy[2], hierarchy[3])，分
                别为后一个轮廓、前一个轮廓、父轮廓、子轮廓的索引。如果没有则为-1。
                
        轮廓的绘制函数：cv2.drawContours()
            函数声明
                image = cv2.drawContours(image, contours, contourIdx, color, thickness)  
            函数说明
                cv2.drawContours()函数是OpenCV中用于绘制轮廓的函数。
            参数说明：
                image：输入的图像，可以是灰度图像或彩色图像。
                contours：轮廓信息，可以是通过cv2.findContours()函数得到的轮廓列表。
                contourIdx：轮廓的索引，指定要绘制的轮廓。如果为负数（例如-1），则绘制所有的轮廓。
                color：绘制轮廓的颜色，可以是指定的颜色（例如(0,255,0)表示绿色）或者是使用-1用于绘制填充轮廓。
                thickness：轮廓线的宽度。如果为负数（例如-1），则绘制填充轮廓。默认值为1。
            返回值说明：
                image：返回的绘制轮廓后的图像。
"""


def filter_number_contours(contours, conditions):
    """
        过滤出可能是数字的轮廓
        :param contours: 轮廓列表
        :return: 过滤后的数字轮廓列表
    """
    min_area = conditions['min_area']
    max_area = conditions['max_area']
    min_width = conditions['min_width']
    max_width = conditions['max_width']
    min_height = conditions['min_height']
    max_height = conditions['max_height']

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
    input_path = 'd://opencv//character_wheel-2.bmp'

    # 加载图像
    image = cv2.imread(input_path)
    # 创建原始图像的彩色副本用于显示
    original_image = image.copy()

    # 1.中值滤波去噪
    image = cv2.medianBlur(image, 3)
    # image_util.show_image_in_window("中值滤波后的图片", image)

    # 2.将图像转换为灰度图
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image_util.show_image_in_window("灰度处理后的图片", image)

    # 3.二值化处理，用于将灰度图像转换为二值图像
    retval, image = cv2.threshold(image, 0, 255,  cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # image_util.show_image_in_window("二值化处理后的图片", image)

    # 4. 边缘检测（轮廓查找）
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 5.过滤数字轮廓
    number_contours_with_rect = filter_number_contours(contours, conditions)

    # 6.绘制过滤后的数字轮廓
    number_contours_image = original_image.copy()
    for contour, rect in number_contours_with_rect:
        x, y, w, h = rect
        # 绘制轮廓
        # cv2.drawContours(number_contours_image, [contour], -1, (0, 0, 255), 1)
        # 绘制边界矩形
        cv2.rectangle(number_contours_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 7.绘制所有轮廓
    all_contours_image = original_image.copy()
    cv2.drawContours(all_contours_image, contours, -1, (0, 255, 0), 2)

    # 8.显示结果
    # image_util.show_image_in_window("所有轮廓", all_contours_image)
    image_util.show_image_in_window("数字轮廓", number_contours_image)

    # 显示检测到的数字数量
    print(f"检测到 {len(number_contours_with_rect)} 个可能的数字轮廓")

    # 等待用户按键
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    conditions = {'min_area': 50, 'max_area': 800, 'min_width': 5, 'max_width': 32, 'min_height': 18.0,
                  'max_height': 40}
    contour_detection(conditions)
