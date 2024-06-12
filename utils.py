import csv

stolen_cars_db = "C:/Users/LENOVO/PycharmProjects/SmartTrafficControlSystem/assets/stolen_cars.csv"
stolen_cars = {}

def load_stolen_cars():
    global stolen_cars
    with open(stolen_cars_db, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            stolen_cars[row[0]] = True  # plate number as key, value is True if stolen

load_stolen_cars()  # Load the stolen cars database when the module is imported