# import geopandas as gpd
# from pathlib import Path

# gpkg_path = Path("Data/processed/wards.gpkg")

# print("File exists:", gpkg_path.exists())

# if gpkg_path.exists():
#     print("Available layers:")
#     print(gpd.list_layers(gpkg_path))

import geopandas as gpd

# Read the correct GeoPackage layer
wards = gpd.read_file(
    "Data/processed/wards.gpkg",
    layer="wards_boundary"
)

# Display first 5 records
print(wards.head())

# Display rows and columns
print("Rows and columns:", wards.shape)

# Display coordinate reference system
print("CRS:", wards.crs)

# Display geometry type
print("Geometry type:", wards.geom_type.unique())

