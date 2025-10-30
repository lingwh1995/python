import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    # 加载基础模型（用预训练权重加速训练）
    model = YOLO('model/yolo11n-obb.pt')
    results = model.train(
        data='./config/water_meter.yml',  # 数据集配置文件的路径
        epochs=20,  # 训练轮数（新手建议20-50，数据多可增加）
        batch=16,  # 批量大小，即单次输入多少图片训练（GPU内存大则设大）
        imgsz=640,  # 训练图像尺寸
        workers=8,  # 加载数据的工作线程数
        device='cpu',  # 指定训练的计算设备，无nvidia显卡则改为 'cpu'（0=GPU，-1=CPU）
        optimizer='AdamW',  # 训练使用优化器，可选 auto,SGD,Adam,AdamW 等
        amp=True,  # True 或者 False, 解释为：自动混合精度(AMP) 训练
        cache=False,  # True 在内存中缓存数据集图像，服务器推荐开启
        verbose=True,  # 增加详细输出以便调试
        project='./',  # 训练结果存放的项目目录
        name='./run/water_meter_experiment',
        augment=True,  # 启用数据增强
        plots=False  # 禁用绘图功能避免错误
    )
