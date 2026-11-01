import csv

def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return(list(csv.DictReader(f)))

    
def clean_values(rows, column):
    values = []
    for row in rows:
        row = row[column].strip()
        if row == "":
            continue
        values.append(float(row))
    return(values)

def summarise(values):
    if len(values) == 0:
        return {"count": 0, "smallest": None, "largest": None, "average":None}
    return{ "smallest": min(values),
            "largest": max(values),
            "count": len(values),
            "average": sum(values) / len(values)
          }



def summarise_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
        return(report)

report = summarise_all("states.csv", ["area_km2", "lgas"])

for column, states in report.items():
    print(column, " -> ", states)