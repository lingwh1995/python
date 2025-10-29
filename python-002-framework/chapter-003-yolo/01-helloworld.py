"""
    1.搭建yolo环境
        # 安装Python（建议3.8-3.11）
        # 安装PyTorch（根据CUDA版本选择，无GPU选CPU版）
        pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  # 有GPU
        # 或
        pip3 install torch torchvision torchaudio  # 无GPU

        # 安装YOLOv11官方库（Ultralytics）
        pip install ultralytics

        # 验证安装
        python -c "from ultralytics import YOLO; print('YOLOv11 installed successfully')"

        # 安装LabelImg
        pip install labelImg
    2.目标检测基础概念
        目标检测：同时预测图像中物体的位置（边界框）和类别。
        边界框：用 (x1, y1, x2, y2) 表示（左上角和右下角坐标）。
        YOLO 核心思想：将图像分成网格，每个网格预测多个边界框和类别概率。
"""