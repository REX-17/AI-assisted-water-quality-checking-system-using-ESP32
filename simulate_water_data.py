import time
import random
from collections import deque
from ai_advisory import generate_advice

# -------- CONFIGURATION --------
N = 10                  # number of samples for trend
READ_INTERVAL = 5       # seconds between readings

TURBIDITY_SAFE = 300
TURBIDITY_MODERATE = 700

# -------- DATA STORAGE --------
history = deque(maxlen=N)

# -------- HELPER FUNCTIONS --------
def classify(turbidity):
    if turbidity < TURBIDITY_SAFE:
        return "Clean"
    elif turbidity < TURBIDITY_MODERATE:
        return "Moderate"
    else:
        return "Heavy"

def detect_trend(data):
    if len(data) < N:
        return "Insufficient Data"

    slope = (data[-1] - data[0]) / N
    if slope > 5:
        return "Degrading"
    elif slope < -5:
        return "Improving"
    else:
        return "Stable"

def action_priority_index(turbidity):
    return round(min(turbidity / 1000, 1.0), 2)

# -------- SIMULATION START --------
turbidity = 200  # start with clean water

while True:
    # Simulate gradual contamination
    turbidity += random.randint(0, 25)
    history.append(turbidity)

    # Core logic
    classification = classify(turbidity)
    trend = detect_trend(list(history))
    api = action_priority_index(turbidity)

    # 🔹 AI ADVISORY (INSIDE LOOP) 🔹
    advice = generate_advice(classification, trend, api)

    # Output
    print({
        "turbidity": turbidity,
        "classification": classification,
        "trend": trend,
        "action_priority_index": api
    })
    print("AI Advisory:", advice)
    print("-" * 60)

    time.sleep(READ_INTERVAL)

#to run it , in a new terminal the address should be 
# C:\Users\ranes\OneDrive\Desktop\water_quality_backend\simulation> python simulate_water_data.py 
#to stop it do CTRL C