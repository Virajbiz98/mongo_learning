import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
from typing import List, Tuple
import logging
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class CPUTemperatureMonitor:
    def __init__(self):
        """
        Initialize MongoDB connection and Streamlit configuration
        """
        try:
            # Load MongoDB URI and check if it's available
            mongo_url = os.getenv("MONGODB_URL", "")
            if not mongo_url:
                raise ValueError("MongoDB connection URL (MONGODB_URL) is missing in the .env file.")

            # Test MongoDB connection
            self.client = MongoClient(mongo_url)
            self.client.server_info()  # This will raise an exception if MongoDB is unreachable or wrong credentials

            # MongoDB Database and Collection
            self.db = self.client[os.getenv("MONGODB_DATABASE", "first_project")]
            self.collection = self.db[os.getenv("MONGODB_COLLECTION", "cpu_temperature")]

            # Log success
            logger.info("Successfully connected to MongoDB")

            # Streamlit page configuration
            st.set_page_config(
                page_title="CPU Temperature Dashboard",
                page_icon="🌡️",
                layout="wide"
            )
        
        except Exception as e:
            logger.error(f"Initialization error: {e}")
            st.error(f"Failed to initialize application. Error: {str(e)}")
            raise  # Raise the exception to stop further execution

    def fetch_temperature_data(self) -> Tuple[List[str], List[float], List[str], List[float]]:
        """
        Retrieve temperature data from MongoDB

        Returns:
            Tuple of times and temperatures for two sensors
        """
        try:
            # Fetch all data from MongoDB
            data = list(self.collection.find({}, {"_id": 0}))
            
            if not data:
                st.warning("No data available in the database.")
                return [], [], [], []

            # Filter data by sensor type
            ptc1_data = [item for item in data if item.get("sensor") == "PTC-1"]
            ptc2_data = [item for item in data if item.get("sensor") == "PTC-2"]

            # Extract times and temperatures for each sensor
            times_ptc1 = [item["time"] for item in ptc1_data]
            temps_ptc1 = [item["temperature"] for item in ptc1_data]
            times_ptc2 = [item["time"] for item in ptc2_data]
            temps_ptc2 = [item["temperature"] for item in ptc2_data]

            return times_ptc1, temps_ptc1, times_ptc2, temps_ptc2

        except Exception as e:
            logger.error(f"Data fetching error: {e}")
            st.error(f"Failed to retrieve temperature data. Error: {str(e)}")
            return [], [], [], []

    def plot_temperature_variation(self):
        """
        Create and display temperature variation plot
        """
        # Fetch temperature data
        times_ptc1, temps_ptc1, times_ptc2, temps_ptc2 = self.fetch_temperature_data()

        if not times_ptc1 or not temps_ptc1:
            st.info("Insufficient data to generate the chart.")
            return

        # Set up the plot styling
        sns.set_theme(style="whitegrid", palette="deep")
        plt.figure(figsize=(14, 7))

        # Plot data for both sensors with styling
        plt.plot(times_ptc1, temps_ptc1,
                 marker="s",
                 linestyle="-",
                 linewidth=2,
                 color="crimson",
                 label="PTC-1 Sensor")

        plt.plot(times_ptc2, temps_ptc2,
                 marker="o",
                 linestyle="--",
                 linewidth=2,
                 color="navy",
                 label="PTC-2 Sensor")

        # Chart configuration
        plt.title("CPU Temperature Monitoring Dashboard",
                  fontsize=20,
                  fontweight="bold",
                  color="#333333")
        plt.xlabel("Time of Day", fontsize=15)
        plt.ylabel("Temperature (°C)", fontsize=15)

        plt.xticks(rotation=45, ha="right")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend(loc="best", frameon=True, shadow=True)

        plt.tight_layout()
        st.pyplot(plt)

    def run(self):
        """
        Main application runner
        """
        st.title("🌡️ CPU Temperature Monitoring")

        # Sidebar information
        st.sidebar.header("Dashboard Information")
        st.sidebar.info("""
        ### Temperature Monitoring System
        - Real-time CPU temperature tracking
        - Multiple sensor support
        - Advanced data visualization
        """)

        # Plot the temperature variation graph
        self.plot_temperature_variation()


def main():
    """
    Entry point of the application
    """
    try:
        monitor = CPUTemperatureMonitor()
        monitor.run()
    except Exception as e:
        logger.critical(f"Application crashed: {e}")
        st.error(f"Critical error occurred. Error: {str(e)} Please contact support.")


if __name__ == "__main__":
    main()
