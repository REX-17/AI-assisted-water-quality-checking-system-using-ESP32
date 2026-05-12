def generate_advice(classification, trend, api):
    if trend == "Degrading":
        urgency = "High" if api > 0.7 else "Moderate"
        return (
            f"Water quality is {classification}. "
            f"A degrading trend has been detected with {urgency} urgency. "
            "Preventive actions such as sediment filtration, controlled aeration, "
            "or phytoremediation are recommended."
        )
    elif trend == "Stable":
        return (
            f"Water quality is {classification}. "
            "Conditions are stable. Continued monitoring is advised."
        )
    else:
        return (
            f"Water quality is {classification}. "
            "An improving trend is observed. No immediate action required."
        )
