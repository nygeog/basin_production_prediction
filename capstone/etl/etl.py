from capstone.etl.viirs_retrieval import viirs_retrieval
from capstone.etl.census_retrieval import census_retrieval
from capstone.etl.census_parse import parse_census
from capstone.etl.eia_retrieval import eia_retrieval
from capstone.etl.eia_parse import eia_parse_county, eia_parse_data
from capstone.etl.generate_basins import generate_us_basins
from capstone.etl.viirs_join_basins import viirs_join_basins, compile_basin_data
from capstone.etl.aggregate_viirs import aggregate_viirs_by_basin_month
import warnings
import glob
import pandas as pd
from tools.tools import get_current_time


warnings.filterwarnings("ignore", category=UserWarning)


def extract_transform_load(config):
    current_date = get_current_time('yyyymmdd')

    # add function here to check if v30 sorted by date has current_date data

    wd = f"{config['workspace_directory']}/data"

    census_shp = census_retrieval(f"{wd}/input/census")  # get data for basins
    census_gdf = parse_census(census_shp)

    eia_xls = eia_retrieval(f"{wd}/input/eia")
    eia_cnty = eia_parse_county(eia_xls)
    eia_data = eia_parse_data(eia_xls)  # parse the target variable(s) data

    basins_list, all_basins = generate_us_basins(
        census_gdf,
        eia_cnty,
        f"{wd}/input/basins",
    )

    viirs_retrieval(
        f"{wd}/input/viirs21c",
        '20120308',
        '20171130',
        version='v21',  # version 21 for older data
    )

    viirs_retrieval(
        f"{wd}/input/viirs30",
        '20171201',
        current_date,
        version='v30',  # version 30 for latest data
    )

    viirs_2_1c_files = glob.glob(f"{wd}/input/viirs21c/*.csv")  # get viirs
    viirs_2_1c_files.sort()  # sort so dates are consecutive for tracking
    print(f'Total 2.1c files: {len(viirs_2_1c_files)}')

    viirs_3_0_files = glob.glob(f"{wd}/input/viirs30/*.csv")  # get viirs files
    viirs_3_0_files.sort()  # sort so dates are consecutive for tracking
    print(f'Total 3.0 files: {len(viirs_3_0_files)}')

    # viirs_join_basins(
    #     wd,
    #     all_basins,
    #     viirs_2_1c_files,
    #     '21c',
    # )
    #
    # viirs_join_basins(
    #     wd,
    #     all_basins,
    #     viirs_3_0_files,
    #     '30',
    # )
    #
    # basins_int_viirs_21c = compile_basin_data(wd, '21c')
    # basins_int_viirs_30  = compile_basin_data(wd, '30')

    # basins_int_viirs_21c = pd.read_csv(
    #     f"{wd}/processing/basins_int_viirs_21c.csv"
    # )
    # basins_int_viirs_30  = pd.read_csv(
    #     f"{wd}/processing/basins_int_viirs_30.csv"
    # )

    # print(basins_int_viirs_21c.shape)
    #
    # print(basins_int_viirs_30.shape)

    # eia_agg_viirs = aggregate_viirs_by_basin_month(viirs_int_basins, eia_data)
    #
    # eia_agg_viirs.to_csv(f"{wd}/processing/eia_agg_viirs.csv", index=False)
