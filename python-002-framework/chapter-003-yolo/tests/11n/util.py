from ultralytics import YOLO
import cv2
import os

try:
    # 加载YOLOv11预训练模型
    model = YOLO("../../model/wheel.pt")

    # 检查图片文件是否存在
    image_path = "dataset/dial/001.jpeg"
    if not os.path.exists(image_path):
        print(f"错误: 图片文件 {image_path} 不存在")
        exit(1)

    # 读取原始图像
    original_image = cv2.imread(image_path)

    # 检测图片
    results = model(image_path)

    # 处理结果并裁剪标注区域
    for i, result in enumerate(results):
        # 获取检测框坐标
        boxes = result.boxes
        if boxes is not None:
            for j, box in enumerate(boxes):
                # 获取边界框坐标
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

                # 裁剪区域
                cropped_region = original_image[y1:y2, x1:x2]

                # 将裁剪区域调整大小为320*100
                resized_region = cv2.resize(cropped_region, (320, 100))

                # 显示裁剪区域（原图和调整大小后）
                cv2.imshow(f"Cropped Region {j + 1}", cropped_region)
                cv2.imshow(f"Resized Region {j + 1}", resized_region)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                # 保存调整大小后的裁剪区域
                cv2.imwrite(f"resized_cropped_region_{i}_{j}.jpeg", resized_region)

        # 显示完整标注结果
        annotated_img = result.plot()
        cv2.imshow("标注结果", annotated_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

except Exception as e:
    print(f"发生错误: {e}")