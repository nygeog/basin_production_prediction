from capstone.etl.eia_retrieval import eia_retrieval
from capstone.etl.viirs_retrieval import viirs_retrieval
from capstone.etl.census_retrieval import census_retrieval
from capstone.etl.eia_parse import eia_parse_county
from capstone.etl.viirs_parse import viirs_parse
from capstone.etl.census_parse import parse_census
import glob


def data_retrieval(config):

    wd = f"{config['workspace_directory']}/data/input"

    census_shp = census_retrieval(f"{wd}/census")  # get counties for basins
    census_gdf = parse_census(census_shp)

    eia_cnty_xls = eia_retrieval(f"{wd}/eia")
    eia_cnty_gdf = eia_parse_county(eia_cnty_xls)

    viirs_retrieval(f"{wd}/viirs", '20200219', '20200223')
    viirs_files = glob.glob(f"{wd}/viirs/*.csv")  # glob to get viirs files

    for viirs_file in viirs_files:
        print(viirs_file)
        viirs = viirs_parse(viirs_file)
        