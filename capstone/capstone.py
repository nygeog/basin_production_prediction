from capstone.organization.create_project_workspace import create_workspace


def run_capstone(config):

    wd = config['workspace_directory']

    create_workspace(wd)
