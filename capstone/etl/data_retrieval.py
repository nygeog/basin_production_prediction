from capstone.etl.eia_retrieval import eia_retrieval
from capstone.etl.viirs_retrieval import viirs_retrieval
from capstone.etl.census_retrieval import census_retrieval


def data_retrieval(config):

    wd = f"{config['workspace_directory']}/data/input"

    census_retrieval(f"{wd}/census")  # get counties data for basins

    eia_retrieval(f"{wd}/eia")

    viirs_retrieval(f"{wd}/viirs", '20200219', '20200223')
