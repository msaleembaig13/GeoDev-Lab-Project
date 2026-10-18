from pathlib import Path
import geopandas as gpd

def main():
    project_root = Path(__file__).resolve().parents[2]
    roads_file = project_root / "Roads.geojson"

    gdf = gpd.read_file(roads_file)

    print(gdf.shape)
    print(gdf.head())

if __name__ == "__main__":
    main()
