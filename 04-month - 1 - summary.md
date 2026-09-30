![Image](dgk_Map3..jpeg)

## Question

Which wards in Dera Ghazi Khan Local Government Area, Punjab, are more than 7km from a health site?

## Operation

Buffered the health facilities by 7 km, intersected the buffer with settlement points, and used Union and ward-based joins to identify settlement coverage and gaps across Dera Ghazi Khan District (DG Khan).


## Expected

Expected settlements to have stronger 7 km coverage around health-facility clusters and more densely settled areas, while more dispersed settlements—particularly toward the western and southern parts of the district—would be more likely to fall outside the coverage area.

## Got

The analysis identified 410 of 2,186 settlements within 7 km of a health facility, leaving 1,776 settlements outside the 7 km coverage area. The map shows that covered settlements are concentrated around health-facility clusters, while many settlements across the wider district remain outside the 7 km buffers.


## What surprised me

- Only about 19% of settlements (410/2,186) fall within the 7 km health-facility coverage area, highlighting a substantial spatial accessibility gap.
- The uncovered settlements are widely dispersed, rather than being concentrated in a single location.
- The results also show why settlement distribution matters: a large district-wide buffer does not necessarily mean that individual settlements have practical access to healthcare.

## What data I still need

- A road network with speed attributes, to upgrade the 7 km straight-line buffer into a real travel-time catchment
- Population data, to estimate the number of people living in underserved areas.
- Facility service-area data, to identify the actual areas served by each health facility.