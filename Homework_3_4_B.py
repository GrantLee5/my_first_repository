import csv

loaded_members = []

with open("members.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)
        loaded_members.append(row)


print(loaded_members)        