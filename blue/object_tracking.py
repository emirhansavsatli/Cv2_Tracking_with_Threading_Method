import cv2
import time

class ColorObjectTracking:
    def __init__(self, lower_color, upper_color):
        self.lower_color = lower_color
        self.upper_color = upper_color
        self.x = 0
        self.y = 0
        self.take_screenshot = False
        self.screenshot_interval = 3
        self.screenshot_number = 0

    def detect_color(self, frame):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_mask = cv2.inRange(hsv_frame, self.lower_color, self.upper_color)
        contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(largest_contour)
            self.x = x + (w // 2)
            self.y = y + (h // 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            current_time = time.time()
            if self.take_screenshot and current_time - self.last_screenshot_time >= self.screenshot_interval:
                self.save_screenshot(frame)
                self.last_screenshot_time = current_time


            self.save_coordinates("coordinates.txt", self.x, self.y)



        return frame

    def save_screenshot(self, frame):
        self.screenshot_number += 1
        screenshot_filename = f"screen/detected_object_{self.screenshot_number}.jpg"
        cv2.imwrite(screenshot_filename, frame)
        print("Saved screenshot with number:", self.screenshot_number)

    def start_screenshot(self):
        self.take_screenshot = True
        self.last_screenshot_time = time.time()

    def stop_screenshot(self):
        self.take_screenshot = False

    def save_coordinates(self, filename, x, y):
        with open(filename, "a") as file:
            file.write(f"x: {x}, y: {y}\n")
