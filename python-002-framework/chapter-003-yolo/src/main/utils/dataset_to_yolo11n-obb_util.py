import math
import xml.etree.ElementTree as ET
from pathlib import Path


def convert_single_xml_to_yolo(xml_file_path, class_mapping):
    """
    将单个XML文件转换为YOLO格式

    Args:
        xml_file_path: XML文件路径
        class_mapping: 类别映射字典 {class_name: class_id}

    Returns:
        str: YOLO格式的标注字符串
    """
    try:
        # 解析XML文件
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # 获取图像尺寸
        size = root.find('size')
        if size is None:
            raise ValueError("缺少size标签")

        width = int(size.find('width').text)
        height = int(size.find('height').text)

        yolo_annotations = []

        # 遍历所有object标签
        for obj in root.findall('object'):
            # 获取类别名称
            name_elem = obj.find('name')
            if name_elem is None or not name_elem.text:
                continue

            class_name = name_elem.text.strip()
            if class_name not in class_mapping:
                print(f"警告: 未知类别 '{class_name}' 在文件 {xml_file_path} 中")
                continue

            class_id = class_mapping[class_name]

            # 处理bndbox格式（标准边界框）
            bndbox = obj.find('bndbox')
            if bndbox is not None:
                x_min = float(bndbox.find('xmin').text)
                y_min = float(bndbox.find('ymin').text)
                x_max = float(bndbox.find('xmax').text)
                y_max = float(bndbox.find('ymax').text)
                angle = 0.0  # 默认角度为0

                # 转换为YOLO格式 (中心点x, 中心点y, 宽度, 高度)
                x_center = ((x_min + x_max) / 2) / width
                y_center = ((y_min + y_max) / 2) / height
                bbox_width = (x_max - x_min) / width
                bbox_height = (y_max - y_min) / height

                # 正确的OBB格式输出（6列）
                yolo_annotations.append(
                    f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f} {angle:.6f}")
                continue

            # 处理robndbox格式（旋转边界框）
            robndbox = obj.find('robndbox')
            if robndbox is not None:
                cx = float(robndbox.find('cx').text)
                cy = float(robndbox.find('cy').text)
                w = float(robndbox.find('w').text)
                h = float(robndbox.find('h').text)

                # 获取旋转角度并转换为弧度
                angle_elem = robndbox.find('angle')
                if angle_elem is not None:
                    angle_degrees = float(angle_elem.text)
                    # 确保角度在合理范围内
                    angle_degrees = angle_degrees % 360  # 保持在0-360范围内
                    # 转换为弧度
                    angle = math.radians(angle_degrees)
                else:
                    angle = 0.0  # 默认角度为0

                # 转换为中心点和尺寸的归一化格式
                x_center = cx / width
                y_center = cy / height
                bbox_width = w / width
                bbox_height = h / height

                # 正确的OBB格式输出（6列）
                yolo_annotations.append(
                    f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f} {angle:.6f}")
                continue

        return '\n'.join(yolo_annotations)

    except Exception as e:
        print(f"处理文件 {xml_file_path} 时出错: {e}")
        return ""


def batch_convert_xml_to_yolo(xml_folder, output_folder, class_mapping):
    """
    批量转换文件夹中的XML文件为YOLO格式

    Args:
        xml_folder: 包含XML文件的文件夹路径
        output_folder: 输出TXT文件的文件夹路径
        class_mapping: 类别映射字典 {class_name: class_id}
    """
    # 创建输出文件夹
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # 统计信息
    success_count = 0
    error_count = 0

    # 遍历所有XML文件
    xml_path = Path(xml_folder)
    for xml_file in xml_path.glob('*.xml'):
        try:
            # 转换并保存
            yolo_data = convert_single_xml_to_yolo(str(xml_file), class_mapping)
            if yolo_data:
                # 生成输出文件路径
                txt_filename = xml_file.stem + '.txt'
                txt_path = Path(output_folder) / txt_filename

                # 写入YOLO格式文件
                with open(txt_path, 'w', encoding='utf-8') as f:
                    f.write(yolo_data)

                print(f"✓ 已转换: {xml_file.name} -> {txt_filename}")
                success_count += 1
            else:
                print(f"✗ 转换失败: {xml_file.name}")
                error_count += 1

        except Exception as e:
            print(f"✗ 处理文件 {xml_file.name} 时出错: {e}")
            error_count += 1

    print(f"\n转换完成! 成功: {success_count}, 失败: {error_count}")


# 使用示例
if __name__ == "__main__":
    # 定义类别映射 (根据实际需求修改)
    class_mapping = {
        'character_wheel': 0
    }

    # 设置输入和输出文件夹路径
    xml_folder = r'E:\images\water_meter\annotations'  # 当前目录
    output_folder = r'E:\images\water_meter\labels'  # 输出文件夹

    # 执行批量转换
    batch_convert_xml_to_yolo(xml_folder, output_folder, class_mapping)