from capstone.etl.eia_retrieval import eia_retrieval
from capstone.etl.viirs_retrieval import viirs_retrieval


def data_retrieval(config):

    wd = "/Users/danielmsheehan/general_assembly/github/projects/project_6/capstone/data/input/viirs"

    viirs_retrieval(wd, '20171201', '20200223')

    eia_retrieval(wd)
