# extract.py
import json
import time
import requests
import random
from datetime import datetime, timedelta
from pathlib import Path

# Define Base Paths
BASE_DIR = Path(__file__).resolve().parents[0]
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# API Endpoints (Fictional)
DELIVERY_API_URL = "https://api.swiftshipexpress.in/v1/deliveries/live"
TRAFFIC_API_URL = "https://api.swiftshipexpress.in/v1/traffic/routes"

# --- Mock Data Generators (To simulate API when offline) ---
def generate_mock_delivery_data():
    cities = ["Hyderabad", "Bangalore", "Mumbai", "Delhi", "Chennai"]
    data = []
    for i in range(5): # Simulate 5 shipments
        source = random.choice(cities)
        dest = random.choice([c for c in cities if c != source])
        dispatch = datetime.now() - timedelta(hours=random.randint(1, 48))
        
        data.append({
            "shipment_id": f"SWIFT-{random.randint(10000, 99999)}",
            "source_city": source,
            "destination_city": dest,
            "dispatch_time": dispatch.isoformat(),
            "expected_delivery_time": (dispatch + timedelta(hours=random.randint(5, 24))).isoformat(),
            "actual_delivery_time": None if random.random() > 0.5 else (dispatch + timedelta(hours=random.randint(5, 26))).isoformat(),
            "package_weight_kg": round(random.uniform(0.5, 20.0), 2),
            "delivery_agent_id": f"AGT-{random.randint(100, 999)}"
        })
    return data

def generate_mock_traffic_data():
    cities = ["Hyderabad", "Bangalore", "Mumbai", "Delhi", "Chennai"]
    data = []
    for city in cities:
        data.append({
            "city_name": city,
            "traffic_congestion_score": random.randint(1, 10),
            "average_speed_kmh": random.randint(10, 60),
            "weather_warnings": random.choice(["None", "Heavy Rain", "Fog", "Heatwave"])
        })
    return data

# --- Main Extraction Logic ---

def fetch_data_with_retry(url: str, retries: int = 3, delay: int = 2, mock_fallback: bool = True):
    """
    Fetch API data with retry logic. Falls back to mock data if URL fails.
    """
    for attempt in range(1, retries + 1):
        try:
            print(f"   Trying connection to {url} (Attempt {attempt})...")
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            if attempt < retries:
                time.sleep(delay)
            else:
                print(f"⚠️ Connection failed. Switching to MOCK MODE for demonstration.")
                if mock_fallback:
                    if "deliveries" in url:
                        return generate_mock_delivery_data()
                    elif "traffic" in url:
                        return generate_mock_traffic_data()
                return None

def extract_delivery_data():
    print(f"⏳ Requesting Live Delivery Data...")
    data = fetch_data_with_retry(DELIVERY_API_URL)
    
    if data:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = RAW_DIR / f"delivery_{timestamp}.json"
        filename.write_text(json.dumps(data, indent=2))
        print(f"✅ Extracted {len(data)} delivery records to: {filename}")
        return str(filename)

def extract_traffic_data():
    print(f"⏳ Requesting Route Traffic Data...")
    data = fetch_data_with_retry(TRAFFIC_API_URL)
    
    if data:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = RAW_DIR / f"traffic_{timestamp}.json"
        filename.write_text(json.dumps(data, indent=2))
        print(f"✅ Extracted {len(data)} traffic records to: {filename}")
        return str(filename)

if __name__ == "__main__":
    extract_delivery_data()
    print("-" * 30)
    extract_traffic_data()