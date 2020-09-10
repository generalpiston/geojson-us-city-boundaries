# geojson-us-city-boundaries

US Census tiger data set places transformed to GeoJSON.

Data sourced from: https://www2.census.gov/geo/tiger/TIGER2019/PLACE/
FIPS Codes: https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code#FIPS_state_codes

Compression: pushd cities && zip -rs 10m /tmp/cities.zip .; popd;
TODO: Respect cities with same name in different states
