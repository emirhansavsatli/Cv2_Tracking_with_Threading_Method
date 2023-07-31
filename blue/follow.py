import time

class Tracking:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tracking_status = False
        self.tracking_speed = 0.5

    def track(self):
        self.tracking_status = True
        while self.tracking_status:
            print("x:", self.x, "y:", self.y)
            time.sleep(self.tracking_speed)

    def stop(self):
        self.tracking_status = False
