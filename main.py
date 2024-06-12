import vehicle_detection
import traffic_control
from utils import stolen_cars, stolen_cars_db

# Video paths for two lanes
video_path1 = "C:/Users/LENOVO/PycharmProjects/SmartTrafficControlSystem/assets/cars2.mp4"
video_path2 = "C:/Users/LENOVO/PycharmProjects/SmartTrafficControlSystem/assets/cars2.mp4"


# Process video 1 and get vehicle count
lane_1_count, lane_1_violators = vehicle_detection.process_video(video_path1, stolen_cars)

# Process video 2 and get vehicle count
lane_2_count, lane_2_violators = vehicle_detection.process_video(video_path2, stolen_cars)

# Control traffic lights based on individual lane counts
traffic_control.control_lights(lane_1_count, lane_2_count, lane_1_violators, lane_2_violators)
