from capstone.etl.eia_retrieval import eia_retrieval
from capstone.etl.viirs_retrieval import viirs_retrieval
from capstone.etl.census_retrieval import census_retrieval
from capstone.etl.eia_parse import eia_parse_county, eia_parse_data
from capstone.etl.census_parse import parse_census
from capstone.etl.generate_basins import generate_us_basins
from capstone.etl.viirs_join_basins import viirs_join_basins, compile_basin_data
from capstone.etl.aggregate_viirs import aggregate_viirs_by_basin_month
import warnings
import glob
import pandas as pd

warnings.filterwarnings("ignore", category=UserWarning)


def extract_transform_load(config):

    wd = f"{config['workspace_directory']}/data"

    census_shp = census_retrieval(f"{wd}/input/census")  # get data for basins
    census_gdf = parse_census(census_shp)

    eia_xls = eia_retrieval(f"{wd}/input/eia")
    eia_cnty = eia_parse_county(eia_xls)
    eia_data = eia_parse_data(eia_xls)  # parse the target variable(s) data

    basins = generate_us_basins(census_gdf, eia_cnty, f"{wd}/input/basins")

    viirs_retrieval(
        f"{wd}/input/viirs21c",
        '20171101',
        '20171130',
        version='v21',  # version 21 for older data
    )

    viirs_retrieval(
        f"{wd}/input/viirs30",
        '20171201',
        '20171231',
        version='v30',  # version 30 for latest data
    )

    viirs_2_1c_files = glob.glob(f"{wd}/input/viirs21c/*.csv")  # get viirs
    viirs_2_1c_files.sort()  # sort so dates are consecutive for tracking

    viirs_3_0_files = glob.glob(f"{wd}/input/viirs30/*.csv")  # get viirs files
    viirs_3_0_files.sort()  # sort so dates are consecutive for tracking

    viirs_2_1c_int_basins = viirs_join_basins(
        wd,
        basins,
        viirs_2_1c_files,
        '21c',
    )

    viirs_3_0_int_basins = viirs_join_basins(
        wd,
        basins,
        viirs_3_0_files,
        '30',
    )

    compile_basin_data(wd, basins, '21c')
    compile_basin_data(wd, basins, '30')

    # viirs_int_basins =  pd.read_csv(
    #     '/Users/danielmsheehan/general_assembly/github/projects/project_6/capstone/data/processing/complete/all_int_viirs.csv',
    #     parse_dates=["date_mscan"]
    # )

    # viirs_2_1c_int_basins
    # viirs_3_0_int_basins
    # eia_agg_viirs = aggregate_viirs_by_basin_month(viirs_int_basins, eia_data)
    #
    # eia_agg_viirs.to_csv(f"{wd}/processing/eia_agg_viirs.csv", index=False)
