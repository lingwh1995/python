# image_clip_util.py
import os
import cv2
from ultralytics import YOLO


class ImageClipUtil:
    """图像裁剪工具类，用于裁剪YOLO模型识别到的区域"""

    def __init__(self, model_path):
        """
        初始化工具类

        Args:
            model_path (str): YOLO模型路径
        """
        self.model = YOLO(model_path)

    def clip_single_image(self, image_path, output_dir,
                         conf_threshold=0.2, max_detections=5):
        """
        裁剪单张图像识别到的区域并保存

        Args:
            image_path (str): 输入图像路径
            output_dir (str): 输出目录路径
            conf_threshold (float): 置信度阈值
            max_detections (int): 最大检测数量
        """
        # 检查输入文件是否存在
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图像文件不存在: {image_path}")

        # 读取图像
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"无法读取图像: {image_path}")

        # 获取文件名信息
        filename = os.path.basename(image_path)
        filename_without_ext, ext = os.path.splitext(filename)

        # 使用模型检测
        results = self.model(
            image_path,
            conf=conf_threshold,
            max_det=max_detections
        )

        # 处理检测结果
        clip_count = 0
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                xyxy = boxes.xyxy.cpu().numpy()

                # 裁剪每个检测区域
                for i, (x1, y1, x2, y2) in enumerate(xyxy):
                    # 转换为整数坐标并确保在图像范围内
                    x1, y1 = max(0, int(x1)), max(0, int(y1))
                    x2, y2 = min(image.shape[1], int(x2)), min(image.shape[0], int(y2))

                    # 裁剪区域
                    clipped_region = image[y1:y2, x1:x2]

                    # 生成输出文件名: 原文件名 + _clip + 序号 + 扩展名
                    output_filename = f"{filename_without_ext}_clip{i}{ext}"
                    output_path = os.path.join(output_dir, output_filename)

                    # 保存裁剪图像
                    success = cv2.imwrite(output_path, clipped_region)
                    if success:
                        print(f"已保存裁剪图像: {output_path}")
                        clip_count += 1
                    else:
                        print(f"保存裁剪图像失败: {output_path}")

        return clip_count

    def clip_directory_images(self, input_dir, output_dir,
                             conf_threshold=0.2, max_detections=5):
        """
        批量裁剪目录下所有图像识别到的区域

        Args:
            input_dir (str): 输入图像目录路径
            output_dir (str): 输出目录路径
            conf_threshold (float): 置信度阈值
            max_detections (int): 最大检测数量
        """
        # 检查输入目录是否存在
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"输入目录不存在: {input_dir}")

        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)

        # 支持的图像格式
        supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

        # 获取目录下所有图像文件
        image_files = [f for f in os.listdir(input_dir)
                      if f.lower().endswith(supported_formats)]

        if not image_files:
            print(f"输入目录 {input_dir} 中没有找到图像文件")
            return 0

        total_clips = 0
        for image_file in image_files:
            image_path = os.path.join(input_dir, image_file)
            try:
                clip_count = self.clip_single_image(
                    image_path, output_dir, conf_threshold, max_detections)
                total_clips += clip_count
                print(f"处理完成: {image_file} (裁剪了 {clip_count} 个区域)")
            except Exception as e:
                print(f"处理图像 {image_file} 时出错: {e}")

        print(f"总共处理了 {len(image_files)} 张图像，裁剪了 {total_clips} 个区域")
        return total_clips


def main():
    """主函数示例"""
    # 使用示例
    try:
        # 初始化工具类
        clipper = ImageClipUtil("../../model/dial.pt")

        # 批量裁剪识别区域
        input_dir = "../11n/dataset/dial/images"
        output_dir = "../11n/dataset/dial/images_clip"
        clipper.clip_directory_images(input_dir, output_dir)

    except Exception as e:
        print(f"执行出错: {e}")


if __name__ == "__main__":
    main()