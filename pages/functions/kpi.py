def gases_kpi(value, range_dict):

    if value <= range_dict["medium"]:
        return {
            "icon": "✅",
            "status": "green"
        }
    elif value <= range_dict["high"]:
        return {
            "icon": "⚠️",
            "status": "#FFD700"
        }
    else: return {
        "icon": "🚨",
        "status": "red"
    }

def temperature_kpi(value, range_dict):
    
    if value <= range_dict["low"]:
        return {
            "icon": "❄️",
            "status": "#34a8eb"
        }
    elif value <= range_dict["medium"]:
        return {
            "icon": "✅",
            "status": "green",
        }
    else:
        return {
            "icon": "🌡️",
            "status": "orange"
        }

