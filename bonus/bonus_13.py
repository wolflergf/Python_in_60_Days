feet_inches_str = input("Enter feet and inches (e.g., 10 20): ")


def parse(feet_inches_str):
    parts = feet_inches_str.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches_str)

result = convert(parsed["feet"], parsed["inches"])

print("{} feet and {} inches is equal to {} meters".format(parsed["feet"], parsed["inches"], result))

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")
