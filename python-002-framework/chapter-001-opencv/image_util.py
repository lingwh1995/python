import cv2


def show_image_in_window(title, image):
    """
        显示图像函数
        param：
            image：要显示的图像
        return：
            无
    """
    cv2.imshow(title, image)
    cv2.waitKey(0)  # 等待按键（0表示无限等待）
    cv2.destroyAllWindows()  # 关闭所有窗口
