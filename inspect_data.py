import csv

# with open('states.csv', encoding='utf-8-sig') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)


# values = []
# for row in rows:
#    row = row["area_km2"].strip()
#    if row == "":
#          continue
#    values.append(float(row))


# print("Largest Value: ", max(values))
# print("Smallest Value: ", min(values))
# print("Count: ", len(values))


def inspect_column(filename, column):
    with open(filename, encoding= "utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        row = row[column].strip()
        if row == "":
            continue
        values.append(float(row))

    return{
        "smallest":min(values),
        "largest":max(values),
        "count":len(values)
    }

result = inspect_column("states.csv", "area_km2")
print(result)
result = inspect_column("states.csv", "LGAS")
print(result)
