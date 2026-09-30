# Data Notes

Mapping of **Dera Ghazi Khan** Healthcare Accessibility using open data

## Datasets

- HumanitarianDataExchange
[Source link](https://data.humdata.org)
- OpenStreetMap
[Source link](https://www.openstreetmap.org)
- OpenDataSets (PakistanHealthSites)
[Source link](https://opendata.com.pk/dataset/pakistan-health-sites)

- OpenStreetMap / Geofabrik
[Source link](https://download.geofabrik.de)
- WorldPod
[Source link](https://www.worldpop.org)

## Dera Ghazi Khan District Boundary

```bash
- Source: Humanitarian Data Exchange (HDX) / OCHA — https://data.humdata.org
- Study Area: Dera Ghazi Khan District, Punjab, Pakistan
- Geometry: Polygon
- CRS: EPSG:4326 (WGS 84)
- Completeness: The district boundary provides full coverage of the study area
- Attribute: Contains administrative information required for District-level analysis

Note: Study area extracted from the Pakistan administrative boundary dataset (pakadm)

The district boundary was used to define the project study area
```

## Tehsil Boundary

```bash
- Source: Humanitarian Data Exchange (HDX) / OCHA — https://data.humdata.org
- Study area: Dera Ghazi Khan District
- Geometry: Polygons
- CRS: EPSG:4326 (WGS 84)
- Completeness: The available tehsil boundaries cover the study area
- Attribute: Contains administrative information required for Tehsil-level analysis

Note: Used to analyze healthcare accessibility patterns across different tehsils
```



## Health Facilities

```bash
- Source: Open Data Pakistan — Pakistan Health Sites — https://opendata.com.pk/dataset/pakistan-health-sites

-
Study area: Dera Ghazi Khan District

- Geometry: Points

- CRS: EPSG:4326 (WGS 84)
- Completeness: The dataset may not contain every health facility currently operating in the study area

- Positional: Facility locations should be reviewed against available reference imagery or other authoritative sources

- Attribute: Facility names and available facility-type information support the healthcare accessibility analysis

- Fitness: It is fit for identifying potential healthcare access points, subject to completeness and positional limitations

Notes: Used to represent healthcare facilities within the study area
Facility types may include hospitals, Basic Health Units (BHUs),Rural Health Centres (RHCs), dispensaries, and other healthcare facilities
```
## Roads

```bash
- Source: OpenStreetMap / Geofabrik — https://download.geofabrik.de

- Study area: Dera Ghazi Khan District

- Geometry: Lines

- CRS: EPSG:4326 (WGS 84)
-Completeness: Road coverage may be incomplete in some rural and remote areas

- Currency: OpenStreetMap road data is continuously updated; the download date should be recorded with the final dataset

- Positional: Road geometries should be reviewed against satellite imagery where necessary

- Attribute: Available road classifications and road-network attributes support network preparation

- Fitness: It is fit for road-network distance analysis, subject to network completeness and connectivity limitations

Notes: Used to construct the road network for shortest-path accessibility analysis
```













