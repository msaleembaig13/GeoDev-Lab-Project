import pandas as pd

pop = pd.read_csv("Data/raw/ward_population.csv")

big = pop[pop["TEHSIL_POPULATION"] > 3500]
print(big)
print("Records over 3,500:", len(big))

ranked = pop.sort_values("TEHSIL_POPULATION", ascending=False)
print(ranked.head(3))

pop["total population"] = pop["TEHSIL_POPULATION"] /1000
print(pop.head())
print("Total Population:", pop["total population"].sum())
