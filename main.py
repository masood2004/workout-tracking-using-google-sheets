import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
EXERCISE_API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_URL = "https://api.sheety.co/4710e690813d69d7bfcb4d692d2c9332/myWorkouts/workouts"

# User profile data
GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 183
AGE = 20

# Validate essential API keys
if not APP_ID or not API_KEY:
    print("❌ ERROR: Missing API credentials. Please check your .env file.")
    exit()

# Headers for Nutritionix API
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

def get_exercise_data(query, gender, weight, height, age):
    payload = {
        "query": query,
        "gender": gender,
        "weight_kg": weight,
        "height_cm": height,
        "age": age,
    }
    try:
        response = requests.post(EXERCISE_API_URL, json=payload, headers=exercise_headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"⚠️ Error connecting to exercise API: {e}")
        return None

def log_to_sheety(entry):
    try:
        response = requests.post(SHEETY_API_URL, json=entry)
        response.raise_for_status()
        print("✅ Workout logged successfully!")
    except requests.RequestException as e:
        print(f"⚠️ Failed to log workout to Sheety: {e}")

def main():
    print("🏋️ Welcome to the Smart Workout Tracker!")
    query = input("Tell me what exercise you did today: ").strip()
    gender = input("What is your gender: ").strip()
    weight = input("What is your weight (kg): ").strip()
    height = input("What is your height (cm): ").strip()
    age = input("What is your age?: ").strip()

    if not query:
        print("❌ No exercise input received. Please try again.")
        return

    print("⏳ Fetching exercise details...")
    exercise_data = get_exercise_data(query, gender, weight, height, age)

    if not exercise_data or "exercises" not in exercise_data:
        print("⚠️ No valid data received from the API.")
        return

    now = datetime.now()

    for exercise in exercise_data["exercises"]:
        workout_entry = {
            "workout": {
                "date": now.strftime("%d/%b/%Y"),
                "time": now.strftime("%I:%M:%S %p"),
                "exercise": exercise.get("name", "Unknown").title(),
                "duration": exercise.get("duration_min"),
                "calories": exercise.get("nf_calories")
            }
        }

        print(f"📋 Logging: {workout_entry['workout']}")
        log_to_sheety(workout_entry)

if __name__ == "__main__":
    main()
