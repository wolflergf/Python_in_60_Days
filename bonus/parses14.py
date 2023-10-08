def parse(feet_inches_str):
    parts = feet_inches_str.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
