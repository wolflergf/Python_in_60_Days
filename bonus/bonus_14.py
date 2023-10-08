from parses14 import parse
from converts14 import convert

feet_inches_str = input("Enter feet and inches (e.g., 10 20): ")

parsed = parse(feet_inches_str)

result = convert(parsed["feet"], parsed["inches"])

print("{} feet and {} inches is equal to {} meters".format(parsed["feet"], parsed["inches"], result))

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")
