import urllib.request
from pathlib import Path


def eia_retrieval(workspace_directory):
    filename = "dpr-data.xlsx"

    if not Path(f"{workspace_directory}/{filename}").is_file():
        url = "https://www.eia.gov/petroleum/drilling/xls/"

        urllib.request.urlretrieve(
            f"{url}/{filename}",
            f"{workspace_directory}/{filename}",
        )

    return f"{workspace_directory}/{filename}"
