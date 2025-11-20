from ultralytics import YOLO
import cv2
import os

"""
    测试表盘刻度轮区域识别模型
"""
try:
    # 加载YOLOv11预训练模型
    model = YOLO("model/wheel.pt")

    # 检查图片文件是否存在
    image_path = "data/wheel/006.jpeg"
    if not os.path.exists(image_path):
        print(f"错误: 图片文件 {image_path} 不存在")
        exit(1)

    # 检测图片
    results = model(image_path)

    # 处理结果并按x坐标排序
    for i, result in enumerate(results):
        # 获取检测框信息
        boxes = result.boxes
        if boxes is not None:
            # 获取边界框坐标
            xyxy = boxes.xyxy.cpu().numpy()  # 获取(x1, y1, x2, y2)坐标
            class_ids = boxes.cls.cpu().numpy()
            confidences = boxes.conf.cpu().numpy()

            # 获取类别名称
            names = result.names if hasattr(result, 'names') else {}

            # 创建包含所有信息的列表
            detections = []
            for idx, (bbox, class_id, confidence) in enumerate(zip(xyxy, class_ids, confidences)):
                x1, y1, x2, y2 = bbox
                class_name = names.get(int(class_id), f"类别{int(class_id)}")
                # 使用中心点x坐标进行排序
                center_x = (x1 + x2) / 2
                detections.append({
                    'index': idx,
                    'center_x': center_x,
                    'x1': x1,
                    'y1': y1,
                    'x2': x2,
                    'y2': y2,
                    'class_id': int(class_id),
                    'class_name': class_name,
                    'confidence': confidence
                })

            # 按中心点x坐标排序
            sorted_detections = sorted(detections, key=lambda x: x['center_x'])

            print(f"检测到 {len(sorted_detections)} 个目标 (按x坐标排序):")
            for j, detection in enumerate(sorted_detections):
                print(f"  目标 {j + 1}: {detection['class_name']} "
                      f"(ID: {detection['class_id']}, 置信度: {detection['confidence']:.2f}, "
                      f"中心x坐标: {detection['center_x']:.2f})")

            # 如果只需要打印识别的数字，按x坐标顺序
            detected_numbers = []
            for detection in sorted_detections:
                # if detection['class_name'].isdigit():
                #     detected_numbers.append(detection['class_name'])
                detected_numbers.append(detection['class_name'])

            if detected_numbers:
                print(f"按顺序识别到的数字: {''.join(detected_numbers)}")

        # 显示标注结果
        annotated_img = result.plot()
        cv2.imshow("标注结果", annotated_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

except Exception as e:
    print(f"发生错误: {e}")