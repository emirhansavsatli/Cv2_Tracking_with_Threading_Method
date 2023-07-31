import cv2
import threading
from object_tracking import ColorObjectTracking
from follow import Tracking

def run_camera(color_object_tracking, tracking_class):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Failed to open camera.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame = color_object_tracking.detect_color(frame)

        cv2.imshow('Object Tracking', frame)

        tracking_class.x = color_object_tracking.x
        tracking_class.y = color_object_tracking.y

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

    tracking_class.stop()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    color_object_tracking = ColorObjectTracking(lower_color=(100, 50, 50), upper_color=(130, 255, 255))
    color_object_tracking.start_screenshot()

    tracking_class = Tracking()
    tracking_thread = threading.Thread(target=tracking_class.track)

    camera_thread = threading.Thread(target=run_camera, args=(color_object_tracking, tracking_class))

    tracking_thread.start()
    camera_thread.start()

    camera_thread.join()
    tracking_thread.join()
