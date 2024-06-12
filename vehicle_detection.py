import datetime

from imutils.video import VideoStream
from imutils.object_detection import non_max_suppression
import cv2
import numpy as np
import pytesseract

# Assuming you have a pre-trained Haar cascade classifier for car detection (replace with your classifier path)
car_cascade = cv2.CascadeClassifier("C:/Users/LENOVO/PycharmProjects/SmartTrafficControlSystem/assets/cars.xml")

# Define the stop line coordinates (hardcoded for simplicity, adjust according to your camera setup)
stop_line_x, stop_line_y = 300, 400

def process_video(video_path, stolen_cars):
    """
    Processes a video and returns vehicle count and violators for a single lane.
    Args:
        video_path (str): Path to the video file.
        stolen_cars (dict): Dictionary of stolen car plate numbers.
    Returns:
        int: Number of cars detected in the video.
        list: List of violators (cars that passed the red light) with plate numbers and timestamps.
    """
    # Open the video file using OpenCV VideoStream
    vs = VideoStream(src=video_path).start()
    # Initialize counter for vehicles
    vehicle_count = 0
    # Initialize list for violators
    violators = []
    # Loop through the frames of the video
    while True:
        # Read a frame from the video stream
        frame = vs.read()
        # Break the loop if there are no more frames
        if frame is None:
            break
        # Convert the frame to grayscale (might be required for some car detection algorithms)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect cars in the frame using the Haar cascade classifier
        cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        # Apply non-maxima suppression to eliminate overlapping bounding boxes
        cars = non_max_suppression(cars, probs=None)
        # Loop through the detected cars and draw bounding boxes (for visualization purposes)
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            vehicle_count += 1
            # Check if the car has crossed the stop line
            if y + h > stop_line_y:
                # Extract the license plate region of interest (ROI)
                plate_roi = gray[y:y+h, x:x+w]
                # Use OCR to extract the plate number
                plate_number = pytesseract.image_to_string(plate_roi, config='--psm 11')
                # Check if the plate number is in the stolen cars database
                if plate_number in stolen_cars:
                    violators.append({'plate_number': plate_number, 'timestamp': datetime.now()})
        # Display the frame with detected cars (optional for visualization)
        cv2.imshow("Frame", frame)
        # Press 'q' to quit the program
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    # Release resources
    vs.stop()
    cv2.destroyAllWindows()
    # Return the total vehicle count and violators
    return vehicle_count, violators