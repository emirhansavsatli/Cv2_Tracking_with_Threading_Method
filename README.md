# Cv2_Tracking_with_Threading_Method

This project is an application that performs real-time color object tracking and following using Python and the OpenCV library with a web camera. 
It includes the ColorObjectTracking and Tracking classes, 
which handle the object tracking and following tasks, respectively, while running them on separate threads to enhance performance.

Features:

  ▷ Color Object Tracking: Enables real-time tracking of a color object using a web camera. It detects and tracks the object within a specific color range.
  
  ▷ Object Tracking Coordinates: Determines and displays the position (x, y coordinates) of the tracked object on the screen.
 
  ▷ Screen Capture: Captures screenshots at regular intervals during the object tracking process and saves them to a specified folder.
  
  ▷ Parallel Processing: Utilizes separate threads for object tracking and following tasks to efficiently utilize the processor and improve performance.
  
  ▷ Stop Functionality: Allows the user to stop the object tracking and following tasks by pressing the "q" key.
  
  ▷ Customizable Color Range: The color range of the tracked object can be customized and adjusted.
  
  ▷ Coordinate Recording: Saves the coordinates of the tracked object to a file for further reference.
