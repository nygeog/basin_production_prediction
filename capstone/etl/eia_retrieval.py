import urllib.request


def eia_retrieval(workspace_directory):
    url = "https://www.eia.gov/petroleum/drilling/xls/"
    filename = "dpr-data.xlsx"

    urllib.request.urlretrieve(
        f"{url}/{filename}",
        f"{workspace_directory}/{filename}",
    )


wd = "/Users/danielmsheehan/general_assembly/github/projects/project_6/capstone/data/input/eia"

eia_retrieval(wd)