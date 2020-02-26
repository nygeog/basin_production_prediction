from capstone.organization.create_project_workspace import create_workspace
from capstone.etl.etl import extract_transform_load


def run_capstone(config):

    create_workspace(config)

    extract_transform_load(config)
