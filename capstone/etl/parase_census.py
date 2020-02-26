import geopandas as gpd


def parse_census():
    census = gpd.read_file(
        '../data/input/census/tl_2017_us_county.shp'
    )

    census.columns = [c.lower() for c in census.columns]

    return census
