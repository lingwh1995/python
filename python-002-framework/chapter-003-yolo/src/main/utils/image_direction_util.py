import cv2
import os


def rotate_images_by_angle(input_path, output_path, angle):
    """
    从input_path文件夹中读取所有图片，旋转指定角度后保存到output_path文件夹

    Args:
        input_path (str): 输入图片文件夹路径
        output_path (str): 输出图片文件夹路径
        angle (float): 旋转角度，单位为度（顺时针为正）
    """
    # 检查输入路径是否存在
    if not os.path.exists(input_path):
        print(f"输入路径 {input_path} 不存在")
        return

    # 创建输出路径（如果不存在）
    os.makedirs(output_path, exist_ok=True)

    # 支持的图片格式
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif')

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_path):
        if filename.lower().endswith(supported_formats):
            # 构建完整的输入文件路径
            input_file = os.path.join(input_path, filename)

            # 读取图像
            image = cv2.imread(input_file)
            if image is None:
                print(f"无法读取图像: {input_file}")
                continue

            # 获取图像尺寸
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)

            # 计算旋转矩阵（旋转指定角度）
            M = cv2.getRotationMatrix2D(center, angle, 1.0)

            # 执行旋转
            rotated_image = cv2.warpAffine(image, M, (w, h))

            # 构建输出文件路径
            output_file = os.path.join(output_path, filename)

            # 保存旋转后的图像
            success = cv2.imwrite(output_file, rotated_image)
            if success:
                print(f"成功处理并保存: {output_file}")
            else:
                print(f"保存失败: {output_file}")


# 使用示例
if __name__ == "__main__":
    # 设置输入和输出路径
    input_path = 'e://images//water_meter'
    output_path = 'e://images//water_meter_new'

    # 调用函数处理图片
    rotate_images_by_angle(input_path, output_path, 90)
