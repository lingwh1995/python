from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import requests

app = Flask(__name__)

# 全局变量存储模型
models = {}


def load_model(model_name):
    """
    加载YOLO预训练模型
    """
    global models
    if model_name not in models:
        models[model_name] = YOLO(f"../../../model/{model_name}")
    return models[model_name]


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


def recognize_wheel_image_from_url_v1(image_url, confidence_threshold=0.5, max_detections=10, iou_threshold=0.5):
    """
    从URL识别表盘刻度轮区域 (版本1)
    """
    try:
        # 加载模型
        model = load_model("wheel.pt")

        # 从URL下载图片
        image = download_image_from_url(image_url)

        # 检测图片
        results = model(
            image,
            conf=confidence_threshold,
            max_det=max_detections,
            iou=iou_threshold
        )

        # 处理结果
        detected_numbers = []

        for result in results:
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
                for bbox, class_id, confidence in zip(xyxy, class_ids, confidences):
                    x1, y1, x2, y2 = bbox
                    class_name = names.get(int(class_id), f"类别{int(class_id)}")
                    # 使用中心点x坐标进行排序
                    center_x = (x1 + x2) / 2
                    detections.append({
                        'center_x': float(center_x),
                        'class_name': class_name
                    })

                # 按中心点x坐标排序
                sorted_detections = sorted(detections, key=lambda x: x['center_x'])

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


def recognize_wheel_image_from_url_v2(image_url, confidence_threshold=0.5, max_detections=10, iou_threshold=0.5):
    """
    从URL识别表盘刻度轮区域 (版本2)
    """
    try:
        # 加载模型
        dial_model = load_model("dial.pt")

        # 从URL下载图片
        image = download_image_from_url(image_url)

        # 根据dial_model识别表盘区域
        dial_results = dial_model(image, conf=confidence_threshold, max_det=max_detections, iou=iou_threshold)

        # 提取裁剪区域
        processed_image = image  # 默认使用原图
        if len(dial_results) > 0 and dial_results[0].boxes is not None:
            # 获取第一个检测框的坐标
            boxes = dial_results[0].boxes.xyxy.cpu().numpy()
            if len(boxes) > 0:
                x1, y1, x2, y2 = map(int, boxes[0])  # 取第一个检测框
                # 裁剪图像
                processed_image = image[y1:y2, x1:x2]

                # 如果裁剪失败或区域太小，使用原图
                if processed_image.size == 0 or processed_image.shape[0] < 10 or processed_image.shape[1] < 10:
                    processed_image = image

        clip_model = load_model("dial_clip.pt")

        # 检测图片
        results = clip_model(
            processed_image,
            conf=0.2,  # 置信度阈值
            max_det=5,  # 最大检测数量限制
            iou=0.4  # NMS IoU阈值
        )

        # 处理结果
        detected_numbers = []

        for result in results:
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
                for bbox, class_id, confidence in zip(xyxy, class_ids, confidences):
                    x1, y1, x2, y2 = bbox
                    class_name = names.get(int(class_id), f"类别{int(class_id)}")
                    # 使用中心点x坐标进行排序
                    center_x = (x1 + x2) / 2
                    detections.append({
                        'center_x': float(center_x),
                        'class_name': class_name
                    })

                # 按中心点x坐标排序
                sorted_detections = sorted(detections, key=lambda x: x['center_x'])

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
            'code': 500,
            'msg': '处理失败',
            'error': str(e)
        }


@app.route('/api/water_meter/recognize/1', methods=['POST'])
def recognize_api_v1():
    """
    接收图片URL并返回识别结果 (版本1)
    """
    try:
        # 获取请求数据
        data = request.get_json()
        image_url = data.get('uri')

        # 获取可选参数
        confidence_threshold = float(data.get('confidence_threshold', 0.2))
        max_detections = int(data.get('max_detections', 5))
        iou_threshold = float(data.get('iou_threshold', 0.4))

        if not image_url:
            return jsonify({
                'success': False,
                'error': 'Missing image_url parameter'
            }), 400

        # 执行识别，传入参数
        result = recognize_wheel_image_from_url_v1(
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


@app.route('/api/water_meter/recognize/2', methods=['POST'])
def recognize_api_v2():
    """
    接收图片URL并返回识别结果 (版本2)
    """
    try:
        # 获取请求数据
        data = request.get_json()
        image_url = data.get('uri')

        # 获取可选参数
        confidence_threshold = float(data.get('confidence_threshold', 0.2))
        max_detections = int(data.get('max_detections', 5))
        iou_threshold = float(data.get('iou_threshold', 0.4))

        if not image_url:
            return jsonify({
                'code': 400,
                'msg': '缺少image_url参数',
                'data': ''
            }), 400

        # 执行识别，传入参数
        result = recognize_wheel_image_from_url_v2(
            image_url,
            confidence_threshold=confidence_threshold,
            max_detections=max_detections,
            iou_threshold=iou_threshold
        )

        status_code = result.get('code', 200)
        return jsonify(result), status_code if status_code != 200 else 200

    except Exception as e:
        return jsonify({
            'code': 500,
            'msg': '服务器内部错误',
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
    load_model("wheel.pt")
    load_model("dial.pt")
    load_model("dial_clip.pt")
    app.run(host='0.0.0.0', port=6000, debug=True)
