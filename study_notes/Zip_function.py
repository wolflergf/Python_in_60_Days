countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]

for countries, filenames in zip(countries, filenames):
    with open(f"{filenames}", "w") as file:
        file.write(countries)


# Create a text file for each country
for country in countries:
    with open(f"{country}.txt", "w") as file:
        file.write(country)
