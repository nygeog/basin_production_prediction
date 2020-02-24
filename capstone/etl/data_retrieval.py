from capstone.etl.eia_retrieval import eia_retrieval
from capstone.etl.viirs_retrieval import viirs_retrieval


def data_retrieval(config):

    wd = f"{config['workspace_directory']}/data/input/"

    viirs_retrieval(f"{wd}/viirs", '20200219', '20200223')

    eia_retrieval(f"{wd}/eia")
