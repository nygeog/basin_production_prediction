from capstone.etl.eia_retrieval import eia_retrieval
from capstone.etl.viirs_retrieval import viirs_retrieval
from capstone.etl.census_retrieval import census_retrieval
from capstone.etl.eia_parse import eia_parse_county
from capstone.etl.viirs_parse import viirs_parse
from capstone.etl.census_parse import parse_census
from tools.geoprocessing import point_in_polygon
from capstone.etl.generate_basins import generate_us_basins
import pandas as pd
import glob
import os
import warnings


warnings.filterwarnings("ignore", category=UserWarning)


def extract_transform_load(config):

    wd = f"{config['workspace_directory']}/data"

    census_shp = census_retrieval(f"{wd}/input/census")  # get data for basins
    census_gdf = parse_census(census_shp)

    eia_cnty_xls = eia_retrieval(f"{wd}/input/eia")
    eia_cnty = eia_parse_county(eia_cnty_xls)

    basins = generate_us_basins(census_gdf, eia_cnty, f"{wd}/input/basins")

    viirs_retrieval(f"{wd}/input/viirs", '20200219', '20200223')
    viirs_files = glob.glob(f"{wd}/input/viirs/*.csv")  # get viirs files

    for basin in basins:
        basin_name, basin_filename, basin_gdf = basin[0], basin[1], basin[2]

        print(f"selecting viirs for {basin_filename}")

        basin_int_viirs_list = []

        for viirs_file in viirs_files:
            print(f"    {os.path.basename(viirs_file)}")

            viirs_gdf = viirs_parse(viirs_file)

            viirs_int_basin = point_in_polygon(
                viirs_gdf,  # set to same crs as census
                basin_gdf,
            )

            basin_int_viirs_list.append(viirs_int_basin)

        basin_viirs = pd.concat(basin_int_viirs_list, sort=True)

        basin_viirs.to_file(
            f"{wd}/processing/{basin_filename}_int_viirs.gpkg",
            driver="GPKG",  # 'ESRI Shapefile',
        )
