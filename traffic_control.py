from vehicle_detection import process_video
from utils import stolen_cars

def control_lights(lane_1_count, lane_2_count, lane_1_violators, lane_2_violators):
    """
    Simulates traffic light control based on vehicle counts for two lanes.
    Args:
        lane_1_count (int): Number of cars detected in lane 1 video.
        lane_2_count (int): Number of cars detected in lane 2 video.
        lane_1_violators (list): List of violators (cars that passed the red light) in lane 1.
        lane_2_violators (list): List of violators (cars that passed the red light) in lane 2.
    """
    # Print individual lane counts
    print(f"Lane 1: {lane_1_count} vehicles detected")
    print(f"Lane 2: {lane_2_count} vehicles detected")

    # Print violators for each lane
    print("Violators in Lane 1:")
    for violator in lane_1_violators:
        print(f"Plate number: {violator['plate_number']}, Time: {violator['timestamp']}")
    print("Violators in Lane 2:")
    for violator in lane_2_violators:
        print(f"Plate number: {violator['plate_number']}, Time: {violator['timestamp']}")

    # Simple logic prioritizing the lane with the most vehicles
    if lane_1_count > lane_2_count:
        light_state = "Lane 1: Green Light On\nLane 2: Red Light On"
    else:
        light_state = "Lane 1: Red Light On\nLane 2: Green Light On"

    # Print the simulated traffic light state
    print(light_state)
