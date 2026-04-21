import os
import shutil

import cv2
from ultralytics import YOLO

def filter(source_dir, target_dir, conf_threshold=0.2, max_detections=5):
    try:
        # 1. 加载 YOLOv11 预训练模型
        # 请确保路径 model/dial.pt 正确
        model = YOLO("../model/dial.pt")

        # 2. 检测图片文件夹是否存在
        if not os.path.exists(source_dir):
            print(f"错误：图片文件夹 {source_dir} 不存在")
            return

        # 3. 创建或清空目标文件夹
        if os.path.exists(target_dir):
            print(f"检测到目标目录已存在，正在清空：{target_dir}")
            # 删除目标目录中的所有文件和子文件夹
            for filename in os.listdir(target_dir):
                file_path = os.path.join(target_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"删除文件 {file_path} 时出错：{e}")
            print("目标目录已清空")
        else:
            # 如果目录不存在，则创建
            os.makedirs(target_dir, exist_ok=True)
            print(f"已创建目标目录：{target_dir}")

        # 4. 读取 source_dir 中的所有图片文件
        image_files = [f for f in os.listdir(source_dir) if f.endswith(".jpeg")]

        if not image_files:
            print(f"在目录 {source_dir} 中未找到图片文件")
            return

        # 5. 遍历 image_files
        total_count = 0
        detected_count = 0
        not_detected_count = 0
        skipped_count = 0

        for image_file in image_files:
            total_count += 1
            image_path = os.path.join(source_dir, image_file)

            # 6. 读取图片并打印尺寸
            image = cv2.imread(image_path)
            if image is None:
                print(f"[{total_count}/{len(image_files)}] 无法读取图片：{image_file}")
                skipped_count += 1
                continue

            height, width, _ = image.shape
            print(f"[{total_count}/{len(image_files)}] {image_file}: 高度={height}, 宽度={width}")

            # 7. 根据图片高度执行不同的处理
            if height == 480:
                print("  图片高度为 480，顺时针旋转 90 度")
                image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                results = model(
                    image,
                    conf=conf_threshold,
                    max_det=max_detections
                )
            elif height == 640:
                # 8. 执行推理检测
                results = model(
                    image,
                    conf=conf_threshold,
                    max_det=max_detections
                )
            else:
                print(f"  跳过：图片高度 {height} 不是 480 或 640")
                not_detected_count += 1
                continue

            # 9. 处理并显示结果
            has_detection = False
            for result in results:
                # 判断是否检测到目标
                if result.boxes is not None and len(result.boxes) > 0:
                    has_detection = True

                    # 获取检测到的目标数量
                    num_detections = len(result.boxes)
                    print(f"  ✓ 检测到 {num_detections} 个目标")

                    # 获取每个检测目标的详细信息
                    for i, box in enumerate(result.boxes):
                        class_id = int(box.cls[0])
                        confidence = float(box.conf[0])
                        class_name = result.names[class_id]
                        print(f"    目标 {i + 1}: 类别={class_name}, 置信度={confidence:.4f}")
                    break

            # 10. 如果没有检测到目标
            if not has_detection:
                print("  ✗ 未检测到目标")
                not_detected_count += 1
                continue

            # 11. 把检测到的图片保存到 target_dir
            detected_count += 1
            target_path = os.path.join(target_dir, image_file)

            # 如果目标文件已存在，添加序号
            if os.path.exists(target_path):
                base, ext = os.path.splitext(image_file)
                counter = 1
                while os.path.exists(target_path):
                    new_filename = f"{base}_{counter}{ext}"
                    target_path = os.path.join(target_dir, new_filename)
                    counter += 1

            # 复制文件到目标目录
            shutil.copy2(image_path, target_path)
            print(f"  ✓ 已保存到：{target_path}")

        # 12. 输出统计信息
        print("\n" + "=" * 50)
        print(f"检测完成！")
        print(f"总图片数：{total_count}")
        print(f"成功处理数：{detected_count}")
        print(f"未检测到目标数：{not_detected_count}")
        print(f"跳过（无法读取）数：{skipped_count}")
        print(f"目标目录：{target_dir}")
        print("=" * 50)

    except Exception as e:
        print(f"程序运行中发生错误：{e}")


if __name__ == "__main__":
    source_dir = r"E:\images\dataset\src_"
    target_dir = r"E:\images\dataset\filter"
    filter(source_dir, target_dir)