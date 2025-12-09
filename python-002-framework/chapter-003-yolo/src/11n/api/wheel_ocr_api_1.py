from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import requests

app = Flask(__name__)

# 全局变量存储模型
model = None


def load_model():
    """
    加载YOLO预训练模型
    """
    global model
    if model is None:
        model = YOLO("../../../model/wheel.pt")
    return model


def download_image_from_url(image_url):
    """
    从URL下载图片并转换为OpenCV格式

    Args:
        image_url (str): 图片URL地址

    Returns:
        numpy.ndarray: OpenCV格式的图像数组
    """
    response = requests.get(image_url)
    response.raise_for_status()

    # 将图片数据转换为numpy数组
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    # 使用OpenCV解码图像
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    return image


def recognize_wheel_image_from_url(image_url, confidence_threshold=0.5, max_detections=10, iou_threshold=0.5):
    """
    从URL识别表盘刻度轮区域

    Args:
        image_url (str): 图片URL地址
        confidence_threshold (float): 置信度阈值，默认0.5
        max_detections (int): 最大检测数量，默认100
        iou_threshold (float): IOU阈值，默认0.5

    Returns:
        dict: 识别结果
    """
    try:
        # 加载模型
        model = load_model()

        # 从URL下载图片
        image = download_image_from_url(image_url)

        # 检测图片 - 添加最大检测数量限制和NMS IoU阈值调节
        results = model(
            image,
            conf=0.2,  # 置信度阈值
            max_det=5,  # 最大检测数量限制
            iou=0.4  # NMS IoU阈值
        )

        # 处理结果
        recognition_result = []
        detected_numbers = []

        for i, result in enumerate(results):
            boxes = result.boxes
            if boxes is not None:
                # 获取边界框坐标
                xyxy = boxes.xyxy.cpu().numpy()
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
                        'index': int(idx),  # 转换为Python原生类型
                        'center_x': float(center_x),  # 转换为Python原生类型
                        'x1': float(x1),  # 转换为Python原生类型
                        'y1': float(y1),  # 转换为Python原生类型
                        'x2': float(x2),  # 转换为Python原生类型
                        'y2': float(y2),  # 转换为Python原生类型
                        'class_id': int(class_id),  # 转换为Python原生类型
                        'class_name': class_name,
                        'confidence': float(confidence)  # 转换为Python原生类型
                    })

                # 按中心点x坐标排序
                sorted_detections = sorted(detections, key=lambda x: x['center_x'])

                recognition_result.extend(sorted_detections)

                # 收集识别的数字
                for detection in sorted_detections:
                    detected_numbers.append(detection['class_name'])

        return {
            'code': 200,
            'msg': '处理成功',
            'data': ''.join(detected_numbers) if detected_numbers else ''
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


@app.route('/api/water_meter/recognize/1', methods=['POST'])
def recognize_api():
    """
    接收图片URL并返回识别结果

    请求参数:
        - image_url: 图片URL地址
        - confidence_threshold: 置信度阈值(可选，默认0.5)
        - max_detections: 最大检测数量(可选，默认10)
        - iou_threshold: IOU阈值(可选，默认0.5)

    返回:
        - success: 是否成功
        - result: 识别结果或错误信息
    """
    try:
        # 获取请求数据
        data = request.get_json()
        image_url = data.get('uri')

        # 获取可选参数
        confidence_threshold = data.get('confidence_threshold', 0.2)
        max_detections = data.get('max_detections', 5)
        iou_threshold = data.get('iou_threshold', 0.4)

        if not image_url:
            return jsonify({
                'success': False,
                'error': 'Missing image_url parameter'
            }), 400

        # 执行识别，传入参数
        result = recognize_wheel_image_from_url(
            image_url,
            confidence_threshold=confidence_threshold,
            max_detections=max_detections,
            iou_threshold=iou_threshold
        )

        return jsonify(result)

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """
    健康检查接口
    """
    return jsonify({
        'status': 'healthy',
        'message': 'Wheel recognition service is running'
    })


if __name__ == '__main__':
    # 应用启动时加载模型
    load_model()
    app.run(host='0.0.0.0', port=6000, debug=True)
