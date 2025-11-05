import os
from dotenv import load_dotenv

load_dotenv()

AI_MODEL_PATH = os.getenv("AI_MODEL_PATH", "./app/models/traffic_model.joblib")

AI_API_URL = os.getenv("AI_API_URL", "http://127.0.0.1:9000/predict")
BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://localhost:8080/api/traffic/predictions")
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&hourly=temperature_2m"
POLLUTION_API_URL = "https://api.openaq.org/v2/measurements?city=Bengaluru&limit=5"

DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:password@localhost:3306/smartcity")

LOG_DIR = os.getenv("LOG_DIR", "./logs")
os.makedirs(LOG_DIR, exist_ok=True)
