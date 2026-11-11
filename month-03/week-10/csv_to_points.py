import pandas as pd
import geopandas as gpd

# Read the new CSV file with longitude and latitude
table = pd.read_csv(
    "Data/raw/Health_Facilities_longitude_latitude.csv"
)

# Convert CSV to point features
facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(
        table["longitude"],
        table["latitude"]
    ),
    crs="EPSG:4326"
)

# Display results
print(facilities.head())
print("Rows and columns:", facilities.shape)
print("CRS:", facilities.crs)