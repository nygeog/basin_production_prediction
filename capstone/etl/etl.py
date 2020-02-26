from capstone.etl.eia_retrieval import eia_retrieval
from capstone.etl.viirs_retrieval import viirs_retrieval
from capstone.etl.census_retrieval import census_retrieval
from capstone.etl.eia_parse import eia_parse_county, eia_parse_data
from capstone.etl.census_parse import parse_census
from capstone.etl.generate_basins import generate_us_basins
from capstone.etl.viirs_join_basins import viirs_join_basins
import glob
import warnings


warnings.filterwarnings("ignore", category=UserWarning)


def extract_transform_load(config):

    wd = f"{config['workspace_directory']}/data"

    census_shp = census_retrieval(f"{wd}/input/census")  # get data for basins
    census_gdf = parse_census(census_shp)

    eia_xls = eia_retrieval(f"{wd}/input/eia")
    eia_cnty = eia_parse_county(eia_xls)
    eia_parse_data(eia_xls)  # parse the target variable(s) data

    basins = generate_us_basins(census_gdf, eia_cnty, f"{wd}/input/basins")

    viirs_retrieval(f"{wd}/input/viirs", '20200222', '20200226')
    viirs_files = glob.glob(f"{wd}/input/viirs/*.csv")  # get viirs files

    viirs_join_basins(wd, basins, viirs_files)
