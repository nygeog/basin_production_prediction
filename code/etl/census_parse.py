import geopandas as gpd


def parse_census(census_shp):
    census = gpd.read_file(census_shp)

    census.columns = [c.lower() for c in census.columns]

    return census
