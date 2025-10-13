import cv2

import image_util as image_util


def opencv_image_operation():
    """
        图像的像素操作与 ROI (Region of Interest)
            像素操作：
                访问像素值：可以通过索引直接访问图像数组中的像素值。
                修改像素值：可以直接赋值来修改图像数组中的像素值。
            ROI 操作：
                提取 ROI：可以使用数组切片来提取图像中的感兴趣区域（ROI）。
                对 ROI 进行操作：可以对提取的 ROI 进行任意的像素操作，如修改颜色、应用滤镜等。
    """
    input_path = 'd://opencv//national_day.jpg'
    output_path = 'd://opencv//national_day_new.jpg'

    # 加载图像
    image = cv2.imread(input_path)
    if image is None:
        print('图像加载失败')
        return

    # 访问 (100, 200) 处的像素值 (B, G, R)
    px_value = image[100, 200]
    print("像素值(B, G, R)：", px_value)

    # 修改该像素点为绿色 (B=0, G=255, R=0)
    image[100, 200] = [0, 255, 0]

    # 获取 ROI (例如从 (50,100) 开始，高100像素，宽200像素的区域)
    roi = image[100:200, 50:250]  # 高度范围在前，宽度范围在后
    # 可以对 ROI 进行操作，例如将其变为红色
    roi[:, :] = [0, 0, 255]  # 注意是 BGR

    # 显示图像
    image_util.show_image_in_window('图像的像素操作与ROI操作', image)

    # 保存图像
    # cv2.imwrite(output_path, image)


if __name__ == "__main__":
    opencv_image_operation()
