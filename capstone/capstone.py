from capstone.organization.create_project_workspace import create_workspace
from capstone.etl.etl import extract_transform_load


def run_capstone(config):
    # set up the project workspace directories, etc.
    create_workspace(config)
    # perform all of the necessary extraction, transformation cleaning, loading
    extract_transform_load(config)
