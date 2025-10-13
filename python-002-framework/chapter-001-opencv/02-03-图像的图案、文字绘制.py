import cv2

import image_util as image_util


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
