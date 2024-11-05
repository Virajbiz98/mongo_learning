import wmi
from connect import collection
import time


# Function to connect to OpenHardwareMonitor
def connect_to_ohm():
    try:
        # Attempt to connect to OpenHardwareMonitor namespace
        return wmi.WMI(namespace=r"root\OpenHardwareMonitor")
    except wmi.x_wmi as e:
        print("Error: Cannot access OpenHardwareMonitor namespace. Ensure OpenHardwareMonitor is running.")
        return None

# Connect to OpenHardwareMonitor
w = connect_to_ohm()
if not w:
    exit("Exiting: OpenHardwareMonitor is not running or cannot be accessed.")

# Function to get CPU temperature
def get_cpu_temperature():
    temperature = None
    try:
        sensors = w.Sensor()
        for sensor in sensors:
            if sensor.SensorType == 'Temperature' and "CPU" in sensor.Name:
                temperature = sensor.Value  # Temperature in Celsius
                break
    except Exception as e:
        print(f"Error reading temperature: {e}")
    
    return temperature

# Main loop to log temperature every minute
while True:
    temp = get_cpu_temperature()
    if temp is not None:
        collection.insert_one({"temperature": temp, "timestamp": time.time()})
        print(f"Logged CPU temperature: {temp}°C")
    else:
        print("Failed to get CPU temperature.")
    
    # Wait for 1 minute
    time.sleep(60)
