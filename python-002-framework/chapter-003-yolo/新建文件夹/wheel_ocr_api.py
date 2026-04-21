from flask import Flask, request, jsonify
from ultralytics import YOLO
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
        models[model_name] = YOLO(f"model/{model_name}")
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


import cv2
import numpy as np

# def parse_roll_label(roll_class_name, wheel_img):
#     try:
#         base_digit = int(roll_class_name.split('_')[-1])
#         next_digit = (base_digit + 1) % 10
#
#         # 1. 预处理：极度强化对比度，把反光压下去，把 1 提起来
#         gray = cv2.cvtColor(wheel_img, cv2.COLOR_BGR2GRAY)
#         # 强制增加局部对比度
#         clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(4, 4))
#         gray = clahe.apply(gray)
#         _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#
#         # 2. 核心：计算每一行的像素和 (水平投影)
#         # 统计每一行有多少个白色像素点
#         row_sums = np.sum(binary, axis=1)
#         h = len(row_sums)
#
#         # 3. 寻找“分界线”：在图像中部寻找像素最少的那一行
#         # 排除掉最顶部和最底部的边框干扰，只看中间 60% 的区域
#         search_start = int(h * 0.2)
#         search_end = int(h * 0.8)
#
#         # 找到像素和最小的行索引
#         min_row_index = np.argmin(row_sums[search_start:search_end]) + search_start
#
#         # 4. 判定逻辑：
#         # 如果分界线在窗口的上半部（索引较小），说明下面的数字占据了大部分空间
#         # 对于你的图，0在下、1在上的逻辑如果反了，请注意调整 base/next
#         # 水表通常是 [旧数字在上，新数字从下往上冒]
#         # 如果 1 在下面露出很多，分界线应该在偏上的位置
#         if min_row_index < (h * 0.5):
#             return str(next_digit)  # 下方新数字占优
#         else:
#             return str(base_digit)  # 上方旧数字占优
#
#     except Exception as e:
#         return roll_class_name.split('_')[-1]


def recognize_wheel_image_from_url_v2(image_url, confidence_threshold=0.2, max_detections=10, iou_threshold=0.5):
    """
    优化后的主识别流程 (已添加图片显示)
    """
    try:
        # 建议：模型加载应放在函数外作为全局变量，避免每次调用重复加载
        dial_model = load_model("dial.pt")
        image = download_image_from_url(image_url)

        # 步骤1：定位表盘/字轮总区域
        dial_results = dial_model(image, conf=confidence_threshold, max_det=max_detections, iou=iou_threshold)

        processed_image = image
        if len(dial_results) > 0 and dial_results[0].boxes is not None:
            boxes = dial_results[0].boxes.xyxy.cpu().numpy()
            if len(boxes) > 0:
                x1, y1, x2, y2 = map(int, boxes[0])
                processed_image = image[y1:y2, x1:x2]

        # 步骤2：识别各个数字位（包含 roll 标签）
        clip_model = load_model("dial_clip.pt")
        results = clip_model(processed_image, conf=0.2, max_det=5, iou=0.4)

        detected_numbers = []
        if len(results) > 0:
            result = results[0]
            boxes = result.boxes

            detections = []
            for bbox, class_id in zip(boxes.xyxy.cpu().numpy(), boxes.cls.cpu().numpy()):
                class_name = result.names.get(int(class_id), "")
                detections.append({
                    'center_x': (bbox[0] + bbox[2]) / 2,
                    'class_name': class_name,
                    'bbox': bbox
                })

            # 按水平位置从左到右排序
            sorted_detections = sorted(detections, key=lambda x: x['center_x'])

            # 步骤3：处理每一个检测到的位
            for det in sorted_detections:
                c_name = det['class_name']
                # 打印c_name
                print(f"c_name: {c_name}")
                if not c_name.startswith("roll"):
                    detected_numbers.append(c_name)
                else:
                    real_digit = str(int(c_name.split('_')[-1]))
                    detected_numbers.append(real_digit)

            # ======================= 添加：显示识别后的图片 =======================
            annotated_img = result.plot()  # 获取画好框的图片
            final_data = ''.join(detected_numbers)

            # 在图上左上角写出最终判定的结果串
            cv2.putText(annotated_img, f"Read: {final_data}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            #cv2.imshow("Recognition Result", annotated_img)
            #cv2.waitKey(0)  # 等待按任意键关闭窗口
            #cv2.destroyAllWindows()
            # =================================================================

        return {
            'code': 200,
            'msg': '处理成功',
            'data': ''.join(detected_numbers)
        }

    except Exception as e:
        return {'code': 500, 'msg': str(e)}

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
