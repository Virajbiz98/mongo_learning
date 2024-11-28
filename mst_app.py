import streamlit as st
from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to MongoDB
client = MongoClient("mongodb+srv://DEVMONGO:DEVMONGO@cluster0.wcbtj.mongodb.net/")
db = client['first_project']
collection = db['cpu_temperature']

# Fetch data from MongoDB
def get_data():
    # Example: Two datasets (PTC-1 and PTC-2)
    data = list(collection.find({}, {"_id": 0}))
    st.write("Fetched Data from MongoDB:", data)  # Debug: Display data in Streamlit

    # Filter and extract two datasets
    ptc1_data = [item for item in data if item.get("sensor") == "PTC-1"]
    ptc2_data = [item for item in data if item.get("sensor") == "PTC-2"]

    # Extract times and temperatures for each sensor
    times_ptc1 = [item['time'] for item in ptc1_data]
    temps_ptc1 = [item['temperature'] for item in ptc1_data]

    times_ptc2 = [item['time'] for item in ptc2_data]
    temps_ptc2 = [item['temperature'] for item in ptc2_data]

    return times_ptc1, temps_ptc1, times_ptc2, temps_ptc2

# Streamlit app
st.title("CPU Temperature Variation for Multiple Sensors")

try:
    # Get data for both datasets
    times_ptc1, temps_ptc1, times_ptc2, temps_ptc2 = get_data()

    if not times_ptc1 or not temps_ptc1 or not times_ptc2 or not temps_ptc2:
        st.error("No valid data available to display. Please check your database.")
    else:
        # Set Seaborn style
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(12, 6))

        # Plot PTC-1 data
        plt.plot(times_ptc1, temps_ptc1, marker='s', color='red', label="PTC-1 (ΔT)")

        # Plot PTC-2 data
        plt.plot(times_ptc2, temps_ptc2, marker='o', color='blue', label="PTC-2 (ΔT)")

        # Chart labels and title
        plt.xlabel("Time of the Day", fontsize=14)
        plt.ylabel("Temperature (°C)", fontsize=14)
        plt.title("Temperature Variation Over Time", fontsize=18, fontweight="bold")

        # Rotate x-axis labels
        plt.xticks(rotation=45, fontsize=12)
        plt.yticks(fontsize=12)

        # Add legend and grid
        plt.legend(fontsize=12, loc="upper right")
        plt.grid(visible=True, linestyle="--", alpha=0.6)

        # Display the plot
        st.pyplot(plt)

except Exception as e:
    st.error(f"An error occurred: {e}")
