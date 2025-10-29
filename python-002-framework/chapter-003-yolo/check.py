from ultralytics import YOLO
import cv2
import os

try:
    # 加载YOLOv11预训练模型
    model = YOLO("./water_meter_experiment2/weights/best.pt")

    # 检查图片文件是否存在
    image_path = "train_883.jpg"
    if not os.path.exists(image_path):
        print(f"错误: 图片文件 {image_path} 不存在")
        exit(1)

    # 检测图片
    results = model(image_path)

    # 处理结果
    for result in results:
        annotated_img = result.plot()
        cv2.imshow("YOLOv11 Detection", annotated_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

except Exception as e:
    print(f"发生错误: {e}")