import os
import shutil
import random


def split_data(image_path, annotation_path, dataset_split_path, train_rate, val_rate):
    images = os.listdir(image_path)
    labels = os.listdir(annotation_path)
    images_no_ext = {os.path.splitext(image)[0]: image for image in images}
    labels_no_ext = {os.path.splitext(label)[0]: label for label in labels}
    matched_data = [(img, images_no_ext[img], labels_no_ext[img]) for img in images_no_ext if img in labels_no_ext]

    unmatched_images = [img for img in images_no_ext if img not in labels_no_ext]
    unmatched_labels = [label for label in labels_no_ext if label not in images_no_ext]
    if unmatched_images:
        print("未匹配的图片文件:")
        for img in unmatched_images:
            print(images_no_ext[img])
    if unmatched_labels:
        print("未匹配的标签文件:")
        for label in unmatched_labels:
            print(labels_no_ext[label])

    random.shuffle(matched_data)
    total = len(matched_data)
    train_data = matched_data[:int(train_rate * total)]
    val_data = matched_data[int(train_rate * total):int((train_rate + val_rate) * total)]
    test_data = matched_data[int((train_rate + val_rate) * total):]

    # 处理训练集
    for img_name, img_file, label_file in train_data:
        old_img_path = os.path.join(image_path, img_file)
        old_label_path = os.path.join(annotation_path, label_file)
        new_img_dir = os.path.join(dataset_split_path, 'train', 'images')
        new_label_dir = os.path.join(dataset_split_path, 'train', 'labels')
        os.makedirs(new_img_dir, exist_ok=True)
        os.makedirs(new_label_dir, exist_ok=True)
        shutil.copy(old_img_path, os.path.join(new_img_dir, img_file))
        shutil.copy(old_label_path, os.path.join(new_label_dir, label_file))
    # 处理验证集
    for img_name, img_file, label_file in val_data:
        old_img_path = os.path.join(image_path, img_file)
        old_label_path = os.path.join(annotation_path, label_file)
        new_img_dir = os.path.join(dataset_split_path, 'val', 'images')
        new_label_dir = os.path.join(dataset_split_path, 'val', 'labels')
        os.makedirs(new_img_dir, exist_ok=True)
        os.makedirs(new_label_dir, exist_ok=True)
        shutil.copy(old_img_path, os.path.join(new_img_dir, img_file))
        shutil.copy(old_label_path, os.path.join(new_label_dir, label_file))
    # 处理测试集
    for img_name, img_file, label_file in test_data:
        old_img_path = os.path.join(image_path, img_file)
        old_label_path = os.path.join(annotation_path, label_file)
        new_img_dir = os.path.join(dataset_split_path, 'tests', 'images')
        new_label_dir = os.path.join(dataset_split_path, 'tests', 'labels')
        os.makedirs(new_img_dir, exist_ok=True)
        os.makedirs(new_label_dir, exist_ok=True)
        shutil.copy(old_img_path, os.path.join(new_img_dir, img_file))
        shutil.copy(old_label_path, os.path.join(new_label_dir, label_file))
    print("数据集已划分完成")


if __name__ == '__main__':
    dataset_dir = '11n'
    dataset_name = 'dial_clip'
    image_path = rf"../{dataset_dir}/dataset/{dataset_name}/images"  # 图片文件夹
    annotation_path = rf"../{dataset_dir}/dataset/{dataset_name}/annotations"  # 标签文件夹
    dataset_split_path = rf"../{dataset_dir}/dataset/{dataset_name}/split"  # 新数据存放位置
    split_data(image_path, annotation_path, dataset_split_path, train_rate=0.9, val_rate=0.05)