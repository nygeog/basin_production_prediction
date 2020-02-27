import geopandas as gpd
import pandas as pd

df = pd.read_csv(
    '/Users/danielmsheehan/general_assembly/github/projects/project_6/capstone/data/processing/all_int_viirs.csv')
df

x = '/Users/danielmsheehan/general_assembly/github/projects/project_6/capstone/data/processing/complete'
gdf_list = []
for i in [
    'anadarko_region_int_viirs.gpkg',
    'haynesville_region_int_viirs.gpkg',
    'appalachia_region_int_viirs.gpkg',
    'niobrara_region_int_viirs.gpkg',
    'bakken_region_int_viirs.gpkg',
    'permian_region_int_viirs.gpkg',
    'eagle_ford_region_int_viirs.gpkg'
]:
    gdf = gpd.read_file(f'{x}/{i}')
    gdf_list.append(gdf)

x = '/Users/danielmsheehan/general_assembly/github/projects/project_6/capstone/data/processing/complete'
gdf_list = []
for i in [
    'anadarko_region_int_viirs.gpkg',
    'haynesville_region_int_viirs.gpkg',
    'appalachia_region_int_viirs.gpkg',
    'niobrara_region_int_viirs.gpkg',
    'bakken_region_int_viirs.gpkg',
    'permian_region_int_viirs.gpkg',
    'eagle_ford_region_int_viirs.gpkg'
]:
    gdf = gpd.read_file(f'{x}/{i}')
    gdf_list.append(gdf)
gdf_all = pd.concat(gdf_list, sort=True)
gdf.to_csv(f'{x}/all.csv', index=False)
gdf.to_file(f'{x}/all_complete.gpkg', driver="GPKG")
gdf_all.to_csv(f'{x}/all.csv', index=False)
gdf_all.to_file(f'{x}/all_complete.gpkg', driver="GPKG")