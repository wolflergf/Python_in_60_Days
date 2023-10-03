try:
    width = float(input("Enter rectangle width: "))
    lenght = float(input("Enter rectangle lenght: "))

    if width == lenght:
        exit("That looks lika a square.")

    area = width * lenght
    print(area)

except ValueError:
    print("Please enter a number.")
