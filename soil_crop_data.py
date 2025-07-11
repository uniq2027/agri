def get_crops_by_soil(soil_type):
    
    soil_crop_map = {
        "Black Soil": ["Cotton", "Soybean", "Pulses"],
        "Alluvial Soil": ["Rice", "Wheat", "Sugarcane"],
        "Red Soil": ["Groundnut", "Millets", "Potato"],
        "Laterite Soil": ["Tea", "Coffee", "Cashew"],
        "Desert Soil": ["Millets", "Barley", "Dates"]
    }
    return soil_crop_map.get(soil_type, ["No data available"])
