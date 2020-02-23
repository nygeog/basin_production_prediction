from tools.tools import get_current_time, create_directory


def create_workspace(workspace_directory):
    print('creating project workspace')

    run_datetime = get_current_time('yyyymmdd_hhmm')
    project = f'{workspace_directory}'

    create_directory(project)

    for i in [
        'data/input',
        'data/processing',
        'data/shadows',
        'data/output',
        # 'maps/output',
        # 'maps/mxd',
        # 'maps/mpk',
        # 'report/'
    ]:
        create_directory('{}/{}'.format(project, i))

    print('    project workspace created at: {}'.format(project))

    return project, run_datetime
