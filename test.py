import cv2

# Mở camera
cam = cv2.VideoCapture(0)  # 0 là ID của camera mặc định

# Kiểm tra nếu camera không mở được
if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

# Lấy thông tin FPS của camera
fps = cam.get(cv2.CAP_PROP_FPS)

if fps == 0:
    print("Unable to determine FPS directly. Estimating manually...")

    # Đo FPS bằng cách tính số frame xử lý trong 5 giây
    import time
    start_time = time.time()
    frame_count = 0

    while time.time() - start_time < 5:  # Chạy trong 5 giây
        ret, frame = cam.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            break
        frame_count += 1

    elapsed_time = time.time() - start_time
    estimated_fps = frame_count / elapsed_time
    print(f"Estimated FPS: {estimated_fps:.2f}")
else:
    print(f"Camera FPS: {fps:.2f}")

cam.release()
