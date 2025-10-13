import cv2


def opencv_video_operation():
    """
        使用opencv将视频转换为灰度视频
    """
    input_path = 'd://opencv//sunset.mp4'
    output_path = 'd://opencv//sunset_new.mp4'

    # 加载视频
    video = cv2.VideoCapture(input_path)

    # 设置视频的编码器和输出视频的属性
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # 获取输入视频的属性
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"视频信息 - 宽度: {width}, 高度: {height}, 帧率: {fps:.2f}, 总帧数: {total_frames}")

    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), False)

    if not out.isOpened():
        print("无法创建视频写入器")
        video.release()
        return

    while True:
        ret, frame = video.read()
        if not ret:
            break
        # 对帧进行操作，例如，这里我们简单地将帧转换为灰度
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray_frame)  # 写入帧到输出视频
        cv2.imshow('Frame', gray_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按'q'键退出
            break

    # 释放资源
    video.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    opencv_video_operation()
