import cv2

"""
    视频处理
        视频处理的基本概念
            视频处理是计算机视觉和图像处理领域的一个重要分支，它涉及到处理图像序列以实现某种特定的效果或提取有用的信息。本章节将对视频处理的相关概念
            和操作进行详细介绍，以帮助读者更好地理解和应用视频处理技术。
        视频处理的目的   
            视频处理指的是使用计算机技术对视频信号进行分析、处理、编辑、合成等一系列操作的过程。视频信号由连续的帧序列组成，每一帧都是一个独立的图像。
            视频处理的目的包括改善视频质量、实现特定的视觉效果、提取视频中的关键信息、压缩视频文件大小、进行视频内容分析等。
        视频处理的应用包括但不限于
            去噪 ：从视频中移除噪声或不需要的信号。
            编码和解码 ：压缩视频文件以节省存储空间，以及将压缩的视频文件解压以便观看。
            帧率转换 ：改变视频的播放速率，例如，慢动作或快进效果。
            分辨率转换 ：调整视频的大小以适应不同的显示设备。
            颜色校正 ：调整视频中颜色的亮度、对比度和饱和度。
            视频分割 ：将视频分割成单独的片段，便于后续处理或分析。
"""


def opencv_video_01():
    """
        使用opencv加载视频

        opencv 常用库函数第三部分

        cv2.VideoWriter() 函数用于创建视频写入对象。
        cv2.VideoWriter_fourcc() 函数用于创建视频编码fourcc。
        cv2.VideoCapture() 函数用于创建视频读取对象。
        cv2.VideoCapture.read() 函数用于读取视频帧。
        cv2.VideoCapture.release() 函数用于释放视频对象。
    """
    # 加载视频
    cap = cv2.VideoCapture('d://opencv//sunset.mp4')

    # 检查视频是否加载成功
    if not cap.isOpened():
        raise IOError("cannot open video......")

    # 读取视频的帧并显示
    while True:
        ret, frame = cap.read()  # ret为布尔值，指示读取是否成功；frame为读取到的帧
        if not ret:
            break  # 如果没有读取到帧，则退出循环
        cv2.imshow('Frame', frame)  # 显示当前帧
        # 按'q'键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源并关闭窗口
    cap.release()
    cv2.destroyAllWindows()


def opencv_video_02():
    """
        使用opencv将视频转换为灰度视频
    """
    # 加载视频
    cap = cv2.VideoCapture('d://opencv//sunset.mp4')

    # 设置视频的编码器和输出视频的属性
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 获取输入视频的实际分辨率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter('d://opencv//output_video.avi', fourcc, 20.0, (width, height), False)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # 对帧进行操作，例如，这里我们简单地将帧转换为灰度
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray_frame)  # 写入帧到输出视频
        cv2.imshow('Frame', gray_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按'q'键退出
            break

    # 释放资源
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def main():
    # opencv_video_01()
    opencv_video_02()


if __name__ == "__main__":
    main()
