import os
import shutil
from pathlib import Path


def copy_files_by_name(src1_dir, src2_dir, target_dir):
    """
    从src1文件夹读取文件名，去掉'_clip'后缀，然后在src2中查找匹配的文件并复制到target目录

    Args:
        src1_dir: 源目录1路径 (包含_clip的文件)
        src2_dir: 源目录2路径 (原始文件)
        target_dir: 目标目录路径
    """
    # 创建目标目录（如果不存在）
    Path(target_dir).mkdir(parents=True, exist_ok=True)

    # 获取src1目录中的所有文件
    src1_files = [f for f in os.listdir(src1_dir) if os.path.isfile(os.path.join(src1_dir, f))]

    # 处理每个文件
    for filename in src1_files:
        # 分离文件名和扩展名
        name_parts = filename.rsplit('.', 1)
        base_name = name_parts[0]
        extension = name_parts[1] if len(name_parts) > 1 else ''

        # 去掉'_clip'后缀（如果存在）
        if base_name.endswith('_clip'):
            new_base_name = base_name[:-5]  # 移除'_clip'
        else:
            new_base_name = base_name

        # 构建新的文件名
        new_filename = f"{new_base_name}.{extension}" if extension else new_base_name

        # 检查src2中是否存在对应的文件
        src2_file_path = os.path.join(src2_dir, new_filename)
        if os.path.exists(src2_file_path):
            # 复制文件到目标目录
            target_file_path = os.path.join(target_dir, new_filename)
            shutil.copy2(src2_file_path, target_file_path)
            print(f"已复制: {new_filename}")
        else:
            print(f"未找到匹配文件: {new_filename} 在 {src2_dir}")

    print(f"文件复制完成。目标目录: {target_dir}")


# 使用示例
if __name__ == "__main__":
    src1_directory = "E:\images\dataset\dial_clip\images"
    src2_directory = "E:\images\dataset\dial\images"
    dest_directory = "E:\dest"

    copy_files_by_name(src1_directory, src2_directory, dest_directory)