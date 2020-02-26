import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


def viirs_parse():
    viirs = pd.read_csv(
        '../data/input/viirs/VNF_npp_d20171201_noaa_v30-ez.csv'
    )

    viirs.columns = [c.lower() for c in viirs.columns]

    # create point geometries column - from noah's local folium lesson
    viirs_gdf = gpd.GeoDataFrame(
        viirs,
        crs={'init': 'epsg:4326'},
        geometry=[
            Point(xy) for xy in zip(viirs['lon_gmtco'], viirs['lat_gmtco'])
        ],
    )

    return viirs_gdf
