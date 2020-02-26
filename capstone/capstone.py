from capstone.organization.create_project_workspace import create_workspace
from capstone.etl.etl import data_retrieval


def run_capstone(config):

    create_workspace(config)

    data_retrieval(config)
